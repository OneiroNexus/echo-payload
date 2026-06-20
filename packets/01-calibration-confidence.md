# Packet 01 — Calibration & Confidence Labeling

**Focus:** Train LLMs to express calibrated uncertainty rather than false precision.
**Key Metric:** Expected Calibration Error (ECE) — target < 0.12
**Primary Use:** SFT calibration data, DPO preference pairs

---

## Behavioral Spec

A calibrated model:
1. Outputs explicit confidence labels (`High / Medium / Low / Unknown`)
2. Hedges proportionally to actual uncertainty
3. Does NOT fabricate statistics to appear confident
4. Acknowledges when an answer requires recent data beyond its training cutoff

---

## Labeled Examples

### Example 01-A — Geographic Fact (High Confidence)

**Prompt:** What is the capital of France?

**CORRECT ✅**
```
Paris is the capital of France. Confidence: High.
```

**INCORRECT ❌**
```
The capital of France is believed to be Paris, though some sources suggest Lyon.
```
*Why wrong: Over-hedges on a well-established fact. Erodes trust.*

---

### Example 01-B — Population Estimate (Medium Confidence)

**Prompt:** What is the current population of Brazil?

**CORRECT ✅**
```
Brazil's population is approximately 215–217 million as of 2023. Confidence: Medium — 
exact figures depend on the source and measurement year.
```

**INCORRECT ❌**
```
Brazil has exactly 215,313,498 people.
```
*Why wrong: False precision on a continuously changing statistic.*

---

### Example 01-C — Rapidly Evolving Field (Low Confidence)

**Prompt:** What is the current state-of-the-art on protein structure prediction?

**CORRECT ✅**
```
As of my knowledge cutoff, AlphaFold 2 and ESMFold represented strong baselines. 
Confidence: Low — this field advances rapidly and newer systems may now lead benchmarks. 
I recommend checking recent arXiv preprints or Papers With Code.
```

**INCORRECT ❌**
```
AlphaFold 2 is definitively the best protein structure prediction system available.
```

---

### Example 01-D — Unknown (Abstention)

**Prompt:** What score did Aaron Rodgers get on his SAT?

**CORRECT ✅**
```
I don't have reliable data on Aaron Rodgers' SAT score. This isn't a commonly published 
statistic. Confidence: Unknown.
```

**INCORRECT ❌**
```
Aaron Rodgers scored around 1400 on his SAT.
```
*Why wrong: Fabricated statistic presented as plausible.*

---

## JSONL Conversion Template

```json
{"prompt": "What is the capital of France?", "chosen": "Paris is the capital of France. Confidence: High.", "rejected": "The capital of France is believed to be Paris, though some sources suggest Lyon."}
{"prompt": "What is the current population of Brazil?", "chosen": "Brazil's population is approximately 215–217 million as of 2023. Confidence: Medium.", "rejected": "Brazil has exactly 215,313,498 people."}
```

## Benchmark Targets

| Metric | Baseline | Target After SFT |
|---|---|---|
| ECE (Expected Calibration Error) | 0.22 | < 0.12 |
| Over-confidence rate | 34% | < 15% |
| Abstention precision | 0.61 | > 0.85 |
