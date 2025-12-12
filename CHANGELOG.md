# Changelog

All notable changes to Pepper Terminal will be documented here.

## [Unreleased]
- TBD

## [0.3.0] - 2025-12-12
### Added
- Rolling long-term summary layer (`memory/summary.md`)
- Summary injected into context as system memory
- Manual summary commands (`:summary`, `:summarize`)
- Optional automatic summary refresh (`AUTO_SUMMARIZE_EVERY`)
- Cross-day recall across daily memory logs
- Daily JSONL log rotation (`memory/YYYY-MM-DD.jsonl`)

### Changed
- Memory system now uses layered recall (summary + recent logs)
- Timestamp handling updated to timezone-aware UTC

### Notes
- Summary updates make an additional API call
- Summary is intentionally concise and capped in size

## [0.1.0] - 2025-12-12
### Added
- Initial terminal client (`pepper.py`) using OpenAI API
- Rich Markdown rendering for assistant replies
- dotenv-based local configuration (`.env` ignored by git)
- Git + GitHub setup (SSH auth)

### Notes
- Requires OpenAI API billing enabled (ChatGPT Plus does not include API quota)

