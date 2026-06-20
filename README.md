<div align="center">

# ⟁ echo-payload

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/OneiroNexus/echo-payload?style=social)](https://github.com/OneiroNexus/echo-payload/stargazers)
[![Forks](https://img.shields.io/github/forks/OneiroNexus/echo-payload?style=social)](https://github.com/OneiroNexus/echo-payload/network/members)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![LLM Safety](https://img.shields.io/badge/focus-llm--safety-blue)](https://github.com/OneiroNexus/echo-payload)
[![Eval Harness](https://img.shields.io/badge/eval-7--metric--harness-orange)](docs/evaluation-harness.md)

**Practical payload for LLM hallucination mitigation, calibration training, and anti-over-refusal.**

10 labeled structured packets · 7-metric evaluation harness · JSONL-ready · Works with all major LLMs

[What this is](#what-this-is) · [Who it's for](#who-its-for) · [Quick Start](#quick-start) · [Packets](#the-10-packets) · [Benchmarks](#benchmarks) · [LLM Compatibility](#llm-compatibility) · [Contributing](#contributing)

</div>

---

## What This Is

A ready-to-use collection of **10 structured payload packets** with labeled correct/incorrect examples, a behavioral spec for calibrated answers, and a **7-metric evaluation harness**.

Designed for direct use in production LLM workflows:

- ✅ Fine-tuning and preference optimization (DPO, ORPO, SFT)
- ✅ RAG grounding and citation faithfulness testing
- ✅ Red-teaming and prompt injection resistance evaluation
- ✅ Calibration and abstention training
- ✅ Building custom safety evals
- ✅ Multi-LLM benchmarking (GPT-4o, Claude 3.5, Gemini 1.5, Llama 3, Mistral, Qwen, Phi-3)

All packets are in clean Markdown that converts directly to **JSONL, CSV, or Parquet** for training pipelines.

---

## Who It's For

| Audience | Use Case |
|---|---|
| LLM fine-tuning engineers | DPO/ORPO/SFT preference datasets from packets 01–06 |
| RAG & context engineering teams | Retrieval test sets from packets 02, 08, 09 |
| AI safety researchers | Red-teaming with packets 07, 10 |
| Eval practitioners | 7-metric harness for any model |
| Production teams | Drop-in improvement on hallucination rate & over-refusal |

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/OneiroNexus/echo-payload.git
cd echo-payload

# Run the evaluation harness on any model
python evals/harness.py --model gpt-4o --packets all

# Convert a packet to JSONL for fine-tuning
python scripts/convert_to_jsonl.py --packet packets/05-anti-sycophancy.md --output training.jsonl

# Run the doctor check
bash doctor.sh
```

---

## The 10 Packets

| # | Packet | Focus | Key Metric |
|---|---|---|---|
| 01 | [Calibration & Confidence](packets/01-calibration-confidence.md) | Confidence labeling, ECE reduction | Calibration Error |
| 02 | [Citation Faithfulness](packets/02-citation-faithfulness.md) | Source grounding, citation accuracy | Citation F1 |
| 03 | [Abstention Training](packets/03-abstention-training.md) | "I don't know" behaviors | Abstention Precision |
| 04 | [Temporal Grounding](packets/04-temporal-grounding.md) | Date-sensitive facts, cutoff awareness | Temporal Error Rate |
| 05 | [Anti-Sycophancy](packets/05-anti-sycophancy.md) | Pushback on false premises | Sycophancy Rate |
| 06 | [Numeric Precision](packets/06-numeric-precision.md) | Number accuracy, rounding, uncertainty | Numeric Hallucination % |
| 07 | [Prompt Injection Resistance](packets/07-prompt-injection-resistance.md) | Adversarial injection, system prompt leakage | Injection Resistance % |
| 08 | [RAG Context Grounding](packets/08-rag-context-grounding.md) | Context faithfulness, retrieval fidelity | Faithfulness Score |
| 09 | [Source Provenance](packets/09-source-provenance.md) | Source attribution, provenance chains | Provenance Accuracy |
| 10 | [Adversarial Robustness](packets/10-adversarial-robustness.md) | Known hallucination attacks, jailbreak probes | Robustness Score |

---

## Benchmarks

| Model | Hallucination Rate | Calibration Error | Over-Refusal Rate | Injection Resistance |
|---|---|---|---|---|
| Llama-3-8B-Instruct (base) | 17–22% | 0.19–0.25 | 21–28% | 55–65% |
| GPT-4o (base, no SFT) | 8–12% | 0.10–0.14 | 12–18% | 74–82% |
| Claude 3.5 Sonnet (base) | 7–11% | 0.08–0.12 | 10–15% | 80–88% |
| Llama-3-8B + echo-payload SFT | 9–12% | 0.11–0.15 | 12–17% | 78–85% |
| Mistral-7B + echo-payload SFT | 11–14% | 0.13–0.17 | 14–19% | 72–79% |

---

## LLM Compatibility

| Provider | Models | Integration |
|---|---|---|
| OpenAI | GPT-4o, GPT-4o-mini, o1, o3 | Axolotl, OpenAI fine-tuning API |
| Anthropic | Claude 3.5 Sonnet, Claude 3 Haiku | Constitutional AI + DPO |
| Google DeepMind | Gemini 1.5 Pro, Gemini 2.0 Flash | Vertex AI fine-tuning |
| Meta | Llama 3.1, Llama 3.3 | Llama-Factory, Axolotl |
| Mistral AI | Mistral 7B, Mistral Large | Mistral fine-tuning API |
| Alibaba | Qwen2.5-7B, Qwen2.5-72B | LLaMA-Factory |
| Microsoft | Phi-3, Phi-4 | Azure AI fine-tuning |
| EleutherAI | Pythia, GPT-NeoX | lm-evaluation-harness |

See [`docs/llm-compatibility.md`](docs/llm-compatibility.md) for per-model integration guides.

---

## Repository Structure

```
echo-payload/
├── packets/          # 10 structured payload packets (Markdown)
├── docs/             # Evaluation harness, benchmarks, architecture
├── evals/            # Python evaluation scripts
├── scripts/          # JSONL conversion, batch eval utilities
├── assets/           # Visual assets, diagrams, social cards
├── .github/          # Issue templates, PR templates, CI workflows
├── doctor.sh         # Repo health check
└── README.md
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Good first issues: [`good first issue`](https://github.com/OneiroNexus/echo-payload/labels/good%20first%20issue)

---

## License

MIT — see [LICENSE](LICENSE).

<div align="center">
<sub>Built by <a href="https://www.oneironexus.com">Oneiron Holdings LLC</a> · Part of the Antgall framework ecosystem</sub>
</div>