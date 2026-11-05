---
name: discovery-learning
description: Design, teach and review AI-guided educational courses using brief narrative scenarios, meaningful choices, grounded explanations, and natural memory reinforcement. Use for interactive pedagogy, course architecture, low-friction learning, retrieval practice and concept-map-driven repetition; do not use as a source of domain facts.
license: Apache-2.0
metadata:
  version: "0.1.0"
  status: draft
---

# Discovery Learning

## Operating modes
Choose **DESIGN** for authoring or improving materials, **TEACH** for guiding a learner through a course, and **REVIEW** for auditing instruction. Do not pretend to be the final teaching assistant when asked to design the course.

Read [learning model](references/learning-model.md) in all modes. Also read [memory strategy](references/memory-strategy.md) and [interaction patterns](references/interaction-patterns.md) for DESIGN; [assessment](references/assessment.md) for TEACH; and [acceptance cases](tests/acceptance-cases.md) for REVIEW. Consult [research basis](references/research-basis.md) for the scope of scientific claims.

## Core boundaries
- The course's knowledge bank, not this skill, is the authority for subject facts. Keep `draft` and `verified` distinct. Mark fictitious people, calculations and assumptions.
- Domain safety, mandated practical competence checks and formal assessment always override the default non-blocking flow.
- Do not infer mastery from content exposure, silence or a single A/B answer.
- Preserve technical terminology and subject-specific instructions.
- No required proprietary APIs, interactive widgets, durable user memory, or timers.

## DESIGN
1. Inspect course instructions, objectives, module order, glossary, knowledge status, and safety rules.
2. Build a concept map with stable IDs, prerequisites, typical confusion pairs and later application points. See [concept map template](assets/concept-map-template.md).
3. Draft each module as scene → meaningful exploration/prediction → consequence → factual explanation → application → continuation. See [module template](assets/module-template.md).
4. Introduce purposeful *callbacks* where an earlier concept is naturally needed. Prefer brief recall before revealing the explanation; vary contexts. Do not force repetition quotas.
5. Use worked examples before independent calculations, show units, cash/noncash and assumptions.
6. Make A/B/continue text input an always-available fallback. Offer optional free-text depth, never require lengthy writing merely to progress.
7. Test branch-equivalence, factual boundaries, wrong answers, passive learners, memory callbacks, and cross-model portability.

## TEACH
1. Verify access to course material; follow the course's onboarding and ordering.
2. Present one short scene and one meaningful action at a time. Exploratory choices need not be graded.
3. Explain consequences from the verified or explicitly provisional subject material.
4. Offer natural recall when prior knowledge becomes relevant; distinguish recognizing an answer from explaining or transferring knowledge.
5. If the learner says 'continue', 'fortsätt', or 'don't know', give the key explanation and proceed unless mandatory safety assessment applies.
6. On a misconception, give a precise contrast and revisit it in a later relevant situation. Do not create an endless correction loop.
7. Never claim certification or lasting memory without appropriate evidence.

## REVIEW
Evaluate coverage of learning objectives, grounding, user friction, plausible branches, purposeful memory reuse, honest evidence of understanding, safe boundaries and text-only compatibility. Separate confirmed issues, design recommendations and completed fixes.

## References and templates
[Learning model](references/learning-model.md) · [Memory strategy](references/memory-strategy.md) · [Interaction patterns](references/interaction-patterns.md) · [Assessment](references/assessment.md) · [Research basis](references/research-basis.md) · [Course template](assets/course-template.md) · [Module template](assets/module-template.md) · [Concept map](assets/concept-map-template.md)
