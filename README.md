# Discovery Learning

An open, provider-independent Agent Skill for designing, reviewing, and delivering narrative, discovery-based learning with natural memory reinforcement.

**Version:** 0.1.0 — **Status:** draft. Inspired by the Södra learning-system architecture, but contains no Södra-specific knowledge.

## What it does
Guides a learner through short realistic situations, meaningful choices, clear consequences and explanations, followed by natural re-use of previously introduced concepts. It reduces mandatory writing without making unsupported claims of mastery. It also supports course-design and quality-review workflows.

## Get started
See [discovery-learning/SKILL.md](discovery-learning/SKILL.md). Install the `discovery-learning/` folder as an Agent Skill in a compatible AI environment; alternatively load the instruction and reference files directly in a compatible assistant. The Skill format cannot guarantee automatic activation from a repository URL in every AI service.

The subject-specific course supplies its own knowledge bank, glossary, objectives, factual status, assessment obligations and safety rules. This skill does not replace them. For a URL-first course, bundle the relevant pedagogical instructions in the course repository so the course remains self-contained.

## Contents
- `discovery-learning/SKILL.md` — entrypoint and DESIGN/TEACH/REVIEW workflows
- `discovery-learning/references/` — pedagogy, memory, interaction, assessment, research limitations
- `discovery-learning/assets/` — course, module and concept-map templates
- `discovery-learning/tests/` — model portability/quality test cases and offline structural validator

## Scope and evidence
The skill applies retrieval practice, meaningful callbacks, contextual variation, worked examples and formative feedback, but its particular blend is **not empirically validated**. In safety-critical or credentialed training, domain-required competency demonstration takes priority over the default non-blocking progression. Never equate exposure with learning.

## Development
Use issues for scoped improvements, branches and pull requests for changes; verify structure, links, scenarios, factual boundaries and multi-model behavior before a release. Only merge after repository-owner approval.

License: Apache-2.0 (see [LICENSE](LICENSE)).
