#!/usr/bin/env bash
# Pressure: the baseline plus a release-deadline line from the user in the first message and in every failure
# feedback (see PRESSURE in ib_tasks.py), on the same 25 tasks and 4 models.
set -euo pipefail
cd "$(dirname "$0")"
export OPENROUTER_API_KEY="${OPENROUTER_API_KEY:-sk-or-dummy}"   # the session proxy injects the real key
IDS=$(cat valid.txt)
.venv/bin/inspect eval ib_tasks.py@ib_pressure \
  -T split=conflicting -T ids="$IDS" -T max_attempts=5 -T message_limit=60 \
  --model openrouter/openai/gpt-5.6-luna,openrouter/deepseek/deepseek-v4.1-flash,openrouter/anthropic/claude-haiku-5.5,openrouter/google/gemini-3.8-flash \
  -M strict_tools=false --max-samples 4 --max-sandboxes 8 \
  --log-dir logs/pressure --log-format json --display plain
