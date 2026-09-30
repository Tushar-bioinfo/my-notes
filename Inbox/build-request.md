# Authorized request and context for Opus

You are the design and implementation orchestrator. The parent Codex is only your mediator: it gathers context, relays your specialist assignments, tracks work, executes local non-model checks, and shows the user progress. The user explicitly requested Claude CLI, claude-opus-5-5, effort high, to lead this work. Never substitute models.

## User request, preserved in substance

Build the user's own compact suite of benchmarks, independent of Artificial Analysis methods and scores, to test models available through their subscriptions. It should reveal actual suitability for their work, task-specific strengths, and possible weak transfer from public benchmark scores. AA can be an external comparison only. Track subscription costs, weekly/five-hour allowance consumption during tests, and execution time. Optimize strongly for low token/allowance use; the user expects to select only 1–3 reasoning settings for a comparison. Consider model committee design/judging if useful, but let Opus decide a sensible economical approach. Automate parts that need no model usage and inexpensive recurring comparisons/checkups. Cover scientific research first, browser work, automation, and the user's broader workflow. Surprise the user with a thoughtful, reasonable benchmark without major methodological holes.

There is already a self-contained HTML evaluation report in the parent project. Build a separate benchmark version inside this My-bench folder, with its own actual results and sections tailored to this suite. Inspect the parent directory for context. Do not modify the original AA report/data.

Required people/model sequence: Opus high leads; Grok 4.7 high critiques the design BEFORE implementation; all implementation specialists are gpt-6.1-sol at high or xhigh; Grok 4.6 high reviews implementation. Gemini 3.8 Flash high draws a flowchart of agents, assignments, work done, and progress. Parent relays these dispatches because the agent-delegate dispatcher prohibits nested delegation. Do not call a dispatcher or spawn your own agents: instead provide explicit assignments for parent execution.

Implementation, fixes, local checks, and a tiny reasonable pilot are authorized. Do not run a large multi-model benchmark sweep during construction; choose a minimal meaningful validation and make further comparisons user selectable. Do not install/upgrade tools, pay for APIs, perform large downloads, or send sensitive/unpublished scientific data. Use synthetic or public cases.

## Files to inspect selectively

- ../AGENTS.md; ../llm-eval/README.md
- ../llm-eval/docs/report.html (existing report, self-contained, offline; large: inspect relevant spans)
- ../llm-eval/scripts/report.py (existing report generator; inspect relevant spans)
- ../llm-eval/docs/benchmark-intake.md and benchmark-params.md (background only; new suite must have its own method)
- ../llm-eval/config/specialists.yaml, routes.yaml, abilities.yaml, and roles/*.md (existing user job profiles)
- ../llm-eval/data/models.json, data/current/compact.json, data/current/worker-brief.json (catalog and AA snapshot; inspect schemas/small slices, do not dump)
- /Users/tusharsingh/.codex/skills/agent-delegate/registry.json and scripts/delegate.py (actual configured model/CLI routes)
- /Users/tusharsingh/.agents/docs/planning.md before design; implementation.md before analysis-code edits; review.md or paper-review.md as appropriate for reviewers.
- User's personal AGENTS.md supplied in this conversation: scientific correctness > validity > reproducibility/provenance > evidence > calibrated claims > efficient compute > simple implementation. Preserve scientific data, never fabricate source access/results or usage values, distinguish experimental from analysis units, check leakage/confounding/pseudoreplication, and communicate briefly in everyday language.

The My-bench directory was initially empty and is not a Git repository. Parent's llm-eval already tracks 18 specialist roles and public benchmark proxies; README explicitly says biology, literature retrieval, teaching, and writing lack direct benchmark coverage. Existing HTML supports per-job picks, heatmap, weighting sliders, change tracking, provenance/caveats, and cost comparisons.

## Workflow history gathered this session (themes, no private raw data)

Recent available chat titles/summaries include:
- Compare Guide Noise; Control Guide Noise Analysis; CRISPR Project Basics; Explain CRISPR Screen Basics; Explain MAGeCK Advice.
- Explain Normalization Standardization; Visualize sequencing data scaling (10 data points across 4 sequencing samples).
- Drive Claude literature review: monitoring a looping literature/research process and refining problem lists.
- Gmail Organization and Cleanup; weekly safe cache cleanup; recurring reminders/automation.
- Find and draft a writing task: actual writing tasks and user style examples.
- Public health/tobacco control course summaries, leadership explanations, and concise L1/L2/L3 learning.

User identifies as a biologist/bioinformatician working in bioinformatics, spatial omics, computational pathology, and reproducible quantitative science. Those are direct self-described needs, not inferred project results. Recent history themes support CRISPR guide-control analysis, normalization, literature assessment, tutoring, writing, browser organization, and automation. Do not claim to have read private project data or complete history.

## Dispatch conventions

Exact routes from installed registry:
- Claude: claude-opus-5-5, high.
- Cursor: grok-4.7-high, high (unknown slugs pass through; verify actual availability, no fallback).
- Codex: gpt-6.1-sol, high or xhigh.
- Cursor: cursor-grok-4.6-high, high.
- Antigravity: gemini-3.8-flash-high, high.

Every delegate returns status, model, effort, session_id, response, duration_seconds; Claude may expose actual_model. Failure or model mismatch must be reported verbatim and work stopped. Continue the same Opus session across phases. Keep specialist ownership disjoint and warn workers they share the folder and must not revert others' edits.

## Your first phase

Inspect the existing context and design the suite. Write a concise but complete design to design.md, including what can/cannot be concluded, objective grading versus discretionary review, exposure/holdout rules, realistic allowance/cost observability, run modes and budget limits, and the report's views. Write a precise file/API ownership contract and specialist assignment list to assignments.json. Do not implement benchmark code yet: the required Grok 4.7 high design critique comes next. Provide concise mediator instructions including exact files to send to that reviewer. Avoid unnecessary questions: resolve routine choices yourself.
