# Discovery Learning

An open Agent Skill for **developing and reviewing independent, AI-guided courses**, combining narrative discovery, meaningful memory reinforcement and purposeful visual learning.

**Version:** 0.2.0 (proposed, draft). **License:** Apache-2.0.

## Architecture
One GitHub repository per course. Discovery Learning acts as a **development and quality-assurance skill**, not as a dependency that learners must install.

1. Use this skill in a development AI to inspect or design a course repository.
2. Discover target AI platforms and their current capabilities, documenting source dates and runtime limitations.
3. Design objective-linked explanations, scenarios, memory callbacks, visuals and text-only equivalents.
4. Generate a **self-contained course repository**: onboarding, AGENTS instructions, pedagogical guidance, knowledge, modules, glossary and quality tests.
5. Test and propose changes via issues, branches and pull requests. Do not merge without the owner's approval.
6. Learners paste the **course repository URL**, not the skill URL, into a compatible AI service. The course must work without this skill or any proprietary UI.

See [the skill](discovery-learning/SKILL.md), [course repository architecture](discovery-learning/references/course-repository-architecture.md), [visual strategy](discovery-learning/references/visual-learning.md), and [platform verification](discovery-learning/references/capability-discovery.md).

## Principle
**Learning goal → pedagogical activity → suitable representation → available tool → text fallback.**

A documented capability is not proof it is enabled. Project-time verification and lightweight runtime checks are distinct. A web check requires actual browsing access; otherwise mark claims as unverified/stale.

## Development state
The skill's instructional design has not been empirically validated. All example projects, capability profiles and tests are draft until checked. Safety-critical courses may require actual competency gates and supervised practice.
