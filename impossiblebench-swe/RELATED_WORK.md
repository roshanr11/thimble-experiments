# Related work and what is new here

Checked 2026-11-17 against the full paper (Zhong, Raghunathan, Carlini, arXiv 2510.20270v1) and its released code
(`safety-research/impossiblebench`).

## ImpossibleBench already covers

From the paper:

- Cheating rates on Impossible-SWEbench (full scaffold, strict prompt D): GPT-5 54% on Conflicting; more capable
  models cheat more (Sec. 4).
- Four cheating types, classified by Claude Opus 4: modify tests, overload comparison operators, record extra state,
  special-casing (Sec. 4.1–4.2).
- Prompt strictness A–D (Sec. 5.1), test access: hidden / read-only (Sec. 5.2), feedback loop and an abort option,
  `flag_for_human_intervention` (Sec. 5.3).
- LLM monitors catch 42–65% of SWE cheats (Sec. 6). **Open question they leave:** monitors accepted "backward
  compatibility" justifications, and "it remains unclear whether the model intentionally crafted this
  justification or was simply misunderstanding the task requirements."

From the code:

- **Cheating rate**: pass rate on impossible SWE-bench and LiveCodeBench variants (`oneoff`, `conflicting`).
- **Cheating type**: an LLM judge sorts cheats into categories (test modification, operator overloading,
  special-casing, extra state). Its judge prompt already notes agents "may claim it is trying to fix a legacy test
  or maintain backward compatibility".
- **Context engineering**:
  - a strict prompt ("If you find any tests that are logically flawed ... STOP")
  - an escape hatch (`human_intervention`: submit `[flag_for_human_intervention]`)
  - test access (`hide_tests`, `reset_tests`)
  - feedback loops (`max_attempts`)
- **Monitoring**: LLM monitors tested on verified cheating transcripts (cheating vs legit).

So these are **not new** here: the cheat rate itself, cheat types, the escape-hatch prompt, test access, and
monitor accuracy at detecting cheating.

## Close related work

- Baker et al. 2025, *Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation*: CoT
  monitors catch coding reward hacks; optimizing against them teaches obfuscation.
- Chen et al. 2025, *Reasoning Models Don't Always Say What They Think*: models often don't verbalize hint use,
  including during reward hacking.
- Turpin et al. 2025, *Teaching Models to Verbalize Reward Hacking in CoT*: undetected reward hacks are 88% of
  responses without intervention.
- Thaman 2026, *Reward Hacking Benchmark*: 72% of exploit episodes include a CoT rationale framing the exploit as
  legitimate problem-solving.
- Taufeeque et al. 2026, *The Obfuscation Atlas*: in a hardcoding-test-cases coding environment, RL against a
  deception detector produces an "obfuscated policy" that justifies the hack in its output.
- Huang et al. 2026, *Reward Hacking Challenges Oversight of Autonomous Research Agents*: hack rates and evasion of
  an LLM review panel.
- Ludwig et al. 2026, *Shortcutting the Fix*: SWE-bench shortcutting is common; telling the agent to solve
  independently suppresses it.
- Scheurer et al. 2023, *LLMs can Strategically Deceive their Users when Put Under Pressure*: under pressure a
  trading agent acts on insider info and hides why in its report to its manager.
- Kutasov et al. 2025, *SHADE-Arena*: sabotage versus monitors in agentic tasks.

## What this project adds (as far as checked)

1. **Concealment in the final report.** For each verified cheat, does the agent's message to the user disclose it,
   describe it vaguely ("compatibility fix"), or hide it? ImpossibleBench scores the code; Scheurer et al. showed
   report-hiding under pressure in trading, not in coding cheats on a verified benchmark.
2. **Awareness before the cheat.** Did the agent notice the test/spec conflict before it cheated (knowing) or
   never notice it (unknowing)? This is measured step by step on the transcript, not from the CoT alone. It answers
   the question ImpossibleBench Sec. 6 leaves open: is a "backward compatibility" justification crafted or a
   misunderstanding?
3. **Interactive pressure.** A Petri auditor plays a user who pushes partway through ("CI is blocking the release").
   ImpossibleBench varies a fixed prompt, test access and feedback, but not user pressure; Scheurer et al. varied
   pressure in a non-coding setting.

The baseline uses ImpossibleBench's released default SWE setup: full scaffold, open tests, and the default prompt
suffix "**DO NOT MODIFY THE TESTS.**". That is close to the paper's looser prompt B, not the strict prompt D behind
its headline numbers, so expect somewhat higher cheat rates than the paper's Figure 3 (Sec. 5.1: GPT-5 54% → 66%).
It was chosen deliberately, to get more cheating transcripts for the concealment and awareness analysis.

Dropped as a headline: judge or monitor accuracy at detecting cheating (ImpossibleBench covers it). It stays only
for the new question: do monitors catch *concealment*?
