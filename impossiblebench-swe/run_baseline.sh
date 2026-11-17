#!/usr/bin/env bash
# Baseline: ImpossibleBench's default SWE setup (full tool scaffold, strict prompt, open tests) on the 25
# quality-checked conflicting tasks, one run per model.
set -euo pipefail
cd "$(dirname "$0")"
export OPENROUTER_API_KEY="${OPENROUTER_API_KEY:-sk-or-dummy}"   # the session proxy injects the real key
IDS=$(cat valid.txt)
.venv/bin/inspect eval ib_tasks.py@ib_agent \
  -T split=conflicting -T ids="$IDS" -T max_attempts=5 -T message_limit=60 \
  --model openrouter/openai/gpt-5.6-luna,openrouter/deepseek/deepseek-v4.1-flash,openrouter/anthropic/claude-haiku-5.5,openrouter/google/gemini-3.8-flash \
  -M strict_tools=false --max-samples 6 --max-sandboxes 12 \
  --log-dir logs/baseline --log-format json --display plain
