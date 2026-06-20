# Contributing to echo-payload

Thank you for your interest in contributing! echo-payload improves with every new packet, benchmark result, and integration guide.

---

## Ways to Contribute

### 1. Submit Benchmark Results
Run the eval harness on your model and submit results via PR to `docs/benchmarks.md`.
This is the **highest-impact contribution** — community benchmarks make this repo useful.

### 2. Improve Existing Packets
Found a better CORRECT/INCORRECT example? Spotted an error? Open a PR with your improvement.
Follow the packet format in `packets/01-calibration-confidence.md` as your template.

### 3. Add a New Packet
If you've identified a hallucination pattern not covered by packets 01–10, propose a new packet.
Open an issue first to discuss scope and prevent duplication.

### 4. Integration Guides
Add a new LLM or framework to `docs/llm-compatibility.md`.

### 5. Good First Issues
Look for issues labeled [`good first issue`](https://github.com/OneiroNexus/echo-payload/labels/good%20first%20issue) for lower-effort starting points.

---

## PR Guidelines

1. **One change per PR** — benchmark results, packet improvement, doc update. Keep it focused.
2. **Follow the format** — new packets must include: Behavioral Spec, Labeled Examples (with why), JSONL template, Benchmark Targets.
3. **No pseudocode** — all script examples must be runnable.
4. **Cite sources** — any benchmark numbers must reference a published methodology.

---

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Be kind, be precise, be useful.
