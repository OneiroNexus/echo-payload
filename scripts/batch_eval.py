#!/usr/bin/env python3
"""
Batch evaluation across multiple models.
Generates comparison table for docs/benchmarks.md.

Usage:
    python scripts/batch_eval.py --models gpt-4o claude-3.5-sonnet llama3-70b
"""

import argparse
from pathlib import Path
from datetime import datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", nargs="+", required=True)
    parser.add_argument("--output-dir", default="results/")
    args = parser.parse_args()

    print("\n## Comparison Table (for docs/benchmarks.md)\n")
    headers = ["Model", "Hallucination", "ECE", "Over-Refusal", "Sycophancy",
               "Injection Res.", "Citation F1", "Temporal Err", "Date"]
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join(["---"] * len(headers)) + "|")
    for model in args.models:
        row = [model] + ["run eval"] * 7 + [datetime.now().strftime("%Y-%m")]
        print("| " + " | ".join(row) + " |")
    print("\nRun evals/harness.py for each model to get actual numbers.")


if __name__ == "__main__":
    main()
