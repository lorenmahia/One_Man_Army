# Templates

> Template index. Research and planning support only; not legal, tax, investment or financial advice.

Copy-and-fill starting points distilled from the playbooks. They are sketches to adapt, not finished or audited artefacts: the playbooks carry the evidence, sources, dates and caveats, so read the linked playbook before relying on a template. Worked examples inside templates use made-up numbers and are labelled as illustrative. The CI workflow files have not been run, and their commit SHAs must be looked up and verified by you.

| Template | Purpose | Stage | Source playbook |
|---|---|---|---|
| [pitch-deck-outline.md](pitch-deck-outline.md) | 12-slide solo-founder deck order with question, evidence and fields per slide | Raise | [Pitch deck and data room](../playbooks/05-raise/pitch-deck-and-data-room.md) |
| [data-room-checklist.md](data-room-checklist.md) | Folder structure and diligence checklist by stage with a status column | Raise | [Pitch deck and data room](../playbooks/05-raise/pitch-deck-and-data-room.md) |
| [investor-target-list.md](investor-target-list.md) | Scored 30-60 name investor list from public sources, plus pipeline stages | Raise | [Investor landscape and approach](../playbooks/05-raise/investor-landscape-and-approach.md) |
| [okr-sheet.md](okr-sheet.md) | Quarterly objectives and key results with baseline, target, score, confidence | Operate | [Operating cadences, OKRs and reporting](../playbooks/06-operate/operating-cadences-okrs-and-reporting.md) |
| [weekly-business-review.md](weekly-business-review.md) | 30-45 minute weekly review with a 5-10 metric scorecard | Operate | [Operating cadences, OKRs and reporting](../playbooks/06-operate/operating-cadences-okrs-and-reporting.md) |
| [investor-update.md](investor-update.md) | Monthly update structure plus a bad-month variant | Operate | [Operating cadences, OKRs and reporting](../playbooks/06-operate/operating-cadences-okrs-and-reporting.md) |
| [risk-register.md](risk-register.md) | Risk table with owner, review date, kill criteria and key-person row | Operate | [Operating cadences, OKRs and reporting](../playbooks/06-operate/operating-cadences-okrs-and-reporting.md) |
| [decision-log.md](decision-log.md) | Lightweight decision record with expected outcome and review date | Operate | [Operating cadences, OKRs and reporting](../playbooks/06-operate/operating-cadences-okrs-and-reporting.md) |
| [experiment-log.md](experiment-log.md) | Pre-registered thresholds, result with Wilson interval, go / adjust / stop | Validate | [Validation and experiment design](../playbooks/01-validate/validation-and-experiment-design.md) |
| [incident-runbook.md](incident-runbook.md) | One-page runbook: detect, contain, rotate, assess, notify, learn | Build | [Security and secrets baseline](../playbooks/03-build/security-and-secrets-baseline.md) |
| [minimal-security-policies.md](minimal-security-policies.md) | Seven short policy outlines to adapt (access, secrets, device, backup, incident, vendor, AI/agent) | Build | [Security and secrets baseline](../playbooks/03-build/security-and-secrets-baseline.md) |
| [ci/github-actions-ci.yml](ci/github-actions-ci.yml) | Minimal CI workflow sketch: read-only permissions, SHA-pinned actions, concurrency | Build | [CI/CD and release pipeline](../playbooks/03-build/cicd-and-release-pipeline.md) |
| [ci/deploy-oidc.yml](ci/deploy-oidc.yml) | Tag-triggered deploy sketch using OIDC, environment-scoped, `id-token: write` on the deploy job only | Build | [CI/CD and release pipeline](../playbooks/03-build/cicd-and-release-pipeline.md) |

## Notes

- Replace every `[ ... ]` placeholder; delete sections you will not use.
- Do not paste real customer, investor or personal data into a shared copy.
- Have a qualified professional confirm legal, tax, security-notification and financing items for your jurisdiction.
