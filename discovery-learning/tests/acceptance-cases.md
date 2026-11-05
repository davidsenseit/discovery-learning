# Discovery Learning acceptance cases

status: draft

| ID | Input / condition | Expected behavior |
|---|---|---|
| T01 | User starts a course | Short relevant scene without a prerequisite examination |
| T02 | User selects A | Correct grounded exploration; no grade for a preference |
| T03 | User selects B | Different emphasis, same mandatory learning content |
| T04 | User says 'continue' | Brief explanation and progression |
| T05 | User answers a prediction incorrectly | Targeted correction, not an endless retry loop |
| T06 | User refuses free text | Alternative low-friction participation |
| T07 | User asks to go deeper | Optional explanation without deleting core coverage |
| T08 | Subject material inaccessible | Explicit access limitation; no fabricated facts |
| T09 | Hypothetical economic values | Clear labels, correct units and separate calculation check |
| T10 | Model without widgets | A/B/continue works through ordinary chat |
| T11 | Single correct A/B choice | No unsupported mastery or retention claim |
| T12 | Earlier concept naturally reappears | Optional retrieval before explanation |
| T13 | Callback has no subject relevance | Omit it; no forced repetition quota |
| T14 | Concept confusion persists | Later contrasting scenario and accurate feedback |
| T15 | Same information appears in different contexts | Terminology and core meaning remain stable |
| T16 | Safety-critical training | Mandatory competence gates override optionality |
| T17 | Course spans one sitting | No claim that this equals multi-day spacing |
| T18 | Two AI providers run same modules | Coverage, source status and fallback comparable |

## Execution evidence
This file defines **planned tests**. It does not certify that the tests were run. Log environment, model, date, exact input, observed output, deviations and remediation.
