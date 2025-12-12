# Pepper Terminal — Project State

Last updated: 2025-12-12

## Purpose
Pepper Terminal is a minimal local terminal client that connects to the OpenAI API for calm, high-resolution conversation, designed to remain understandable and extensible.

## Current Status (v0.1)
- Working: terminal loop, dotenv loading, OpenAI chat call, rich rendering, persistent memory logs
- Known constraints: API billing required; no persistent memory; no commands/modes

- Persistent memory logs rotate daily under memory/YYYY-MM-DD.jsonl.
- Startup recall loads last RECALL_MESSAGES messages across RECALL_DAYS daily logs.

## How to Run
1) `cd pepper-terminal`
2) `source venv/bin/activate`
3) `python pepper.py`

## Architecture (today)
### Entry point
- `pepper.py`: single-file app containing:
  - system prompt
  - in-session message history
  - OpenAI call
  - terminal I/O formatting

### Config
- `.env` (not committed): `OPENAI_API_KEY=...`
- `.gitignore`: excludes `.env`, `venv/`, caches

## Operational Notes
- If `.env` isn’t loading, run from repo root or load dotenv with an explicit path.
- If API returns `insufficient_quota`, enable API billing.

## Roadmap (next)
- requirements.txt
- graceful error handling + user-friendly messages
- persistent memory (JSON or SQLite)
- command prefixes (e.g., `:help`, `:save`, `:note`)

