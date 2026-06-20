#!/usr/bin/env python3
"""
Convert echo-payload Markdown packets to JSONL training format.

Usage:
    python scripts/convert_to_jsonl.py --packet packets/05-anti-sycophancy.md
    python scripts/convert_to_jsonl.py --packet all --format dpo
    python scripts/convert_to_jsonl.py --packet all --format sft --output sft.jsonl
"""

import argparse
import json
import re
from pathlib import Path


def extract_examples(packet_text):
    pattern = re.compile(
        r"###\s+Example\s+[\w-]+.*?\n"
        r"\*\*Prompt:\*\*\s*(.*?)\n"
        r".*?"
        r"\*\*CORRECT.*?\*\*\s*\n```\n(.*?)```"
        r".*?"
        r"\*\*INCORRECT.*?\*\*\s*\n```\n(.*?)```",
        re.DOTALL
    )
    for match in pattern.finditer(packet_text):
        prompt, chosen, rejected = match.group(1).strip(), match.group(2).strip(), match.group(3).strip()
        if prompt and chosen and rejected:
            yield {"prompt": prompt, "chosen": chosen, "rejected": rejected}


def convert_packet(packet_path, format_type="dpo"):
    text = packet_path.read_text()
    examples = list(extract_examples(text))
    if format_type == "sft":
        return [{"instruction": e["prompt"], "output": e["chosen"]} for e in examples]
    elif format_type == "alpaca":
        return [{"instruction": e["prompt"], "input": "", "output": e["chosen"]} for e in examples]
    return examples  # dpo default


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", required=True)
    parser.add_argument("--format", default="dpo", choices=["dpo", "sft", "alpaca"])
    parser.add_argument("--output", default="training.jsonl")
    args = parser.parse_args()

    packets_dir = Path(__file__).parent.parent / "packets"
    packet_files = sorted(packets_dir.glob("[0-9][0-9]-*.md")) if args.packet == "all" else [Path(args.packet)]

    all_examples = []
    for pf in packet_files:
        examples = convert_packet(pf, args.format)
        all_examples.extend(examples)
        print(f"  {len(examples)} examples from {pf.name}")

    with open(args.output, "w") as f:
        for ex in all_examples:
            f.write(json.dumps(ex) + "\n")

    print(f"\n✅ {len(all_examples)} examples written to {args.output}")


if __name__ == "__main__":
    main()
