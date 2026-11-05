# Dynamic platform capability discovery

status: draft
last_document_review: 2026-11-05

## Why this exists
Platform features change, and availability depends on product, model, account, application, enabled settings, deployment and runtime. This document describes a repeatable **verification process**, not a permanent capability list.

## Two checkpoints
**Project start (DESIGN):** Identify course delivery targets; investigate current official documentation for each selected platform and fill a dated capability profile in the course repository. Perform actual tests where access is available. Do not claim tests were executed if only documents were read.

**Course start (runtime):** Briefly inspect tools actually exposed in the learner's environment. Start the course without slowing onboarding for broad web research. Use supported enhancements; if capabilities are absent or unknown, use text-only alternatives.

## Evidence status
- `documented`: clearly supported by a current authoritative provider source, but not tested here
- `available`: a relevant tool/interface is visibly exposed to the running assistant
- `tested`: a specific scenario completed successfully in the target environment
- `blocked`: a specific capability demonstrably unavailable or failed in tested environment
- `unknown`: not checked, no web access, conflicting evidence, or insufficient evidence
A capability can have multiple labels, e.g. documented+blocked for a plan restriction. Never convert documented into tested automatically.

## Project-start procedure
1. Record target platforms and variants: ChatGPT web/mobile/API/Work, Claude web/Desktop/API/Claude Code or other environments relevant to intended learners. Do not assume they share a capability.
2. Check available official release notes, product documentation and tool schemas if web access exists. Give explicit inspection date and source URLs; capture publication/update dates.
3. Ask which modalities are essential: ordinary chat, images, live charts, clickable selections, interactive simulations, file/data analysis, audio or vision.
4. Distinguish documented support from the current session's exposed tools. Test representative interactive activities when possible and record exact environment.
5. For each pedagogical action, record the best supported representation and a text-only fallback.
6. Save a dated snapshot in the **course repository**, not as a permanent assumption in the skill.
7. Recheck at each new course project, whenever a relevant feature changes or expires, before relying on a capability flagged stale, or after test failure. Never assert an automatic calendar-based refresh unless an actual scheduler is configured.

## Failure behavior
If browsing unavailable, mark documentation freshness `unknown` or `stale`, use provided platform files only as dated historical examples, and continue with conservative design. If a tool is not exposed, do not invent it. If a renderer fails, present the equivalent text representation and record the deviation.

## Sources for initial examples (not permanent truth)
- ChatGPT interactive charts and data analysis: https://help.openai.com/en/articles/9213685-extracting-insights-with-chatgpt-data-analysis
- ChatGPT capabilities overview: https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview
- Claude Artifacts: https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them

Do not infer cross-plan/tool availability from general articles.
