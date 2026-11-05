# Platform discovery and visual-learning acceptance tests

status: draft
execution_status: not_run

| ID | Trigger | Required result |
|---|---|---|
| P01 | New course project | Identify target platforms; check official docs if browsing available; date claims |
| P02 | No browsing available | Mark docs unverified/stale, do not imply an online check |
| P03 | Provider docs describe a feature | Mark documented, not tested |
| P04 | Feature exposed in current runtime | Mark available, test a simple interaction before relying on it |
| P05 | UI widget absent | Use plain text A/B/continue without loss of core objectives |
| P06 | UI fails midway | Fall back to explanation and report failure without inventing state |
| P07 | Course starts from URL | No long capability research before welcome and first scenario |
| P08 | Tool supports charts but no sliders | Do not promise sliders; choose supported representation |
| P09 | Diagram generated | Validate labels, relationships, alt description and factual accuracy |
| P10 | Hypothetical variable model | Verify formula, units, bounds, and two worked text states |
| P11 | Visual is merely decorative | Omit without loss of pedagogical content |
| P12 | Cross-platform use | Same required learning insights with and without rich UI |
| P13 | Capability snapshot ages | Recheck at next project or material capability change |
| P14 | New course repository | Contains a self-contained runtime and dated platform profile |
| P15 | Runtime attempts to import skill repository | Reject dependency and replace with bundled instructions |
| P16 | Learner's domain requires competency gate | Preserve gate despite generic non-blocking design |

Document actual runs with platform, client, plan when known, date, prompt, outputs, pass/fail and limitations. These are **test designs** until executed.
