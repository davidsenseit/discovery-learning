---
name: discovery-learning
description: Develop and review self-contained AI-guided courses in their own GitHub repositories, using discovery-led pedagogy, memory reinforcement, visual learning and verification of target AI-platform capabilities. Use when planning, building, adapting or auditing an educational repository.
license: Apache-2.0
metadata:
  version: "0.2.0"
  status: draft
---

# Discovery Learning — course development skill

## Mission and role boundaries
This skill develops, maintains and quality-reviews **course-specific GitHub repositories**. It is not the finished teaching agent, and learners need not install this skill. Each course repository must carry its own sufficient instructions, content, interaction fallbacks and tests.

The course's primary knowledge and domain-specific safety requirements override generic teaching defaults. Do not treat this skill as a source of subject facts.

## Before proposing changes
1. Inspect the target repository, current branch, instructions, modules, quality controls, issues and existing decisions. If a new course has no repository, have one created before GitHub development; do not silently substitute another repository.
2. Establish audience, objectives, source hierarchy, terminology, assessment requirements and whether hands-on competency is compulsory.
3. Perform a **project-time target-platform review** using [capability discovery](references/capability-discovery.md): verify relevant ChatGPT, Claude and other selected platforms using current official documentation where possible; distinguish documented, available, tested, blocked and unknown. Record dates and links.
4. Select the simplest pedagogically adequate representations with [visual learning](references/visual-learning.md) and [memory strategy](references/memory-strategy.md).
5. Propose an implementation plan and scope; then develop changes via isolated branch and PR, without merging until approval.

## DESIGN — author a course in its own repository
Read [learning model](references/learning-model.md), [interaction patterns](references/interaction-patterns.md), [memory strategy](references/memory-strategy.md), [course repository architecture](references/course-repository-architecture.md), and applicable [templates](assets/course-template.md).

- Build stable learning objectives and a concept map with prerequisites, confusion pairs and later natural application points.
- Plan a narrative sequence: scene → meaningful exploration → grounded consequence and explanation → application → continuation.
- Insert optional retrieval opportunities when earlier knowledge becomes necessary. Distinguish recognition from recall and transfer.
- For each objective, decide whether text, a flowchart, illustration, graph, animated sequence or interactive model materially improves understanding. Include meaningful accessibility descriptions and verified data.
- Specify **platform-neutral interaction intent** and **at least one text-only equivalent**. Keep all mandatory learning insights and assessments reachable without widgets.
- Generate or update the course's own AGENTS, onboarding, pedagogical files, knowledge, activities, glossary, fact status, tests, and capability snapshot. Record the skill version used.

## REVIEW — quality and portability
Check alignment of objectives, content, visuals, activities, answers and callbacks; inspect risk of cognitive overload, false understanding, hallucinated images or model-dependent controls. Run [acceptance tests](tests/acceptance-cases.md) and [platform tests](tests/platform-capabilities.md), reporting **executed** separately from **planned**. Document fact checks and numerical verification independently.

## Course runtime design (what the skill exports, not an installation requirement)
The standalone course should give a short welcome and start its first module if material is available. Use low-friction A/B/continue interaction, factual explanations, selective graphics and natural callbacks. Runtime may check currently exposed features without a lengthy browsing detour. Never assert support merely from a platform name. Honor safety-specific practical assessment gates; never claim mastery from silence or one guess.

## Restrictions
- Never invent current tool support, learning outcomes, financial results or safety rules.
- Do not require cross-repository access during course delivery.
- Never require permanent personal memory, timers, proprietary APIs or interactive UI to complete the core course.
- Mark draft vs verified; time-stamp mutable platform data and factual numbers.
- An attempted documentation lookup without web access does not count as completed verification.

## Reference entrypoints
[Course architecture](references/course-repository-architecture.md) · [Learning model](references/learning-model.md) · [Memory strategy](references/memory-strategy.md) · [Visual learning](references/visual-learning.md) · [Capability discovery](references/capability-discovery.md) · [Interaction patterns](references/interaction-patterns.md) · [Assessment](references/assessment.md) · [Research](references/research-basis.md) · [Course template](assets/course-template.md) · [Module template](assets/module-template.md) · [Concept map template](assets/concept-map-template.md) · [Platform tests](tests/platform-capabilities.md)
