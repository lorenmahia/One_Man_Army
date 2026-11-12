# Experiment Log

> Template. Research and planning support only; not legal, tax, investment or financial advice.

A log for small validation experiments. The core rule from the playbook: write the pass, adjust and fail thresholds, the segment, the denominator and the sample size BEFORE you look at any results, and date them. Small samples are fine for finding patterns but weak for measuring rates, so report counts with a 95% Wilson interval and let the whole interval, not the point estimate, decide. Use one entry per test.

## Hypothesis template

"We believe `[segment]` has `[problem]`. If we offer `[solution]` at `[price]`, then at least `[X of N]` will take `[specific action]` within `[time]`." Kill statement: "If fewer than `[Y of N]`, we will not build `[Z]`."

## Entry (copy per experiment)

```
Date written:        [YYYY-MM-DD]   (thresholds fixed before the test)
Hypothesis:          [ ... ]
Segment:             [who counts as qualified; define the denominator now]
Test type:           [interview / landing page / pre-order / paid pilot / ...]
Thresholds (written before the test):
  Pass (go):         [ ... ]
  Adjust:            [ ... ]
  Fail (stop):       [ ... ]
Sample size planned: [N]
Start / end dates:   [ ... ]
Cost:                [money] and [hours]
--- after the test ---
Raw counts:          [k of n]
95% interval:        [low% to high%]
Decision:            [go / adjust / stop]
What we learned:     [ ... ]
Next action:         [ ... ]
Challenged by:       [someone who reviewed the interpretation]
```

## Calling the test

- Go only if the whole interval clears the pass threshold; stop only if the upper end falls below the fail threshold.
- If the interval includes both pass and fail, extend the sample once, to a pre-set cap.
- Maximum two adjustment rounds before a forced decision.
- Do not drop outliers after the fact, and do not run until the number looks good.

Illustrative gate criteria from the playbook (Estimates; set your own): B2B SaaS or service - go at 3+ of 10 target buyers signing a paid pilot or LOI at the stated price, stop at 0 paid commitments from 15+ qualified prospects.

## Wilson 95% intervals for small counts (z = 1.96)

These values are from the playbook and were recomputed independently for this template; they match to one decimal place.

| Result | Observed rate | 95% interval |
|---|---|---|
| 0 of 20 | 0% | 0% to 16.1% (rule of three: 3/20 = 15%) |
| 2 of 10 | 20% | 5.7% to 51.0% |
| 4 of 40 | 10% | 4.0% to 23.1% |
| 3 of 50 | 6% | 2.1% to 16.2% |
| 5 of 100 | 5% | 2.2% to 11.2% |
| 10 of 100 | 10% | 5.5% to 17.4% |

Formula: centre = (p + z^2/(2n)) / (1 + z^2/n); half-width = z * sqrt(p(1-p)/n + z^2/(4n^2)) / (1 + z^2/n).

## Example entry (ILLUSTRATIVE, made-up scenario; interval from the table above)

```
Hypothesis:    Freelance designers lose billable hours to invoicing. If we offer
               an invoicing tool at 15 per month, at least 8 of 40 will pre-order
               within 14 days.
Thresholds:    Pass: interval lower bound above 10%. Fail: interval upper bound
               below 10%. Otherwise adjust or extend once.
Raw counts:    4 of 40
95% interval:  4.0% to 23.1%
Decision:      adjust (interval spans both pass and fail); extend to a pre-set cap
               of 100 once, with one change to the offer.
```

Reading it: 4 yes answers of 40 is not "10%"; it is consistent with about 4% to 23%.

Source playbook: [Validation and experiment design](../playbooks/01-validate/validation-and-experiment-design.md)
