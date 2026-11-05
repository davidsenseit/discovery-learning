# ChatGPT capability reference – historical snapshot, not guarantee

status: draft
checked_at: 2026-11-05
evidence: documented
runtime_tested: false

## Source links
- https://help.openai.com/en/articles/9213685-extracting-insights-with-chatgpt-data-analysis
- https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview

## Documented categories
- Generate or analyze images and charts in supported environments.
- Data analysis can create static charts and, for bar/line/pie/scatter, often interactive charts.
- Data analysis can generate tables; some views are interactive.
- Available features vary by account, plan, model, device, settings and tool permissions.

## Use constraints
Do **not** assume a ChatGPT conversation can execute arbitrary custom JS UI or expose slider controls just because it can display charts. Check exact tools in the runtime. Some facilities depend on uploads, data analysis and other enabled product capabilities. Always keep A/B/continue and text examples as fallback.

## Revalidation
At a new course project, confirm the current documents, date, relevant account/deployment and available test environment. Record results in course repository.
