# Discovery Learning course-development acceptance cases

status: draft
execution_status: not_run

| ID | Input / condition | Expected behavior |
|---|---|---|
| T01 | New target course repository | Inspect current files, instructions and branch before editing |
| T02 | Empty target repository | Generate self-contained runtime scaffolding, not a skill dependency |
| T03 | Learner sends only course URL | Short welcome and first module, or honest access limitation |
| T04 | Learner selects A | Grounded exploration and no score for preference |
| T05 | Learner selects B | Different emphasis, same mandatory learning insights |
| T06 | Learner says continue | Brief explanation and progress, unless mandatory assessment gate |
| T07 | Learner prediction wrong | Precise correction without compulsory repeated attempts |
| T08 | Learner declines writing | Low-friction option and nonblocking fallback |
| T09 | No visual tool available | Same required understanding through text/structured table |
| T10 | Visual interaction available | Used only where materially useful; not automatic decoration |
| T11 | Concept naturally returns | Recall opportunity and new application, not verbatim repetition |
| T12 | Correct A/B guess | Never described as proven mastery |
| T13 | Same course in two models | Equivalent core content and relevant caveats |
| T14 | Safety-critical course | Mandatory required competence and supervision not waived |
| T15 | Hypothetical calculations | Separate numerical check, units, assumptions and correct labels |
| T16 | Capability knowledge stale | Revalidate at project start or mark evidence unavailable |
| T17 | Platform marketing page lists widgets | Feature documented; not silently marked tested |
| T18 | Course developer proposes merge | PR and test evidence; actual merge only with owner approval |

## Evaluating the generated course
Keep target platform and model, exact sample input, observed result, human judgment, date and evidence links. Do not claim execution before tests have actually run. Evaluate educational retention and completion independently; interactive features alone do not prove improved learning.
