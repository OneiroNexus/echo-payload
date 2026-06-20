# Repository Architecture & Flow

## System Overview

echo-payload is a **documentation + specification repository** — no model weights, no training infrastructure required. It provides structured data and methodologies that plug into any existing LLM workflow.

---

## Flow Architecture

### Flow A — Initial Deployment

```
Notion (Build Sheet)
        │
        ▼
  Canva Pro AI ────────────────────────────────────────┐
  (Social banner, hero image,                             │
   packet cards, flywheel diagram)                        │
        │                                                 │
        ▼                                                 ▼
  GitHub Repository ◄──────────────────────── Visual Assets
  (50+ files, topics, Discussions)
        │
        ▼
  Facebook Business
  (Launch announcement post)
```

### Flow B — Content Updates

```
Notion updated → Diff → Canva (changed assets) + GitHub (commit) → Facebook
```

### Flow C — Community Engagement

```
GitHub Event (issue/PR) → Canva (community card) → Facebook post
```

---

## Packet Processing Pipeline

```
Markdown Packet (.md)
        │
        ├─► convert_to_jsonl.py ─► .jsonl (DPO/ORPO training)
        ├─► convert_to_jsonl.py ─► .csv (spreadsheet analysis)
        ├─► evals/harness.py ─────► 7-metric eval report
        └─► RAG ingestion ────────► vector store
```

See [`docs/make-workflow.md`](make-workflow.md) for Make.com automation specs.
