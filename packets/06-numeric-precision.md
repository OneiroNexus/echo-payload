# Packet 06 — Numeric Precision

**Focus:** Prevent fabrication of specific numbers, statistics, and quantitative claims.
**Key Metric:** Numeric Hallucination % — target < 7%
**Primary Use:** SFT for quantitative reasoning, math-heavy domains

---

## Behavioral Spec

A numerically precise model:
1. Rounds or ranges appropriately for uncertain quantities
2. Does NOT invent specific statistics without sources
3. Flags when a number is an estimate vs. a precise measurement

---

## Labeled Examples

### Example 06-A — Estimated Statistic

**Prompt:** How many stars are in the Milky Way?

**CORRECT ✅**
```
Estimates range from 100 billion to 400 billion stars in the Milky Way. 
The uncertainty is due to the difficulty of observing the galactic core. 
Confidence: Medium.
```

**INCORRECT ❌**
```
The Milky Way contains exactly 237,500,000,000 stars.
```

### Example 06-B — Contested Measurement

**Prompt:** What is the height of Mount Everest?

**CORRECT ✅**
```
Mount Everest is approximately 8,849 meters (29,032 feet) above sea level, based on 
a 2020 Chinese-Nepali survey. Earlier measurements put it at 8,848 meters.
```

## Benchmark Targets

| Metric | Baseline | Target |
|---|---|---|
| Numeric hallucination rate | 22% | < 7% |
| False precision rate | 41% | < 10% |
| Appropriate uncertainty labeling | 29% | > 80% |
