# ADR 0001 – Independent course repositories and capability-aware design

status: proposed
date: 2026-11-05

## Context
Discovery Learning was initially scoped as a general teaching and course-design skill. The intended deployment is instead one subject course per GitHub repository. Each learner should be able to start from the *course URL* in a compatible AI service. Platforms evolve and do not expose uniform visual interaction tools.

## Decision
- Discovery Learning is a **development and review skill**, not an operational dependency of a learner-facing course.
- Each course repo contains all teaching instructions, subject knowledge, learning objectives, glossary, interactions, memory callbacks and testing required to run independently.
- At project initialization, review official documentation for selected AI platforms and store dated, evidence-labeled capability profiles in the course repo.
- At learner runtime, inspect only the actually exposed tools without delaying course onboarding.
- Choose pedagogical purpose before visual representation before implementation; always support a faithful text-only fallback.
- Keep course-specific safety rules and mandatory assessment gates authoritative.
- Update skill versions independently of course versions; course repository can record which design skill version informed its construction.

## Rejected alternatives
- Runtime import of central skill: unnecessary dependency and incompatible with URL-first portability.
- Static permanent platform capability claims: high maintenance and fast obsolescence.
- Mandatory rich widgets: excludes learners and services without the right UI.
- Skill as live teacher: confuses development governance with end-user instruction.

## Consequences
Better portability and auditability, but deliberate duplication of small teaching instructions into each course. Project-time capability discovery consumes research effort and cannot claim completeness without access. Multi-provider testing and factual validation remain necessary.
