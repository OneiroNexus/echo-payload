# LLM Compatibility Guide

echo-payload is model-agnostic and has been designed for use with all major LLM families.

---

## OpenAI — GPT-4o, o1, o3

**Fine-tuning path:** OpenAI Fine-tuning API

```bash
openai api fine_tuning.jobs.create -t training.jsonl --model gpt-4o-mini-2024-07-18
```

**Best packets:** 05 (Anti-Sycophancy), 07 (Injection Resistance), 10 (Adversarial)

---

## Anthropic — Claude 3.5 Sonnet, Claude 3 Haiku

**Approach:** Constitutional AI prompting

```python
system_prompt = """
Express confidence as: High / Medium / Low / Unknown
Cite sources explicitly when making factual claims
Correct false premises politely but firmly
Do not change correct answers under user pressure
"""
```

**Best packets:** 01 (Calibration), 03 (Abstention), 05 (Anti-Sycophancy)

---

## Google DeepMind — Gemini 1.5 Pro, Gemini 2.0 Flash

**Fine-tuning path:** Vertex AI supervised tuning

```python
from google.cloud import aiplatform
dataset = aiplatform.TextDataset.create(display_name="echo-payload-training", gcs_source="gs://your-bucket/training.jsonl")
```

**Best packets:** 04 (Temporal), 06 (Numeric), 08 (RAG)

---

## Meta — Llama 3.1, Llama 3.3

**Fine-tuning path:** Axolotl (recommended) or Llama-Factory

```yaml
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
datasets:
  - path: training.jsonl
    type: alpaca
rl: dpo
```

**Best packets:** 01, 05, 07 — highest relative improvement

---

## Mistral — Mistral 7B, Mistral Large

```python
from mistralai import Mistral
client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
with open("training.jsonl", "rb") as f:
    upload = client.files.upload(file=("training.jsonl", f))
job = client.fine_tuning.jobs.create(model="open-mistral-7b", training_files=[upload.id])
```

---

## Alibaba — Qwen2.5 (7B, 14B, 72B)

```bash
llamafactory-cli train --model_name_or_path Qwen/Qwen2.5-7B-Instruct --dataset echo_payload_dpo --stage dpo
```

---

## Microsoft — Phi-3, Phi-4

**Fine-tuning path:** Azure AI Studio or local Axolotl

---

## EleutherAI — Pythia, GPT-NeoX

```bash
lm_eval --model hf --model_args pretrained=EleutherAI/pythia-6.9b --tasks truthfulqa_mc
```

---

## Universal JSONL Format

```json
{"prompt": "...", "chosen": "...", "rejected": "..."}
```

```bash
python scripts/convert_to_jsonl.py --packet packets/05-anti-sycophancy.md
```
