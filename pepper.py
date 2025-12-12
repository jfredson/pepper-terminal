import os
import json
from datetime import datetime, timezone
from pathlib import Path
from openai import OpenAI
from openai import APIConnectionError, AuthenticationError, RateLimitError, NotFoundError, BadRequestError
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

console = Console()

SYSTEM_PROMPT = """You are Pepper: calm, precise, thoughtful, and collaborative.
You acknowledge uncertainty when appropriate.
You do not hallucinate.
You speak clearly, concisely, and with warmth.
"""

# ---------- Persistent Memory (local) ----------
APP_DIR = Path(__file__).resolve().parent
MEMORY_DIR = APP_DIR / "memory"

def memory_file_for_today() -> Path:
    # Local date-based filename (simple + readable)
    today = datetime.now().date().isoformat()  # YYYY-MM-DD
    return MEMORY_DIR / f"{today}.jsonl"

# How many recent messages to reload into context each run (keeps token cost sane)
RECALL_MESSAGES = 30

def ensure_memory_dir() -> None:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

def append_event(role: str, content: str) -> None:
    """Append a single message event to JSONL log."""
    ensure_memory_dir()
    event = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "role": role,
        "content": content,
    }
    mem_file = memory_file_for_today()
    with mem_file.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")

def load_recent_messages(limit: int) -> list[dict]:
    """Load last N messages from JSONL log (role/content only)."""
    mem_file = memory_file_for_today()
    if not mem_file.exists():
        return []
    lines = mem_file.read_text(encoding="utf-8").splitlines()
    tail = lines[-limit:] if limit > 0 else []
    msgs: list[dict] = []
    for line in tail:
        try:
            event = json.loads(line)
            role = event.get("role")
            content = event.get("content")
            if role in ("system", "user", "assistant") and isinstance(content, str):
                msgs.append({"role": role, "content": content})
        except json.JSONDecodeError:
            # Ignore malformed lines (should be rare)
            continue
    return msgs

def clear_memory() -> None:
    """Delete the JSONL conversation log (if it exists)."""
    mem_file = memory_file_for_today()
    if mem_file.exists():
        mem_file.unlink()


def help_text() -> str:
    return (
        "Local commands:\n"
        "  :help   Show this help\n"
        "  :where  Show the memory file path\n"
        "  :new    Reset in-session context (does not delete memory file)\n"
        "  :clear  Delete today's memory file (asks for confirmation)\n"
        "  exit    Quit\n"
    )

def main():
    console.print("[bold cyan]Pepper Terminal v0.1[/bold cyan]")
    console.print("Type 'exit' to quit.\n")

    # Start with system prompt, then reload recent conversation
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(load_recent_messages(RECALL_MESSAGES))

    while True:
        try:
            user_input = console.input("[bold green]You > [/bold green]")
            # ----- Local commands (handled before conversation logic) -----
            if user_input.strip() == ":new":
                console.print("\n[dim]Starting a fresh in-session context (log remains on disk).[/dim]\n")
                messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                continue

            if user_input.strip() == ":where":
                console.print(f"\n[dim]Memory file: {memory_file_for_today()}[/dim]\n")
                continue

            if user_input.lower() in ("exit", "quit"):
                console.print("\n[dim]Goodbye.[/dim]")
                break

            messages.append({"role": "user", "content": user_input})

            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=messages,
                    temperature=0.4
                )
            except RateLimitError as e:
                console.print("\n[bold red]Pepper >[/bold red] API quota/rate limit hit.")
                console.print("[dim]If this says insufficient_quota, enable API billing or increase your usage limit.[/dim]\n")
                continue
            except AuthenticationError:
                console.print("\n[bold red]Pepper >[/bold red] Authentication failed.")
                console.print("[dim]Check OPENAI_API_KEY in .env and make sure it’s active (not revoked).[/dim]\n")
                continue
            except APIConnectionError:
                console.print("\n[bold red]Pepper >[/bold red] Network error connecting to OpenAI.")
                console.print("[dim]Check internet/VPN/firewall and try again.[/dim]\n")
                continue
            except NotFoundError:
                console.print("\n[bold red]Pepper >[/bold red] Model or endpoint not found.")
                console.print("[dim]Try switching the model to 'gpt-4o-mini' in pepper.py.[/dim]\n")
                continue
            except BadRequestError as e:
                console.print("\n[bold red]Pepper >[/bold red] Bad request.")
                console.print(f"[dim]{e}[/dim]\n")
                continue

            reply = response.choices[0].message.content
            messages.append({"role": "assistant", "content": reply})
            append_event("user", user_input)

            console.print("\n[bold magenta]Pepper >[/bold magenta]")
            console.print(Markdown(reply))
            console.print()

        except KeyboardInterrupt:
            console.print("\n[dim]Interrupted.[/dim]")
            break

if __name__ == "__main__":
    main()

