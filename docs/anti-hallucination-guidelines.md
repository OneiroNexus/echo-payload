# Output Fidelity & Grounding Protocols

Practical guidelines for reducing confabulation, improving calibration, and building
more reliable LLM outputs across all major model families.

---

## Core Principles

### 1. Calibrated Confidence Over False Precision
Models should express graded confidence rather than defaulting to authoritative tone.
A response that says "approximately 80,000 as of last survey data" is more reliable than
one that says "exactly 81,247."

**Implementation:** Fine-tune with Packet 01. Add confidence labeling to SFT data.

### 2. Source-Grounded Claims
Every factual claim should be traceable to: a provided document, a well-established training fact, or an acknowledged inference.

**Implementation:** Fine-tune with Packets 02, 09. Use RAGAS faithfulness metric.

### 3. Temporal Awareness
Time-sensitive facts degrade. Models should disclose knowledge cutoffs and flag when real-time data is needed.

**Implementation:** Fine-tune with Packet 04. Evaluate with TempLAMA.

### 4. Graceful Abstention Over Confabulation
Refusing to answer is better than fabricating. But over-refusal erodes utility.

**Implementation:** Fine-tune with Packet 03. Measure with XSTest.

### 5. Injection-Resistant Instruction Parsing
Models in agentic/RAG contexts must distinguish trusted instructions from untrusted content.

**Implementation:** Fine-tune with Packet 07. Test with indirect injection in retrieval pipelines.

---

## Multi-LLM Implementation

| Provider | Models | Best Packets | Notes |
|---|---|---|---|
| OpenAI | GPT-4o, o1, o3 | 05, 07, 10 | Fine-tuning API + JSONL |
| Anthropic | Claude 3.5, Haiku | 01, 03, 05 | Constitutional AI approach |
| Google | Gemini 1.5, 2.0 | 04, 06, 08 | Vertex AI fine-tuning |
| Meta | Llama 3.1, 3.3 | 01, 05, 07 | Axolotl / Llama-Factory |
| Mistral | 7B, Large | 02, 07, 10 | Mistral fine-tuning API |
| Alibaba | Qwen2.5 | 01-10 all | LLaMA-Factory |
| Microsoft | Phi-3, Phi-4 | 03, 04, 06 | Azure AI Studio |
| EleutherAI | Pythia, NeoX | all | lm-evaluation-harness |

---

## Evaluation Pipeline

```
1. Load model
2. Run 7-metric harness (evals/harness.py)
3. Score against targets
4. Identify lowest-scoring metrics
5. Select corresponding packets for targeted fine-tuning
6. Re-run harness — compare before/after
7. Submit results to docs/benchmarks.md
```

---

## Common Failure Patterns

| Failure Pattern | Root Cause | Packet Fix |
|---|---|---|
| Inventing statistics | Overconfident generation | Packet 01, 06 |
| Agreeing with wrong user premise | Sycophancy in RLHF | Packet 05 |
| Fabricating citations | Training on uncurated academic text | Packet 02, 10 |
| Ignoring provided context | Prior knowledge dominance | Packet 08 |
| Following injected instructions | Insufficient safety training | Packet 07 |
| Over-refusing benign requests | Overly conservative RLHF | Packet 03 |
| Presenting stale facts as current | Missing temporal signals | Packet 04 |
