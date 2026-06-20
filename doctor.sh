#!/usr/bin/env bash
# echo-payload doctor.sh — Repo health check

PASS=0
FAIL=0
WARN=0

check() {
  local label="$1"
  local condition="$2"
  if eval "$condition" 2>/dev/null; then
    echo "  ✅ $label"
    PASS=$((PASS+1))
  else
    echo "  ❌ $label"
    FAIL=$((FAIL+1))
  fi
}

warn_check() {
  local label="$1"
  local condition="$2"
  if eval "$condition" 2>/dev/null; then
    echo "  ✅ $label"
    PASS=$((PASS+1))
  else
    echo "  ⚠️  $label (optional)"
    WARN=$((WARN+1))
  fi
}

echo ""
echo "🔍 echo-payload — Repo Health Check"
echo "======================================"

echo ""
echo "📂 Core Files"
check "README.md exists"          "[ -f README.md ]"
check "LICENSE exists"            "[ -f LICENSE ]"
check "CONTRIBUTING.md exists"    "[ -f CONTRIBUTING.md ]"
check "CHANGELOG.md exists"       "[ -f CHANGELOG.md ]"

echo ""
echo "📦 Packets (10 required)"
for i in 01 02 03 04 05 06 07 08 09 10; do
  check "Packet $i exists" "ls packets/${i}-*.md"
done

echo ""
echo "📄 Docs"
check "evaluation-harness.md"     "[ -f docs/evaluation-harness.md ]"
check "benchmarks.md"             "[ -f docs/benchmarks.md ]"
check "architecture.md"           "[ -f docs/architecture.md ]"
check "llm-compatibility.md"      "[ -f docs/llm-compatibility.md ]"

echo ""
echo "⚙️  Scripts & Evals"
check "evals/harness.py"          "[ -f evals/harness.py ]"
check "evals/metrics.py"          "[ -f evals/metrics.py ]"
check "scripts/convert_to_jsonl.py" "[ -f scripts/convert_to_jsonl.py ]"

echo ""
echo "💙 GitHub Config"
check ".github/workflows/ci.yml"  "[ -f .github/workflows/ci.yml ]"
warn_check "assets/ has content"  "[ -d assets ]"

echo ""
echo "======================================"
echo "  ✅ Passed: $PASS"
echo "  ❌ Failed: $FAIL"
echo "  ⚠️  Warnings: $WARN"

if [ "$FAIL" -eq 0 ]; then
  echo ""
  echo "  🎉 Repo is healthy and ready!"
  exit 0
else
  echo ""
  echo "  ⚠️  Fix $FAIL failing checks before deploying."
  exit 1
fi
