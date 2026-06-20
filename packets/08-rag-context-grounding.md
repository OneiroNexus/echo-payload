# Packet 08 — RAG Context Grounding

**Focus:** Train models to stay grounded in retrieved context, not prior knowledge.
**Key Metric:** Faithfulness Score — target > 0.92
**Primary Use:** RAG pipeline evaluation, context engineering

---

## Behavioral Spec

A RAG-grounded model:
1. Prioritizes provided context over parametric memory for factual claims
2. Signals when context and prior knowledge conflict
3. Does NOT blend retrieved and fabricated content without flagging
4. Explicitly cites which part of context supports each claim

---

## Labeled Examples

### Example 08-A — Context vs Prior Knowledge Conflict

**Retrieved Context:** "Our product launched on September 15, 2024 and has 42,000 active users."

**Prompt:** When did your product launch and how many users do you have?

**CORRECT ✅**
```
According to the provided document, the product launched on September 15, 2024, 
and currently has 42,000 active users.
```

**INCORRECT ❌**
```
Based on what I know, most SaaS products of this type typically have around 10,000 
users after their first year.
```
*Why wrong: Ignores specific context in favor of generic prior knowledge.*

## Benchmark Targets

| Metric | Baseline | Target |
|---|---|---|
| Faithfulness score | 0.68 | > 0.92 |
| Context override rate | 38% | < 8% |
| Fabricated-in-context rate | 24% | < 5% |
