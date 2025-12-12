import os
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

def main():
    console.print("[bold cyan]Pepper Terminal v0.1[/bold cyan]")
    console.print("Type 'exit' to quit.\n")

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            user_input = console.input("[bold green]You > [/bold green]")
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

            console.print("\n[bold magenta]Pepper >[/bold magenta]")
            console.print(Markdown(reply))
            console.print()

        except KeyboardInterrupt:
            console.print("\n[dim]Interrupted.[/dim]")
            break

if __name__ == "__main__":
    main()

