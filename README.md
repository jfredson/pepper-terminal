# Pepper Terminal

Pepper Terminal is a lightweight local terminal client that connects to OpenAI’s API and provides a calm, precise, and collaborative conversational interface designed for long-form thinking, reflection, and structured development.

It is intentionally minimal. Pepper Terminal prioritizes clarity, debuggability, and extensibility over features.

---

## Why Pepper Terminal Exists

Most AI interfaces optimize for speed and breadth. Pepper Terminal optimizes for:

- Thoughtful, high-resolution conversation  
- Explicit uncertainty over confident guessing  
- A quiet, focused local environment  
- Future integration with structured memory systems  

Pepper Terminal is not intended to replace ChatGPT. It is intended to **complement it**, especially for local work, experimentation, and tooling.

---

## Current Features (v0.1)

- Local terminal interface (macOS tested)
- OpenAI API integration
- Conversation context retained during session
- Clean, readable output
- Minimal, understandable codebase

---

## Non-Goals (for now)

- Persistent memory across sessions
- Voice input and output
- Autonomous actions
- Background agents

These may be added later, deliberately.

---

## Requirements

- macOS (tested on Apple Silicon)
- Python 3.11 or newer
- An OpenAI API key with billing enabled

---

## Installation

1. Clone the repository  
2. Create and activate a virtual environment  
3. Install dependencies  
4. Create a `.env` file with your OpenAI API key  

Example `.env` file:


