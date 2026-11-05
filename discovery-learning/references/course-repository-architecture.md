# Course repository contract

status: draft

## Separation of responsibilities
- **Discovery Learning repository:** cross-domain methods for DESIGN/REVIEW, versioned templates, platform capability investigation and quality tests.
- **Course repository (one per course):** complete learner-facing material: README, AGENTS, onboarding, ordered objectives and modules, knowledge, glossary, exercises, interaction and visual specifications, status, safety rules and validation artifacts.
- **Learner AI runtime:** consumes only course repository content. No assumption that it can load or invoke this skill.

## Initial course development
Check whether the user has already created a target GitHub repo. Inspect its contents and local instructions before recommending or writing modifications. For an empty repo, create a self-contained course scaffold using the templates. Never create an implicit dependency on this skill's remote paths. A course can record `discovery_learning_version: 0.2.0` as provenance without using it as a runtime import.

## Suggested structure (adapt to existing repo)
```text
README.md
AGENTS.md
ROADMAP.md
pedagogy/{ONBOARDING,FRAMEWORK,ASSESSMENT,INTERACTION}.md
knowledge/
discovery/
glossary/
exercises/
quality/{platform-capabilities,acceptance-tests}.md
docs/decisions/
```

## Capability documentation
At project initiation, inspect official vendor documentation for target platforms (e.g. ChatGPT, Claude), then document:
- inspection date, source URL and publication/update date when provided
- environment variants (web, mobile, API, enterprise, developer tools), plan/permission limits, and what remains unknown
- supported visual/interactive representations and requirements
- what was tested in a real session vs merely documented
- portable fallback behavior
Repeat when a new project begins, a major platform change is detected, capability assumptions materially affect the design or a test fails.

## Independence test
In a fresh compatible AI conversation with access only to the course repository:
- A pasted course URL leads to onboarding and the first scenario, or an honest access limitation.
- No link to this skill must be fetched to teach.
- Every core module functions with text-only A/B/continue when rich controls are absent.
- Concepts, numeric examples, safety checks and status remain consistent across target platforms.
- A participant choosing 'continue' is not blocked except where an actual safety/assessment requirement exists.

## GitHub workflow
Develop on a topic branch, create an issue for scoped work and a PR with checks, record decisions, and merge only after owner approval. Do not represent unrun tests as passed.
