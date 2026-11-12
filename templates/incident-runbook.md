# Incident Runbook (One Page)

> Template. Research and planning support only; not legal, tax, investment or financial advice.

A one-page incident response runbook for a one-person company. CISA asks small businesses to have a written, reviewed plan and to practise it. Print it or store a copy somewhere you can reach if your laptop is dead, and fill in the contacts now, not during an incident. Note the time you became "aware": notification clocks may run from it.

Owner: `[you]`   Last reviewed: `[YYYY-MM-DD]`   Backup contact with emergency access: `[name / phone]`

## Steps

| # | Step | Do | Record |
|---|---|---|---|
| 1 | Detect | Note time, source (alert, customer report, vendor notice, scanner) and what you saw. Start a timestamped log file now and write everything down. | Time aware: `[ ]` |
| 2 | Contain | Revoke sessions and tokens for affected accounts; disable the leaked key or compromised service account; isolate the affected host or deployment; pause CI if the pipeline is suspected. Prefer reversible steps; preserve logs and snapshots before wiping anything. | `[ ]` |
| 3 | Rotate | From a clean device, change credentials starting with email, registrar, source host, cloud root and payments, then the exposed secret and everything reachable by it. Re-issue hardware-key-based sessions. Revoke or rotate first; deleting a commit does not make a secret safe. | `[ ]` |
| 4 | Assess | What data and which customers were reachable? Pull provider audit logs for the exposure window. Decide whether personal data was accessed, altered, lost or disclosed. Record facts, effects and remedial action. | `[ ]` |
| 5 | Notify | Decide who must be told after confirming with counsel: regulators, customers, affected vendors, your cyber insurer, investors. | `[ ]` |
| 6 | Learn | Within two weeks, write a blameless note: timeline, root cause, what worked, control changes, owner and date for each. Update this runbook and the vendor/asset inventory. | `[ ]` |

## Notification clocks (EXAMPLES ONLY)

These vary by jurisdiction and facts. Confirm with counsel; the shortest applicable clock sets your pace. Figures below are from secondary summaries in the playbook, not verified statutes.

| Regime | Example clock | Applies if |
|---|---|---|
| GDPR / UK GDPR | Authority within 72 hours of becoming aware where feasible, unless unlikely to risk individuals; individuals without undue delay if high risk | You process personal data in scope |
| US states | Vary; some list 30 days, others "without unreasonable delay"; verify the statute | Residents of that state affected |
| HIPAA | Individual notice no later than 60 calendar days after discovery | Covered entity or business associate only |
| EU NIS2 | Early warning 24 hours, fuller report 72 hours, final report about a month later | In scope only |
| India CERT-In | 6 hours for specified incidents | Specified incident types |
| Customer contracts / DPAs | May set their own, shorter clocks; no typical value verified | Check each contract |

## Communication messages (write in plain words)

- Customer notice: what happened and when; what data was and was not involved; what you have done; what the customer should do; a named contact and next-update time. No speculation, no blame.
- Regulator notice: facts known so far, categories and approximate numbers, likely consequences, measures taken, contact; more to follow if phased. Have counsel review.
- Vendor notice: which credentials or integrations may be affected, what you are rotating, what you need from them.
- Investor update: short and factual; impact, status, cost estimate, next steps.

## Contacts to fill in now

Counsel `[ ]`   Insurer `[ ]`   Hosting / cloud support `[ ]`   Payments provider `[ ]`   Registrar `[ ]`

## Example log lines (ILLUSTRATIVE, made-up)

- 14:05 Scanner alert: API key found in public repo. Time aware.
- 14:12 Key revoked at provider. 14:20 New key issued; deploy updated.
- 14:40 Provider logs reviewed for the exposure window; `[no / some]` use by unknown IPs.

Source playbook: [Security and secrets baseline for a one-person startup](../playbooks/03-build/security-and-secrets-baseline.md)
