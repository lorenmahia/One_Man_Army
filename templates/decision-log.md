# Decision Log

> Template. Research and planning support only; not legal, tax, investment or financial advice.

A lightweight decision record for pricing, channels, tools, hires and legal structure. The playbook builds on Michael Nygard's 2011 architecture-decision-record idea (Title, Status, Context, Decision, Consequences) and adds the rejected alternatives that the common critique says it omits. At the review date, compare expected vs actual; this builds calibration. Link entries from the weekly review.

## Entry template (copy per decision)

```
ID:               D-[NNN]
Date:             [YYYY-MM-DD]
Title:            [short decision]
Type:             [one-way (hard to reverse) / two-way (easy to reverse)]
Status:           [proposed / accepted / superseded by D-NNN / reversed]
Context:          [what is happening, constraints, evidence]
Options considered:
  A. [option] - [pros / cons]
  B. [option] - [pros / cons]
  C. [do nothing] - [pros / cons]
Decision:         [chosen option and why]
Expected outcome: [what should happen, and the metric that shows it]
Review date:      [YYYY-MM-DD]
Actual outcome:   [fill at review]
Lesson:           [what to do differently]
```

Moving a kill criterion or a signed threshold is itself a decision: log it here, with the reason.

## Index table

| ID | Date | Decision | Type | Status | Review date | Outcome |
|---|---|---|---|---|---|---|
| D-001 | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

## Example entry (ILLUSTRATIVE, made-up)

```
ID:               D-007
Date:             2026-03-02
Title:            Raise monthly price from 29 to 39
Type:             two-way
Status:           accepted
Context:          Eight of ten interviewed customers said price was not a concern;
                  support load is rising.
Options considered:
  A. Raise to 39 for new customers only - lower churn risk, slower revenue
  B. Raise to 39 for everyone - faster revenue, churn risk
  C. Keep 29 - no risk, no learning
Decision:         A, because it is reversible and tests price sensitivity.
Expected outcome: New-customer conversion stays within 2 points of current rate.
Review date:      2026-04-30
Actual outcome:   [fill at review]
Lesson:           [fill at review]
```

Source playbook: [Operating cadences, OKRs and reporting](../playbooks/06-operate/operating-cadences-okrs-and-reporting.md)
