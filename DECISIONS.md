# Decisions

## 2025-12-12 — Keep single-file architecture for v0.x
We keep `pepper.py` as a single file to preserve inspectability and reduce friction.
Refactor into modules only when persistent memory + commands land.

## 2025-12-12 — Introduce a rolling summary layer

### Decision
Add a long-term summary stored in `memory/summary.md`, injected into the conversation as a system message and periodically updated via the model.

### Reasoning
- Full chat history does not scale with token limits
- JSONL logs are durable but inefficient for recall
- A summary provides compressed continuity across sessions and days
- Keeping it in plain text preserves inspectability and control

### Trade-offs
- Requires an additional API call when updating
- Summary quality depends on prompt discipline
- Summary may lag behind reality if not refreshed

### Mitigations
- Manual `:summarize` command
- Optional auto-summary every N turns
- Summary size capped to control token usage

---

## 2025-12-12 — Layered memory architecture

### Decision
Use three distinct memory layers:
1) Daily append-only logs
2) Recent rolling recall window
3) Long-term summary

### Reasoning
- Separates durability from context efficiency
- Makes each layer simple and replaceable
- Mirrors human memory patterns (episodic + semantic)

### Future Direction
- Replace or augment logs with SQLite
- Add semantic indexing on top of summaries
