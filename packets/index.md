# Packet Index

| # | Name | File | Focus | Metric |
|---|---|---|---|---|
| 01 | Calibration & Confidence | [01-calibration-confidence.md](01-calibration-confidence.md) | ECE reduction, uncertainty labeling | ECE < 0.12 |
| 02 | Citation Faithfulness | [02-citation-faithfulness.md](02-citation-faithfulness.md) | Source grounding | Citation F1 > 0.88 |
| 03 | Abstention Training | [03-abstention-training.md](03-abstention-training.md) | "I don't know" behaviors | Over-refusal < 8% |
| 04 | Temporal Grounding | [04-temporal-grounding.md](04-temporal-grounding.md) | Cutoff awareness | Temporal Error < 8% |
| 05 | Anti-Sycophancy | [05-anti-sycophancy.md](05-anti-sycophancy.md) | Pushback on false premises | Sycophancy Rate < 10% |
| 06 | Numeric Precision | [06-numeric-precision.md](06-numeric-precision.md) | Number accuracy | Numeric Hallucination < 7% |
| 07 | Prompt Injection Resistance | [07-prompt-injection-resistance.md](07-prompt-injection-resistance.md) | Adversarial injection | Injection Resistance > 85% |
| 08 | RAG Context Grounding | [08-rag-context-grounding.md](08-rag-context-grounding.md) | Retrieval faithfulness | Faithfulness > 0.92 |
| 09 | Source Provenance | [09-source-provenance.md](09-source-provenance.md) | Attribution chains | Provenance Accuracy > 0.90 |
| 10 | Adversarial Robustness | [10-adversarial-robustness.md](10-adversarial-robustness.md) | Known attack patterns | Robustness > 0.85 |

## Workflow Mapping

```
Fine-tuning (DPO/ORPO) → Packets 01, 05, 06, 10
RAG pipeline testing    → Packets 02, 08, 09
Red-teaming / safety    → Packets 07, 10
Calibration training    → Packets 01, 03, 04
Context engineering     → Packets 02, 08
```
