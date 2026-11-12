# Operating Cadences, OKRs and Reporting for a One-Person Company

> Last verified: 2026-11-11. Research and planning support only; not legal, tax, investment or financial advice.

## Summary

- **Fact:** Large-company management systems (OKRs, EOS, Scaling Up, Amazon's weekly business review, stage-gate) are documented almost entirely in practitioner books, vendor sites and consultancy material. We found no independent, rigorous evidence that any of them improves outcomes. Treat them as menus of rituals, not proven treatments.
- **Inference:** The parts that transfer to a team of one are small: a few written priorities per quarter, a weekly look at input metrics, a monthly written report, and written decisions. Alignment, cascading and facilitation machinery is theatre when there is nobody to align.
- **Fact:** Investor-update guidance converges on metrics first, specific asks, short recap, and bad news early with a plan. The update is also a forcing function for the founder even with no investors.
- **Inference:** A solo founder's real extra risks are key-person risk and sunk-cost drift. A risk register, a continuity note and pre-agreed kill criteria (go / adjust / stop) address both cheaply.
- **Inference:** Automate collection and reminders (digests, dashboard refresh, deadline sync). Keep judgment calls (what to cut, whom to tell, whether to stop) with the human.

## 1. What big companies do that matters, and what is theatre

**Evidence quality (read first).** **Fact:** The searches for this playbook returned no peer-reviewed effectiveness study of OKRs or EOS. OKR failure-rate claims come from vendors and consultancies, for example the [OKR Institute](https://okrinstitute.org/why-okrs-fail/) (self-reported, own client base, updated May 2026) and [Profit.co](https://www.profit.co/blog/okr-university/why-most-enterprise-okr-programs-fail-in-year-two/) (undisclosed method). *EOS Worldwide* publishes a "top 5%" claim with no data or method on its [Traction page](https://www.eosworldwide.com/traction-component) (accessed 2026-11-11). Stage-gate authors themselves note a [lack of hard evidence](https://eprints.soton.ac.uk/468604/2/PROMETHEUS_38_2_Baxter_et_al.pdf) on what governance works best (search snippet only; paper not opened). Goal-setting research (Locke and Latham) is a separate academic literature we did not review; do not assume it validates any specific OKR product.

**Per published accounts:**

- **OKRs.** **Fact (practitioner/promotional source):** Andy Grove built the method at Intel from Drucker's management by objectives, and John Doerr took it to Google in 1999, per [What Matters](https://www.whatmatters.com/stories/the-origin-story) (a site selling Doerr's book and course; the Intel growth figures there are unverified). Google's published guide, summarised in a search snippet of [re:Work](https://rework.withgoogle.com/en/guides/set-goals-with-okrs) (page itself could not be fetched), says scoring is 0 to 1, about 0.6 to 0.7 is a healthy result, and OKRs are not employee evaluations or a shared to-do list. Date of guide not confirmed.
- **EOS / Traction.** **Fact:** Rocks are 3 to 7 priorities per person/company reset every 90 days, a weekly scorecard, and a weekly 90-minute Level 10 meeting with a 60-minute issue-solving segment, per the vendor [EOS Worldwide](https://www.eosworldwide.com/traction-component). Critics call it rigid and one-size-fits-all; adopters pay implementers ([ACE article](https://www.acecma.org/about/news/is-eos-the-answer-or-the-leadership-flavor-of-the-month-5312), search snippet only).
- **Scaling Up / Rockefeller Habits.** **Fact:** Verne Harnish's habits cluster around priorities, data and meeting rhythm; summaries disagree on wording and no source we opened listed all ten. Verify against the [Scaling Up coaches page](https://coaches.scalingup.com/blog/blog-post-title-one-lpc9d-ewsb7-k3ryp-jz5xl-ddfh3) (search snippet only) or the book.
- **Amazon WBR.** **Fact (secondary):** Per [Commoncog](https://commoncog.com/the-amazon-weekly-business-review/) (published 2024-07-02, updated 2026-06-14, based on Colin Bryar's account), the WBR asks what customers experienced, how the business did, and whether it is on track. It is exception-driven, uses trailing-6-week plus 12-month charts, separates controllable input metrics from output metrics, and bans strategy debate in the meeting. Amazon reportedly reviews about 400 to 500 metrics at company level; the author's own firm uses 47.
- **Working backwards / decisions.** **Fact:** Bezos's 2016 letter, as quoted in [secondary coverage](https://chiefexecutive.net/how-amazon-does-it-decision-making-inside-the-worlds-most-daring-digital-company/) (snippet only), separates reversible "Type 2" decisions to make fast from near-irreversible "Type 1" decisions, and suggests deciding at roughly 70% of the information you wish you had.
- **Stage-gate.** **Fact:** Cooper's stage-gate uses fixed review points with go/kill decisions. Cooper himself argues it is [not rigid or linear](https://eprints.soton.ac.uk/468604/2/PROMETHEUS_38_2_Baxter_et_al.pdf) (snippet); a [2026 PDMA piece](https://community.pdma.org/knowledgehub/bok/product-innovation-process/new-product-governance-in-a-time-compressed-world) (snippet) suggests go/kill decision quality may be near its practical limit.

| System | Core useful idea | Theatre risk | Evidence quality | Fit for a team of one |
|---|---|---|---|---|
| OKRs | Few ambitious outcomes, scored honestly | Cascades, alignment, scores tied to pay | Practitioner and vendor; no rigorous trials found | High if cut to 1 to 3 objectives per quarter |
| EOS / Traction | 90-day Rocks, weekly scorecard, fixed agenda | Meeting ritual for a team; paid implementer | Vendor and anecdote; unsupported "top 5%" claim | Medium: take Rocks plus scorecard, drop L10 meeting and team parts |
| Scaling Up habits | Priorities, data, rhythm checklist | Team-alignment habits | Practitioner/book | Low to medium: use as a checklist only |
| Amazon WBR | Weekly input metrics, exception review, causal metric tree | 400+ metric decks; Finance-run facilitation | Memoir and secondary accounts | High in miniature (5 to 10 metrics, 20 minutes) |
| Working backwards / Type 1-2 | Write the outcome first; fast on reversible calls | Long narrative docs for small decisions | Memoir and letters | High: one-page decision record |
| Stage-gate | Pre-agreed go/kill criteria | Heavy gating bureaucracy | Author-promoted; acknowledged evidence gap | High as a light go-adjust-stop gate (section 6) |

**So what for a solo founder:** Borrow the primitives (quarterly priorities, weekly input metrics, fixed kill criteria) and skip the machinery built for coordinating people.

## 2. OKRs for a solo founder

**How to write them.** **Fact:** Objectives say what you want to accomplish; key results are numeric and gradable (per the re:Work summary above). **Inference for one person:**

1. One to three objectives per quarter, two to four key results each. More than about nine total KRs is a to-do list.
2. Objective: a qualitative outcome a customer or the business would notice ("Prove that freelance designers will pay for X"). Not a project ("Build onboarding").
3. Key result: a measurable outcome with a baseline and target ("5 paying customers from 0"; "week-4 retention 25% from unknown"). Where you lack a baseline, make "establish the baseline" the first KR.
4. Separate committed KRs (expect 1.0) from stretch KRs (expect about 0.7). Label each. Google's 0.6 to 0.7 guidance is for stretch goals ([re:Work snippet](https://rework.withgoogle.com/en/guides/set-goals-with-okrs)).
5. Cap WIP: tasks live in a separate list; OKRs are not a task list.

**Common failure modes** (sources: vendor/practitioner lists at [OKR Institute](https://okrinstitute.org/why-okrs-fail/) and [Profit.co](https://www.profit.co/blog/okr-university/why-most-enterprise-okr-programs-fail-in-year-two/), 2026; low evidence quality):

- Objectives written as projects; key results that measure activity (posts published) not outcomes (signups from posts).
- No baseline, so scores are guesses.
- Sandbagging when scores matter to someone else. **Inference:** for a solo founder the equivalent is flattering yourself; fix with a written scoring rule agreed before the quarter.
- Set and forget: goals never reviewed between planning sessions.

**Avoiding vanity metrics.** **Inference:** A metric is vanity if you cannot name a decision it would change. Prefer paying customers, retained users, revenue and cash over downloads, pageviews and followers (the [Sacks/Ruby metrics essay](https://sacks.substack.com/p/the-saas-metrics-that-matter), 2021, notes engagement ratios like DAU/MAU are only meaningful for paid, active seats).

**Illustrative example sets (not benchmarks; adapt numbers to your market):**

| Stage | Objective | Key results |
|---|---|---|
| Pre-revenue (illustrative) | O1: Confirm that a specific buyer will pay to solve problem X | KR1: 20 problem interviews completed (from 0). KR2: 3 written pre-orders or paid pilots at the target price. KR3: top-3 stated pain points documented and ranked |
| Pre-revenue (illustrative) | O2: Ship a usable first version | KR1: 10 users complete the core task unaided. KR2: median time-to-first-value under 10 minutes (baseline measured in week 2) |
| Revenue stage (illustrative) | O1: Make the product stick | KR1: month-2 logo retention from 70% to 80%. KR2: 60% of new users reach the activation event within 7 days (from 45%). KR3: reduce top churn reason (to be identified in week 1) cases by half |
| Revenue stage (illustrative) | O2: Grow efficiently | KR1: MRR from 4k to 6k. KR2: CAC payback under 12 months on the best channel. KR3: runway never below 9 months |

**Scoring cadence.** **Inference:** Glance at progress weekly (in the weekly review), score formally at quarter end in 30 minutes: score 0 to 1, write one sentence on why, and decide continue / modify / drop for each. Do not link scores to anything punitive, including self-judgment of worth.

**So what for a solo founder:** Two objectives, five numeric KRs, a baseline for each, and an honest end-of-quarter score are enough.

## 3. The operating rhythm

**Fact:** Fixed cadence is the common thread across EOS (weekly/quarterly/annual), Scaling Up (daily/weekly/monthly/quarterly/annual meeting rhythm, per summaries) and Amazon's weekly WBR. **Inference:** time boxes below are starting points, not researched optima.

| Ritual | Cadence | Time box | Output |
|---|---|---|---|
| Daily plan | Daily | 10 min | Top 1 to 3 outcomes; one "customer-facing" item |
| Daily close | Daily | 5 min | Log blockers and what was learned |
| Weekly business review (WBR) | Weekly | 30 to 45 min | Updated scorecard, 1 to 3 decisions, next week's plan |
| Monthly close and investor/advisor update | Monthly | 2 to 3 hours | Reconciled books, written update |
| Quarterly reset | Quarterly | Half day to 1 day | Scored OKRs, next quarter OKRs, risk register refresh, kill-criteria check |
| Annual plan | Annual | 1 to 2 days | 12-month plan, budget, scenarios, personal goals |

**Weekly business review template (adapted from the Amazon account in [Commoncog](https://commoncog.com/the-amazon-weekly-business-review/)):**

| Step | Question | Notes |
|---|---|---|
| 1. Customer | What did customers experience last week? | Support tickets, calls, churn reasons, 1 to 3 verbatim comments |
| 2. Scorecard | Which input and output metrics moved vs trailing 6 weeks and target? | 5 to 10 metrics max; flag only exceptions |
| 3. Why | For each exception: what is the cause, or "unknown, follow-up scheduled"? | Do not invent explanations |
| 4. OKR check | On track, at risk or off track per KR? | Notes only; no re-planning in the meeting |
| 5. Cash | Cash balance, 4-week burn, runway in months | One line |
| 6. Risks and decisions | Any register item changed? Any decision to log? | Link to the decision log |
| 7. Next week | Top 3 commitments | Saved where you will see them Monday |

**Monthly close.** **Inference:** Reconcile bank and payment-processor data, record revenue and costs, compute MRR, burn and runway from the same source, then write the update (section 5). Do it by working day 5 so the data is fresh.

**Quarterly reset.** Score OKRs, review the risk register and kill criteria, write a one-page "what I learned" note, set next quarter's one to three objectives, and book the next 90 days' deadlines.

**Annual plan.** Revenue, cost and runway scenarios (section 6), 3 to 5 bets, one thing to stop doing, and a personal-sustainability plan (time off, health).

**Time budget (Estimate, illustrative):** about 2.5 hours per week plus 3 hours per month plus 1 day per quarter is roughly 5% to 8% of a 40 to 50 hour week once annual time is averaged. If admin exceeds about 10% of working time, cut metrics before cutting customer contact.

**So what for a solo founder:** One 30-to-45-minute weekly review and one written monthly update carry most of the value; the quarterly reset is where you change course.

## 4. KPI selection

**Principles.**

- **Metrics tree.** **Fact (secondary):** Amazon's WBR deck is laid out as a causal chain where one process's output is another's input ([Commoncog](https://commoncog.com/the-amazon-weekly-business-review/), updated 2026-06). **Inference:** Draw a tree: revenue to customers x revenue per customer; customers to leads x conversion x retention. Pick leaf nodes you can influence this week.
- **Input vs output.** **Fact:** The WBR holds teams to controllable inputs (for example outreach sent, demos booked) and reports outputs (revenue) without debating them. Outputs lag; inputs steer.
- **Fewer is better.** Five to ten for a solo founder (**Inference**).

**Stage-appropriate set (Inference unless cited):**

| Stage | Core metrics |
|---|---|
| Pre-revenue | Interviews done, pre-orders/waitlist conversions, activation (first-value rate), weekly active users, cash and runway |
| Early revenue | MRR/ARR and growth, new/churned/expansion MRR, activation, retention by cohort, gross margin, burn, runway |
| Scaling | Above plus CAC and CAC payback, net revenue retention, burn multiple, customer concentration |

**Definitions and reference points (from [Sacks and Ruby, 2021-10-18](https://sacks.substack.com/p/the-saas-metrics-that-matter); over two years old and written in a looser-capital era, so thresholds may have shifted):**

- MRR/ARR: recurring only, excluding one-time services; ARR is 12 x MRR.
- CAC payback: sales and marketing spend divided by (new MRR x gross margin), in months. Omitting the gross-margin adjustment is a [common definitional error](https://www.getaleph.com/blog/2026-saas-benchmarks-takeaways) (snippet).
- Gross margin: they suggest a long-term target of at least 75%.
- Burn multiple: net burn divided by net new ARR; below 1 excellent, below 2 good.
- Customer concentration: largest customer under 10% of revenue is "low".
- Logo retention: roughly 70% to 95% annually depending on segment (small business low end, enterprise high end).

**Benchmarks (survey-based, directional only):**

- CAC payback median: about 16 months in 2025 (Benchmarkit, 198 B2B SaaS firms, middle half 10 to 24 months) per an [Aleph summary](https://www.getaleph.com/blog/2026-saas-benchmarks-takeaways) (search snippet only; not opened). Aleph is a finance software vendor.
- Gross margin: medians reported between about 75% and 77% across all B2B revenue types, and about 82% for pure SaaS, in different secondary sources (snippets); expect AI-heavy products about 5 points lower, per [Growth Unhinged / High Alpha, 2025-11-12](https://www.growthunhinged.com/p/2025-saas-benchmarks-report) (survey of 800+ mostly US firms; self-reported, sponsored by a pricing vendor, Metronome).
- Early-stage gross margins fell nearly 10 points year on year in that same survey; the author attributes it to AI costs likely, not proven.
- These samples skew to $5M to $20M ARR companies, so a solo founder under $1M ARR should read them as context, not targets.

**NPS caveats.** **Fact:** NPS is contested. Keiningham et al. (2007) rejected the claim that it is the single best predictor, and a 2024 study found customer satisfaction explains slightly more financial variance, though NPS also predicts ([search snippets](https://digitalcommons.memphis.edu/facpub2/182); not opened). Bias allegations about the original research are disputed by its vendor side. **Inference:** At small n, read verbatim comments, not the score.

**Data hygiene and single source of truth.** **Inference:**

- One owner per metric (you), one definition written down, one system of record per number (payments processor for revenue, bank for cash, product analytics for usage).
- Never hand-copy a number twice; link or export.
- Record the date and definition on every dashboard number; version definition changes.
- Reconcile revenue to bank monthly.
- Note data anomalies in the WBR instead of silently fixing them (the WBR design makes distortions visible; see [Commoncog](https://commoncog.com/the-amazon-weekly-business-review/)).

**So what for a solo founder:** Pick one activation, one retention, one revenue, one cash metric and one input metric per OKR; write each definition once and reconcile monthly.

## 5. Investor and board reporting

**Monthly update structure.** **Fact:** YC partner Aaron Harris advises leading with metrics, putting asks near the top, and ending with a short recap, per a [Visible.vc post, 2019-04-18](https://visible.vc/blog/tips-from-yc-using-asks-metrics-and-a-recap-to-power-your-investor-updates/) (secondhand; over two years old; Visible sells update software; YC's original template was not found). Other common templates add highlights, lowlights and team news (search snippets: [Visible](https://astro.visible.vc/blog/investor-updates), [OpenView](https://labs.openviewpartners.com/investor-update-template/)). We did not open First Round or a16z update guides; do not attribute specific templates to them.

Suggested outline (**Inference**, synthesised):

1. Headline in one or two sentences (green / yellow / red).
2. Key metrics vs last month and vs plan (MRR, growth, churn, cash, burn, runway).
3. Asks: specific, named (intros, hiring, advice), max three.
4. Highlights (wins) and lowlights (misses), each with one line on cause.
5. Priorities for next month, tied to OKRs.
6. Short appendix only if needed.

Keep it short and consistent; the point is that it is a habit. Length figures such as "250 to 750 words" come from a low-authority source and are unverified.

**Bad months.** **Fact:** Founder Collective's [Micah Rosenbloom (2018-03-19)](https://foundercollective.com/blog/how-to-break-bad-news-to-investors/) advises early disclosure, owning mistakes, phoning serious news rather than writing it, calling board members one-on-one before a meeting, and mixing good and bad news in regular updates. [SaaStr (Lemkin; undated, apparently 2024-25)](https://www.saastr.com/10-things-that-make-your-investors-lose-confidence) lists surprises, unclear runway, rosy updates and blaming the market as confidence-killers. **Inference:** In a bad month: lead with the miss and the number, state the cause you know and say what you don't, give the new runway date, show the action plan and decision date, and make one specific ask.

**Board deck structure (when a board exists).** **Fact:** [Sacks (2021-03-04)](https://sacks.substack.com/p/the-saas-board-meeting) suggests a two-hour quarterly meeting: CEO update with top priorities and KPIs (30 min), sales (30), other departments (20), financials (10 to 20), team (10 to 20), and admin in closed session (5 to 10). Deck goes out 1 to 2 days early with a consistent KPI package; he calls monthly board meetings generally counterproductive. Other templates exist (Carta, NextView seed-stage, Bain Capital Ventures via WaveUp) but were seen only as search snippets. **Inference:** For a solo CEO, collapse to: progress and problems, KPIs, financials and runway, risks, decisions needed. Put the decision you need from the board on slide one.

**Advisory board for a solo founder.** **Inference:** With no board, a small advisory group (two to four people with relevant experience) gives the challenge you otherwise lack. Meet quarterly; send the monthly update; ask each for one standing job (for example finance, distribution, technical). The Founder Institute's FAST agreement is one common template ([Founder Institute](https://fi.co/FAST), search snippet only): equity grids vary by version and source (a 2020 version listed 0.15% to 0.25% per standard advisor; other guides cite about 0.40% and total advisory pools of under 2% up to about 5%), with a three-month cliff. Treat equity as a range to negotiate, and get a lawyer to review. **Open:** current FAST grid not verified.

**So what for a solo founder:** Send the monthly update even with no investors (to advisors or yourself); it forces a monthly close and an honest read of the numbers.

## 6. Decision-making and risk

**Decision log / ADRs.** **Fact:** Michael Nygard's [2011-11-15 essay](https://hackmd.io/2OXCu_8MTcKA7emUvwrMSQ.md) (secondary copy; snippet) proposed a short record with Title, Status, Context, Decision, Consequences. A common critique: it omits rejected alternatives, so add them. Use for pricing, channels, tools, hires, legal structure.

Decision log template: date, decision, type (one-way / two-way, per the Bezos Type 1/Type 2 split above), context, options considered, chosen option and why, expected outcome and metric, review date, status. At review, compare expected vs actual: this builds calibration.

**Pre-mortems.** **Fact:** Gary Klein's [HBR (Sept 2007, 85(9), 18-19)](https://comprobo24.github.io/assignments/performing_a_project_premortem.pdf) technique: assume the project has failed and list reasons, before starting. A secondary source cites 1989 research showing imagining the event as already happened increased the number of reasons generated by about 30% (not verified at source). **Inference:** Run one before each quarter's biggest bet; 20 minutes alone, then add the top three causes to the risk register.

**Risk register template:**

| ID | Risk | Likelihood (1-5) | Impact (1-5) | Score | Early warning | Mitigation | Owner | Review date | Status |
|---|---|---|---|---|---|---|---|---|---|
| R1 | Single customer is over 30% of revenue | 3 | 5 | 15 | Contract renewal in 90 days | Diversify; sign multi-year | You | 2027-01-15 | Open |
| R2 | Founder unavailable for 2+ weeks | 2 | 5 | 10 | None | Continuity note, deputy | You | quarterly | Open |
| R3 | Key vendor/API change | 3 | 3 | 9 | Changelog | Abstraction; fallback vendor | You | monthly | Open |

(Example rows are illustrative.) Owner is always you; adding a named backup is part of the mitigation. Review the top five monthly.

**Key-person risk.** **Fact:** Practice guidance is mainly practitioner content ([Rework resource](https://resources.rework.com/libraries/founder-led-companies/business-continuity-beyond-founder), [Entrepreneur](https://www.entrepreneur.com/leadership/what-your-business-risks-if-a-founder-is-incapacitated/504493), search snippets); statistics about unprepared small businesses were uncorroborated and are omitted. The recurring advice: document where critical information lives and who may access it if you cannot, store credentials in a password manager with emergency access, review quarterly, and consider key-person insurance and a succession note. **Inference:** Minimum viable continuity pack: one page listing accounts, domains, payment processors, bank, legal entity docs, customers to notify, a trusted person with emergency access, and a documented "pause and wind-down" procedure. Check legal and insurance details with a professional.

**Runway scenarios.** **Inference:** Model three cases monthly: base, downside (revenue minus 30%, costs flat), and upside. For each, compute the cash-out date. Decide in advance the runway thresholds that trigger action (for example, at 9 months start cost cuts; at 6 months run the stop/adjust review). Thresholds are illustrative, not researched.

**Kill criteria and the go-adjust-stop gate.** **Fact:** Practitioner sources recommend defining success metrics, a time horizon and kill criteria in advance, and warn that teams under pressure tend to lower the bar or extend deadlines as the threshold nears (a [go/no-go template](https://godofstartups.com/knowledge/idea/when-to-kill-a-project), search snippet; and [Kromer on pivot or persevere](https://kromatic.com/blog/how-to-make-pivot-or-persevere-decisions-in-your-innovation-accounting), snippet). One claimed statistic about pivots with under six months of runway lacked a source and is excluded.

Gate template (**Inference**), written at the start of a quarter, reviewed at its end:

| Gate | Evidence required | Go | Adjust | Stop |
|---|---|---|---|---|
| Problem validated | 15 to 20 interviews; 3 pre-orders | Proceed to build | Narrow segment or message | Stop if no one will pay |
| Product pull | Activation and week-4 retention targets | Invest in growth | Fix onboarding/scope | Stop if retention near zero after 2 iterations |
| Efficiency | CAC payback and runway | Scale spend | Cut cost, change channel | Stop or sell if runway is under N months with no path |

Write the thresholds while calm, sign and date them, and move them only through a logged decision.

**So what for a solo founder:** Log decisions, run one pre-mortem a quarter, keep a five-row risk register, and sign your kill criteria before you are emotionally invested.

## 7. Automation: agents and scheduled tasks

**Where agents and schedules help (Inference):**

- Weekly digest: compile metrics, support themes and new competitor/market items into a Monday brief.
- Dashboard refresh: scheduled pulls from the system of record into the scorecard.
- Deadline sync: tax, filing, contract renewals and OKR review dates into your calendar with reminders.
- Draft work: first drafts of the monthly update and quarterly review from logged data, for you to edit.
- Hygiene checks: flag stale risks, missing review dates, metric definition changes.

**Where human judgment must stay:** choosing which metrics matter, interpreting anomalies ("do not invent explanations" applies to AI summaries too), setting and moving kill criteria, what to tell investors and customers, legal, tax and financial decisions, and anything involving relationships. Verify every number an agent reports against the source system. Never let an agent send external messages or move money without your approval.

**Pointers by name only (options, no claims about contents beyond their descriptions).**

- In-repo skills: `artifact-project-dashboard`, `scheduled-artifact-refresh`, `deadline-calendar-sync`, `recurring-research-digest`, `long-form-report-builder`.
- Third-party plugins: `business-analytics`, `business-operations-skills`, `pm-skills`, `c-level-agents`. Review each plugin's actual permissions and contents before installing.

**Staged plan.**

| Stage | Do |
|---|---|
| Week 1 | Write 1 to 2 objectives with baselines; pick 5 to 8 metrics and their definitions; create a scorecard, a decision log and a 5-row risk register; book the weekly review in your calendar; write the continuity page |
| Month 1 | Run 4 weekly reviews; do the first monthly close and write the first update; run a pre-mortem on your top bet; draft signed kill criteria; automate one weekly digest and one dashboard refresh; sync deadlines |
| Quarter 1 | Score OKRs and run the quarterly reset; review the risk register and gate; recruit 2 to 3 advisors if useful; review which metrics changed a decision and delete the rest; reassess automation against errors found |

**So what for a solo founder:** Automate the collecting and reminding; keep the deciding.

## Checklist

- [ ] 1 to 2 objectives with numeric KRs and baselines; committed vs stretch labelled
- [ ] 5 to 8 metrics with written definitions and a single source of truth each
- [ ] Metrics tree drawn; input metrics identified
- [ ] Weekly review booked (30 to 45 min) with the template
- [ ] Monthly close done by working day 5; update written (metrics, asks, highlights, lowlights, runway)
- [ ] Bad-news rule: lead with it, cause, plan, runway, one ask
- [ ] Decision log live; one-way decisions get options considered and a review date
- [ ] Pre-mortem done on the quarter's largest bet
- [ ] Risk register with likelihood, impact, mitigation, owner, review date
- [ ] Continuity page written and a trusted person has emergency access
- [ ] Three runway scenarios and signed go-adjust-stop criteria
- [ ] Quarterly reset and OKR scoring scheduled
- [ ] Automations limited to collecting, drafting and reminding; human review of numbers

## Open questions

- No independent, rigorous evidence found that OKRs, EOS or Scaling Up improve outcomes; Locke and Latham goal-setting literature not reviewed.
- Google's re:Work OKR guide could not be fetched; only a search snippet was seen, and its publication date is unconfirmed.
- YC's original investor-update template, First Round and a16z update guides, and Sequoia/Foresight board decks were not found or opened.
- Current CAC payback and gross-margin benchmarks: figures conflict across secondary sources and the Benchmarkit/Aleph report was not opened; solo and sub-$1M companies are underrepresented.
- Current FAST advisor equity grid not verified; legal review needed.
- Amazon WBR metric counts and Bezos letter details come from secondary accounts, not Amazon documents.
- Time-box and runway thresholds in this playbook are inferences, not researched optima.
- Reliable data on how much admin time solo founders actually spend was not found.

## Sources

All accessed 2026-11-11. "Snippet" means only the search-result summary was seen.

1. [Google re:Work, Set goals with OKRs](https://rework.withgoogle.com/en/guides/set-goals-with-okrs) (snippet; fetch failed)
2. [Commoncog, The Amazon Weekly Business Review](https://commoncog.com/the-amazon-weekly-business-review/) (published 2024-07-02, updated 2026-06-14; opened)
3. [EOS Worldwide, The Traction Component](https://www.eosworldwide.com/traction-component) (opened; vendor)
4. [What Matters, The OKR Origin Story](https://www.whatmatters.com/stories/the-origin-story) (opened; promotional)
5. [Sacks and Ruby, The SaaS Metrics That Matter](https://sacks.substack.com/p/the-saas-metrics-that-matter) (2021-10-18; opened)
6. [Sacks, The SaaS Board Meeting](https://sacks.substack.com/p/the-saas-board-meeting) (2021-03-04; opened)
7. [Visible.vc, Tips from YC on investor updates](https://visible.vc/blog/tips-from-yc-using-asks-metrics-and-a-recap-to-power-your-investor-updates/) (2019-04-18; opened; vendor)
8. [Founder Collective, How to Break Bad News to Investors](https://foundercollective.com/blog/how-to-break-bad-news-to-investors/) (2018-03-19; opened)
9. [SaaStr, 10 things that make your investors lose confidence](https://www.saastr.com/10-things-that-make-your-investors-lose-confidence) (undated; opened)
10. [Growth Unhinged, 2025 SaaS Benchmarks Report](https://www.growthunhinged.com/p/2025-saas-benchmarks-report) (2025-11-12; opened; sponsored)
11. [Aleph, 2026 SaaS benchmarks takeaways](https://www.getaleph.com/blog/2026-saas-benchmarks-takeaways) (snippet; vendor)
12. [OKR Institute, Why OKRs fail](https://okrinstitute.org/why-okrs-fail/) (snippet; vendor)
13. [Profit.co, Why enterprise OKR programs fail in year two](https://www.profit.co/blog/okr-university/why-most-enterprise-okr-programs-fail-in-year-two/) (snippet; vendor)
14. [ACE, Is EOS the answer or the leadership flavor of the month?](https://www.acecma.org/about/news/is-eos-the-answer-or-the-leadership-flavor-of-the-month-5312) (snippet)
15. [Scaling Up coaches, Mastering the Ten Rockefeller Habits](https://coaches.scalingup.com/blog/blog-post-title-one-lpc9d-ewsb7-k3ryp-jz5xl-ddfh3) (snippet)
16. [Chief Executive, How Amazon Does It: Decision Making](https://chiefexecutive.net/how-amazon-does-it-decision-making-inside-the-worlds-most-daring-digital-company/) (snippet; secondary on Bezos 2015/2016 letters)
17. [Baxter et al., Prometheus 38(2) on stage-gate](https://eprints.soton.ac.uk/468604/2/PROMETHEUS_38_2_Baxter_et_al.pdf) (snippet)
18. [PDMA, New Product Governance in a Time-Compressed World](https://community.pdma.org/knowledgehub/bok/product-innovation-process/new-product-governance-in-a-time-compressed-world) (snippet)
19. [Keiningham et al. via University of Memphis, NPS construct and predictive validity](https://digitalcommons.memphis.edu/facpub2/182) (snippet)
20. [Klein, Performing a Project Premortem (HBR 2007), copy hosted on GitHub Pages](https://comprobo24.github.io/assignments/performing_a_project_premortem.pdf) (snippet; unofficial copy)
21. [Nygard, Documenting Architecture Decisions, via HackMD copy](https://hackmd.io/2OXCu_8MTcKA7emUvwrMSQ.md) (snippet; secondary)
22. [Visible.vc, Investor updates](https://astro.visible.vc/blog/investor-updates) (snippet; vendor)
23. [OpenView, Template for the Perfect Investor Update](https://labs.openviewpartners.com/investor-update-template/) (snippet)
24. [Founder Institute, FAST agreement](https://fi.co/FAST) (snippet)
25. [Rework, Business continuity beyond the founder](https://resources.rework.com/libraries/founder-led-companies/business-continuity-beyond-founder) (snippet)
26. [Entrepreneur, What your business risks if a founder is incapacitated](https://www.entrepreneur.com/leadership/what-your-business-risks-if-a-founder-is-incapacitated/504493) (snippet)
27. [God of Startups, When to kill a project](https://godofstartups.com/knowledge/idea/when-to-kill-a-project) (snippet)
28. [Kromatic, Pivot or persevere](https://kromatic.com/blog/how-to-make-pivot-or-persevere-decisions-in-your-innovation-accounting) (snippet)
