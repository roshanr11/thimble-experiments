"""Run Bloom's scenario pipeline with output capped at 16k tokens (OpenRouter reserves credit for max_tokens)."""
import sys
import petri_bloom._understanding.understanding as u
import petri_bloom._ideation.ideation as i
from petri_bloom import run_scenarios

cap = lambda model: 16000  # noqa: E731
u._resolve_max_tokens = cap
i.resolve_max_tokens = cap
run_scenarios(sys.argv[1], scenarios_model=sys.argv[2], overwrite=True)
