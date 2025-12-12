# Pepper Terminal — Project State

Last updated: 2025-12-12

## Purpose
Pepper Terminal is a minimal local terminal client that connects to the OpenAI API for calm, high-resolution conversation. It is designed to remain understandable, inspectable, and extensible over long time horizons.

## Current Status (v0.3)
Pepper Terminal is fully functional with persistent local memory and a long-term summary layer.

### Working
- Interactive terminal loop (`pepper.py`)
- OpenAI API chat completions
- Rich-rendered assistant output
- dotenv-based configuration
- Git + GitHub (SSH)
- Persistent local memory (JSONL, daily rotation)
- Cross-day recall (configurable window)
- Rolling long-term summary layer (`memory/summary.md`)
- Local command system (`:help`, `:where`, `:new`, `:clear`, `:summary`, `:summarize`)
- Optional auto-summary updates every N turns

### Known Constraints
- API billing required
- No vector search or semantic memory yet
- Summary updates incur an extra API call

## How to Run
1) `cd pepper-terminal`
2) `source venv/bin/activate`
3) `python pepper.py`

## Architecture (current)

### Entry Point
- `pepper.py`
  - system prompt
  - command handling
  - OpenAI interaction
  - memory logging
  - summary management

### Memory Layers
1) **Daily Logs**
   - Stored as `memory/YYYY-MM-DD.jsonl`
   - Append-only
   - Logs both user and assistant messages

2) **Rolling Recall**
   - On startup, loads last `RECALL_MESSAGES`
   - Spans up to `RECALL_DAYS` most recent log files

3) **Long-Term Summary**
   - Stored at `memory/summary.md`
   - Injected into context as a system message
   - Updated manually (`:summarize`) or automatically (`AUTO_SUMMARIZE_EVERY`)

### Config / Safety
- `.env` (not committed): API key
- `.gitignore`: excludes memory, venv, secrets

## Operational Notes
- Commands are handled before conversation logic and are not logged.
- Summaries are designed to be stable, factual, and token-efficient.
- Memory files are private and never committed.

## Roadmap (near-term)
- `:stats` command
- Session-end auto-summary
- Memory export (Markdown)
- Optional SQLite backend

