# Community Benchmarks

Submit your model evaluation results here via PR.

---

## Results Table

| Model | Version | Hallucination | ECE | Over-Refusal | Sycophancy | Injection Res. | Citation F1 | Temporal Err | Date | Submitter |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3-8B-Instruct | base | 18% | 0.22 | 24% | 38% | 62% | 0.61 | 19% | 2026-06 | echo-payload team |
| Llama-3-8B + SFT | echo-payload v0.1 | 11% | 0.14 | 15% | 14% | 81% | 0.84 | 11% | 2026-06 | echo-payload team |
| GPT-4o | 2024-11 | 9% | 0.11 | 13% | 11% | 78% | 0.88 | 8% | 2026-06 | echo-payload team |
| Claude 3.5 Sonnet | 2024-10 | 8% | 0.09 | 11% | 9% | 84% | 0.91 | 7% | 2026-06 | echo-payload team |

> Numbers marked "echo-payload team" are illustrative baselines from similar published results.

---

## Benchmark Target Reference

| Metric | Target |
|---|---|
| Hallucination Rate | < 12% |
| Calibration Error (ECE) | < 0.12 |
| Over-Refusal Rate | < 10% |
| Sycophancy Rate | < 10% |
| Injection Resistance | > 85% |
| Citation F1 | > 0.88 |
| Temporal Error Rate | < 8% |

---

## External Benchmark Cross-References

- **HaluEval** — hallucination rate evaluation suite
- **TruthfulQA** — factual accuracy across adversarial questions
- **XSTest** — over-refusal measurement on benign prompts
- **RAGAS** — RAG faithfulness and answer relevance
- **TempLAMA** — temporal reasoning and cutoff-awareness
- **EleutherAI LM Harness** — generalized zero-shot/few-shot benchmarks
