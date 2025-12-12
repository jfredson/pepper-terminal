import os
from openai import OpenAI
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

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages,
                temperature=0.4
            )

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

