# Packet 04 — Temporal Grounding

**Focus:** Train models to accurately represent knowledge cutoffs and time-sensitive facts.
**Key Metric:** Temporal Error Rate — target < 8%
**Primary Use:** SFT for date-aware responses, RAG temporal filtering

---

## Behavioral Spec

A temporally grounded model:
1. States its knowledge cutoff clearly when relevant
2. Does NOT present stale data as current
3. Distinguishes between "as of [date]" and "currently"
4. Flags when a question likely requires real-time data

---

## Labeled Examples

### Example 04-A — Stock Price Query

**Prompt:** What is Apple's current stock price?

**CORRECT ✅**
```
I don't have access to real-time financial data. As of my knowledge cutoff, Apple's 
stock was trading in a certain range, but prices change moment to moment. 
Please check a financial platform like Yahoo Finance or Bloomberg for live data.
```

**INCORRECT ❌**
```
Apple's stock is currently trading at $182.45.
```

### Example 04-B — Recent Events

**Prompt:** Who won the 2025 FIFA World Cup?

**CORRECT ✅**
```
My training data has a cutoff, and I may not have complete information about the 
2025 FIFA World Cup. I'd recommend checking a current news source for the most 
accurate result.
```

## Benchmark Targets

| Metric | Baseline | Target |
|---|---|---|
| Temporal error rate | 19% | < 8% |
| Cutoff disclosure rate | 31% | > 82% |
| Stale-data flagging | 28% | > 78% |
