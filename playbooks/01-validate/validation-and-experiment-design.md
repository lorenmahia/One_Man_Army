# Validation and Experiment Design: Turning an Idea into Evidence Before Spending Money

> Last verified: 2026-11-11. Research and planning support only; not legal, tax, investment or financial advice.

## Summary

- **Fact:** Public post-mortems keep pointing at demand and money. CB Insights' March 2026 study of 385 VC-backed shutdowns found 70% ran out of capital and 43% cited poor product-market fit; older CB Insights data put "no market need" near 42%. These are VC-backed, self-reported samples, so treat them as signals, not base rates for solo businesses.
- **Inference:** Cheap evidence ordered by strength beats opinion: past behaviour in interviews, then commitments of time, money or reputation (pre-orders, paid pilots), then clicks, then compliments.
- **Fact:** Small samples are fine for finding patterns (about 5-12 interviews per segment) but weak for measuring rates. A 0-of-20 result still leaves a true rate of up to about 16% plausible (Wilson interval, computed below).
- **Fact:** Stated-price methods (Van Westendorp, Gabor-Granger) suffer from hypothetical bias. A real price ask, with a real payment attempt, is the strongest cheap price test.
- **Inference:** Write the success and failure thresholds before you start. Decide go, adjust or stop at a dated gate, and kill ideas cleanly rather than drifting.

## 1. The failure data: why startups fail

**Fact (CB Insights, 2026).** CB Insights studied 431 VC-backed companies that publicly shut down since 2023 and could identify reasons for 385. Shares (companies can cite several, so they exceed 100%): ran out of capital 70%, poor product-market fit 43%, bad timing or macro conditions 29%, unsustainable unit economics 19% ([CB Insights, startup failure reasons, 5 Mar 2026](https://www.cbinsights.com/research/startup-failure-reasons-top/)). The report itself treats running out of cash as usually the final cause, not the root problem. Limits: VC-backed only, public post-mortems only, companies with a prior exit excluded, and the author is a commercial data vendor analysing its own platform.

**Older figure (flag: about 8-9 years old).** An earlier CB Insights post-mortem list is widely summarised as 42% "no market need", 29% ran out of cash, 23% wrong team, 19% outcompeted, from about 101 failed startups. I could only see this as a secondary-source search snippet, and one summary said the share varied across editions (about 35-42%) ([Top 20 Reasons Startups Fail: CB Insights, secondary summary, c. 2018, snippet only](https://startupnews.com.au/news/top-20-reasons-startups-fail-cb-insights/)). Treat 42% as a range of roughly 35-42%, and note that the 2026 "product-market fit 43%" is a similar order of magnitude though categories differ.

**Startup Genome (2011, over 15 years old; fast-moving topic).** Blackbox/Startup Genome analysed over 3,200 high-growth tech startups from February 2011 and reported premature scaling in 70% of failed startups, no prematurely scaled startup passing 100,000 users, and 93% never reaching $100K revenue ([TechCrunch, 1 Sep 2011](https://techcrunch.com/2011/09/01/a-deeper-look-at-blackboxs-data-on-startup-failure-and-its-top-cause-premature-scaling-infographic)). The article itself flags critics, a loose definition ("core dimensions moving at mismatched speeds") and no independent verification. Secondary sources conflict on some figures (for example the 100,000-user versus $100K-per-month thresholds), so use it only as a directional argument.

**What this implies.**
- **Inference:** Demand risk and cash risk are linked: building before evidence burns the cash that later kills the company. Validation is cheap insurance against the "build, then discover nobody wants it" path.
- **Inference:** Samples are VC-backed tech companies; a solo service or local business has different failure modes (owner burnout, thin margins, regulation) that these studies do not measure. See Open questions.

**So what for a solo founder:** Spend the first weeks buying evidence of demand and willingness to pay, not building; your runway is the thing the data says usually ends companies.

## 2. Problem validation: customer discovery

### Methods compared

| Method | Core idea | Best for | Main weakness |
|---|---|---|---|
| The Mom Test (Fitzpatrick) | Talk about their life, ask about specific past behaviour, listen more than you talk, seek commitment over compliments ([book site](https://www.momtestbook.com/); [summary, snippet only](https://www.supersummary.com/the-mom-test/summary/)) | Early problem discovery, any business type | Book-level guidance; no numeric thresholds |
| Jobs-to-be-Done "switch" interview (Moesta, Spiek) | Reconstruct a recent purchase or switch timeline; map push, pull, anxiety and habit ([JTBD switch interview](https://jobstobedone.org/switch-interview/)) | Understanding why people buy and switch; positioning | Needs people who recently switched; 45-90 minutes each; recall fades after about 30-90 days |
| Lean Customer Development (Alvarez) | Short interviews with people who have the problem; recent specific behaviour; notes on emotion ([secondhand notes by J. Stark](https://jonathanstark.com/notes-on-lean-customer-development)) | Quick B2B and consumer discovery | I only saw secondhand notes, not the book |
| Customer Development (Blank) | State business-model hypotheses, then test problem and solution outside the building before scaling ([Startup Owner's Manual, snippet only](https://smeportal.unescwa.org/sites/default/files/2019-12/The_Startup_Owner%20s_Manual-A%20step%20by%20step%20guide%20for%20building%20a%20great%20company.pdf)) | Framing the whole sequence | Heavier process than a solo founder needs |
| YC "How to Talk to Users" (Migicovsky) | Specifics about past events beat hypotheticals; based on The Mom Test | Founders new to interviewing | The author's own 2025 note says he rarely uses the framework himself ([Migicovsky blog, 2019, note 2025](https://ericmigi.com/blog/startup-school-how-to-talk-to-users)); I could not retrieve the talk's detail |

**Inference:** These methods agree on the essentials (ask about the past, avoid pitching, treat compliments as noise) and differ mainly in what they interview for: problems (Mom Test, Lean Customer Development) versus buying decisions (JTBD). Use the first to find a problem worth solving, the second once people already buy something.

### How many interviews are enough? (sources disagree)

- **Qualitative research:** In one study of 60 interviews, 92% of themes (100 of 114) appeared within the first 12, and 70% (80 of 114) in the first 6; the population was fairly homogeneous ([Guest, Bunce and Johnson 2006, via ALNAP; snippet only](https://library.alnap.org/node/58582)). Arithmetic check: 80/114 = 70.2%, 100/114 = 87.7%. The 92% quoted in the snippet does not match 100/114, so I report the percentages as quoted and flag the inconsistency; verify against the paper.
- **Founder practice:** JTBD practitioners say patterns often emerge within 5-8 interviews for a given job ([JTBD switch interview](https://jobstobedone.org/switch-interview/)). A secondhand summary of Alvarez says start with about 5 and do 5-10 more per iteration (search snippet; unverified).
- **Usability testing (different task):** Nielsen's model says 5 users find about 85% of problems if one user finds 31%; recomputed as 1 - 0.69^5 = 0.84. The 31% is an average, the article dates from 2000, and distinct user groups need 3-4 people each ([NN/g, 2000](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)). This is about finding usability problems, not validating demand.
- **Disagreement:** Five-ish is the lower bound; twelve is a common saturation point for one homogeneous segment; ten to twenty across several segments is plausible. **Estimate:** 8-12 per segment, stopping when the last 3 interviews add no new pain, workaround or objection. Keep conversations about problems separate from conversations about price.

### Recruiting without a network

- **Fact:** Send short, personal emails, follow up once after about a week, and ask for about 20 minutes ([Stark notes](https://jonathanstark.com/notes-on-lean-customer-development); [Lean B2B](https://leanb2bbook.com/blog/b2b-customer-interviews-with-cold-emails/)).
- **Range of reply rates:** the Lean B2B author says "as many as 30%" of cold emails can become interviews, with no data given; a secondhand roundup cites 2-10% from a 2023 platform dataset (snippet only). Plan for 5%, not 30%: about 10 interviews needs roughly 200 well-targeted emails at 5%.
- **Where:** LinkedIn, topic forums, mailing lists and places where the people gather; ask each contact for one introduction; avoid recruiting friends and family ([Stark notes](https://jonathanstark.com/notes-on-lean-customer-development)).

### Biases to design against

- **Politeness and hypotheticals:** people give aspirational answers about the future; ask about the last time it happened ([Stark notes](https://jonathanstark.com/notes-on-lean-customer-development)).
- **Leading questions** ("Don't you think...?") and pitching your idea.
- **Confirmation bias (Inference):** you hear what supports your idea; have a second person read raw notes.
- **Sampling bias (Inference):** friendly or easy-to-reach people overrepresent satisfied or tech-savvy users; also interview people who rejected or churned from alternatives.
- **Survivorship in JTBD:** include people who nearly switched but did not ([JTBD](https://jobstobedone.org/switch-interview/)).

### Synthesis

1. Record the dominant emotion and a one-sentence summary right after each interview ([Stark notes](https://jonathanstark.com/notes-on-lean-customer-development)).
2. Log each fact as: who, what they did last time, cost or workaround, and any commitment offered.
3. Tally across interviews: how many have the problem, have recently tried to solve it, spend money or time on it, and accepted a next step.
4. Separate observations (what happened) from your interpretations.

**So what for a solo founder:** Do 8-12 past-behaviour interviews per segment, recruit at roughly 5% reply rates, and count commitments rather than compliments.

## 3. Demand and solution tests, ranked by cost and evidence strength

Order from cheapest and weakest to costlier and strongest. Cost figures are **Estimates** (my own ballparks), as none of the sources I opened gave pricing.

| Test | Typical cost | Proves | Cannot prove |
|---|---|---|---|
| Fake door / landing page + waitlist | Near zero to low | Message and offer attract attention and an email | Willingness to pay; that the product works; email-giving costs nothing |
| Smoke test with ads | Ad budget (low hundreds) | Cold-traffic interest at a measurable click and signup rate | Retention; traffic quality varies by channel |
| Pricing-page / payment-click test | Low | Interest survives a price | Actual payment unless money moves |
| Concierge MVP | Your time | People adopt a hand-delivered service; reveals what they value | Scalability or margins |
| Wizard-of-Oz MVP | Moderate time | Users accept the apparent product; reveals real workflows | Automation economics |
| Pre-sales, deposits, letters of intent | Low cash, high effort | Real commitment (deposits strongest; LOIs are non-binding) | Delivery capacity; repeat purchase |
| Paid pilot | Your time plus delivery | Budget, buying process and value in a real setting | Broad market demand |
| Crowdfunding | Campaign prep, fees, rewards | Public demand and audience reach | Durable demand beyond an enthusiast crowd |

**Landing page + waitlist.** Fact: Buffer first put up a two-page test (product page, then email capture), then inserted a pricing page; people kept clicking through, a small number clicked paid plans, and no exact figures were published; the first paying customer came within 4 days of launch and conversion to paid was about 4% after about two and a half months ([Buffer, 16 Feb 2011](https://buffer.com/resources/idea-to-paying-customers-in-7-weeks-how-we-did-it)). The post is 15 years old and a success story, so survivorship bias applies. Benchmark: Unbounce's SaaS landing-page median conversion is 3.8% (all-industry 6.6%); paid search 4.1%, paid social 2.9%, display 0.3%; the report is gated, so methodology is unverified, and Unbounce is a vendor ([Unbounce SaaS benchmark](https://unbounce.com/conversion-benchmark-report/saas-conversion-rate/); year not shown on page, a 2024 report per a search summary). Mistake: counting email signups from friends as demand.

**Demo video as a smoke test.** Secondary accounts say Dropbox's demo video took its beta waitlist from about 5,000 to about 75,000 in roughly a day (snippet-only; sources disagree on video length of 3 or 4 minutes) ([YourStory, 2026, could not open page](https://yourstory.com/2026/02/dropbox-fake-demo-video-75k-signups-mvp)). Caveat: audience-specific (the video was tailored to Digg readers) and exceptional.

**Fake-door tests.** Show a button or feature that does not exist yet, count clicks, then tell people honestly it is not ready and offer a waitlist (see ethics, section 6). Mistake: deceiving people about payment; never take money for something you cannot deliver.

**Concierge and Wizard-of-Oz.** Concierge means delivering the service by hand and visibly; Wizard of Oz means the customer sees a finished-looking product while you do the work manually behind it. The Food on the Table slides argue that if people will not adopt your idea with high-touch service, they will not adopt a cold web page, and describe serving the first users by hand ([Rosso slides, snippet only](https://www.slideshare.net/TheLeanStartup/manuel-rosso-food-on-the-table)). Rule of thumb (**Inference**): serve 5-10 customers by hand before automating anything.

**Pre-sales, LOIs and paid pilots.** **Inference:** order of strength is cash paid > refundable deposit > signed LOI > verbal promise. A paid pilot is the best test for B2B because it also exposes the buying process. Mistake: counting "I'd buy that" or friendly LOIs from people who cannot sign a purchase order.

**Crowdfunding as validation.** The 2025 Kickstarter year-in-review gave no platform-wide success rate ([Kickstarter, 2025 review](https://updates.kickstarter.com/a-year-in-review-2025-kickstarter-highlights/)); third-party estimates put the overall rate at about 39-40% (snippet only, [Search Logistics](https://searchlogistics.com/learn/statistics/kickstarter-stats-facts)). Success usually reflects your existing audience and marketing, so a funded campaign validates reach as much as the product. Mistake: promising fulfilment dates you cannot meet.

**Ads-driven demand tests: rules of thumb.** There is no authoritative minimum sample. Use the interval math in section 5: with 100 visitors and 5 signups, the plausible true rate is about 2.2% to 11.2%, which still straddles the 3.8% SaaS median. **Estimate:** pre-set a threshold, run at least 200-300 targeted visitors, and treat the result as directional.

**Common mistakes across all tests:** measuring vanity actions (likes, free signups); changing the page mid-test; mixing traffic sources; stopping the moment the number looks good.

**So what for a solo founder:** Climb the ladder one rung at a time and stop at the cheapest test that can falsify your idea; only a payment, deposit or paid pilot counts as strong evidence of demand.

## 4. Pricing and willingness-to-pay tests with small samples

| Method | How it works | Honest limits |
|---|---|---|
| Van Westendorp | Four questions: too cheap, a bargain, expensive, too expensive | Hypothetical bias; the source calls it "not fully reputable", and only 8 of 60 surveyed companies used it ([Berman on Lenny's Newsletter, 13 Feb 2024](https://www.lennysnewsletter.com/p/the-ultimate-guide-to-willingness)) |
| Gabor-Granger | Yes/no purchase intent at a sequence of prices | Anchoring on the first price; the researcher picks the price grid ([Marketbridge, snippet only; vendor](https://marketbridge.com/article/survey-pricing-methodologies/)) |
| Conjoint / discrete choice | Choose among product bundles that vary in features and price; infer value of each attribute | Long, harder to design, needs statistical software and a larger sample; usually out of reach for a solo founder ([Berman](https://www.lennysnewsletter.com/p/the-ultimate-guide-to-willingness)) |
| Direct price ask | Quote a real price and ask for payment or a deposit | Small samples; but behaviour, not opinion |
| BDM incentive-aligned ask | Stated maximum compared to a random price; binding purchase | Participants often find it confusing ([Berman](https://www.lennysnewsletter.com/p/the-ultimate-guide-to-willingness)) |

**Hypothetical bias, Fact (secondhand):** the same article cites a donation study where a real treatment raised $310 and a hypothetical one pledged $780 (more than twice as much); I did not verify the underlying study. The article gives no recommended sample sizes.

**Practical small-sample approach (Inference):**
1. Interview about the current cost of the problem (time, money, workaround) before showing a price.
2. Quote one of two or three price points to different prospects and ask for a deposit or a pre-order.
3. Record accept, counter or decline, and the reason. Also note price-anchoring: the first number you say affects the answer.
4. Treat Van Westendorp or Gabor-Granger output from fewer than about 30-50 respondents as a rough range only (**Estimate**; no source gave a minimum).

**So what for a solo founder:** Ask for real money at a stated price from a handful of qualified prospects; use survey methods only to bracket a range.

## 5. Experiment design for tiny samples

**Hypothesis template.** "We believe [segment] has [problem]. If we offer [solution] at [price], then at least [X of N] will take [specific action] within [time]." Add a kill statement: "If fewer than [Y of N], we will not build [Z]."

**Write criteria in advance.** Fix the segment, action, sample size, duration, and the pass, adjust and fail thresholds before you look at any results. Record them in the log with a date.

### Confidence intervals for small counts

Use the Wilson score interval, not the simple "plus or minus" formula. The simple (Wald) interval collapses to zero width when you see 0 successes and can leave the 0-1 range at small n; Wilson avoids both ([Wikipedia, Binomial proportion confidence interval](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval)). Rule of three: with 0 successes in n trials, the 95% upper bound is about 3/n (same source). Wilson at 0 successes is [0, 3.84/(n + 3.84)] ([arXiv 2109.12464, snippet only](https://arxiv.org/pdf/2109.12464)).

I computed these 95% Wilson intervals (z = 1.96) and rechecked them in a short script:

| Result | Observed rate | 95% interval |
|---|---|---|
| 0 of 20 | 0% | 0% to 16.1% (rule of three: 3/20 = 15%) |
| 2 of 10 | 20% | 5.7% to 51.0% |
| 4 of 40 | 10% | 4.0% to 23.1% |
| 3 of 50 | 6% | 2.1% to 16.2% |
| 5 of 100 | 5% | 2.2% to 11.2% |
| 10 of 100 | 10% | 5.5% to 17.4% |

**Reading it:** 4 yes answers out of 40 does not mean 10%; it is consistent with anything from about 4% to 23%. You need the whole interval to clear your pass threshold, or the upper end to fall below your fail threshold, to call the test.

### Why p-values mislead at small n

The American Statistical Association states that a p-value is not the probability that the hypothesis is true or that the data arose by chance alone, and it should not be the sole basis for decisions ([ASA statement, Wasserstein and Lazar, 2016](https://www.stat.berkeley.edu/%7Ealdous/Real_World/ASA_statement.pdf); principle wording from a search summary, as the PDF text was not readable here). **Inference:** with 20 or 30 observations, a non-significant result mostly means "too little data", not "no effect", and a lucky significant result is easily a fluke. Prefer intervals plus pre-set thresholds, and repeat the test.

### Avoiding confirmation bias
- Pre-register thresholds (above); record failures as carefully as wins.
- Define the denominator in advance (who counts as a qualified visitor or prospect).
- Do not drop "outliers" after the fact; do not run until the number looks good.
- Ask someone else to challenge the interpretation.

### Experiment log template (columns)
Date; hypothesis; segment; test type; pass / adjust / fail thresholds (written before the test); sample size planned; start and end dates; raw counts; 95% interval; decision; what we learned; next action; cost in money and hours.

**So what for a solo founder:** Write the thresholds first, report counts with an interval, and let the whole interval, not the point estimate, decide.

## 6. Market sizing, alternatives mapping, and research ethics

### Market-size sanity checks
- **Bottom-up:** buyers you can actually reach times realistic annual price; top-down: a published market figure narrowed by segment. Triangulate; a large gap means one set of assumptions is wrong ([Waveup, vendor blog](https://waveup.com/blog/top-down-and-bottom-up-market-size-calculation/)). The page's 20% and 2x thresholds and 1-5% penetration claims are unsourced heuristics; the page itself is a fundraising consultancy's marketing.
- **Pitfall:** sizing the market as what customers earn or spend overall rather than what you can charge them (the grocery-store example in the same source).
- **Worked example (illustrative):** 5,000 reachable clinics times $600 per year equals $3.0M per year; 2% share is 100 clinics, equal to $60,000 per year. This is an **Estimate** from invented inputs; replace with interview and pilot data. For a solo business, check whether the realistic revenue in year one covers your minimum income, using the in-repo `unit-economics-model` skill.

### Competitor and alternative mapping
List what the customer does today, not just direct competitors: spreadsheets, hired help, doing nothing, a rival product. For each, record price, switching cost, what they like and complain about (from interviews and public reviews), and why the customer might not switch. The JTBD forces (habit of the present, anxiety about the new) are a useful checklist ([JTBD](https://jobstobedone.org/switch-interview/)).

### Research ethics
- **Consent:** tell people who you are, why you are asking and how you will use the answers; let them stop at any time. The Belmont principles (respect for persons, beneficence, justice) underpin this ([Belmont summary, snippet only](https://vpr.tamu.edu/research-compliance/human-research-protection-program/using-deception-and-incomplete-disclosure-in-research)).
- **No deception that costs people money or trust:** fake-door tests should disclose promptly ("not available yet; join the list") and never collect payment for undeliverable goods. Research ethics sources treat deception as needing debriefing at minimum (same source).
- **Privacy:** collect the minimum; store notes without identifiers where possible; get permission before recording; delete on request. Privacy law varies by country (**Inference**; check with `country-business-research`).
- **Regulated sectors (health, finance, children, legal):** do not collect health or financial details in interviews without legal advice; do not make claims that look like medical or investment advice; check licensing before charging pilots.
- **Respect for time:** keep to 20 minutes unless agreed otherwise; do not turn research into a sales pitch.

**So what for a solo founder:** Size the market from the bottom up using real prices, map the "do nothing" alternative, and tell people the truth about what you are doing.

## 7. The go / adjust / stop gate

### Example criteria (illustrative **Estimates**; set your own before testing)

| Business type | Go | Adjust | Stop |
|---|---|---|---|
| B2B SaaS / service | 3+ of 10 target buyers sign paid pilot or LOI at the stated price | Interest but price or buyer role unclear | 0 paid commitments from 15+ qualified prospects |
| Consumer product | Pre-orders or deposits above a set count at the target price | Clicks but no payments | Interval upper bound below the rate needed to cover ad costs |
| Local service | 5+ prepaid bookings at target price | Bookings only with discounts | Fewer than 2 bookings from a targeted push |
| Creator / content product | Paid presale covers production costs | Audience engages but will not pay | Audience below the size the economics require |

Tie each threshold to the economics: the conversion you need follows from price, cost and your cost of acquiring a customer (see `unit-economics-model`).

### Deciding when evidence is mixed
1. Is the problem real and recurring (interview evidence) but payment weak? Adjust price, segment or offer, then retest once.
2. Is interest strong from one subgroup only? Narrow to that segment.
3. Are results inside a wide interval that includes both pass and fail? Extend the sample once, to a pre-set cap.
4. Set a maximum of two adjustment rounds before a forced decision.

### Pivot types (published taxonomies)
Ries's 2009 post names segment (same product, different customers), customer-problem (different problem, same customers) and feature (narrow to one feature) pivots, and says pivoting follows learning rather than jumping to a new vision ([Ries, 22 Jun 2009](https://www.startuplessonslearned.com/2009/06/pivot-dont-jump-to-new-vision.html)). The later book lists ten types, including zoom-in, zoom-out, customer need, platform, business architecture, value capture, engine of growth, channel and technology; I only saw secondary summaries ([Shortform, snippet only](https://shortform.com/blog/?p=7909)).

### Killing an idea cleanly
- Record the decision, the data and the date in the experiment log.
- Thank and inform interviewees and waitlist members; delete unneeded personal data and refund any deposits.
- Write a one-page post-mortem: assumptions tested, what failed, what you would do differently.
- Salvage reusable assets (audience, interviews, code) and set a cooling-off period before choosing the next idea.

### Staged plan

| When | Do |
|---|---|
| **Week 1** | Write hypotheses and thresholds. List 30-50 target contacts. Send about 100 outreach messages. Book 5 interviews. Map alternatives. Start the experiment log. |
| **Month 1** | Complete 8-12 interviews per segment. Synthesise. Run one cheap demand test (landing page or concierge). Quote a real price to 5-10 prospects. Mid-month review against thresholds. |
| **Quarter 1** | Run a stronger test (pre-sales, deposits or paid pilot). Check unit economics. Make the go / adjust / stop decision at a scheduled date; at most two adjust rounds. |

**So what for a solo founder:** Put the gate date in your calendar now; a decision made on schedule beats months of drift.

### Pointers (names only)
- In-repo skills: `customer-discovery-interviews`, `country-business-research`, `unit-economics-model`, `start-here`.
- Third-party plugins (options only; check their own descriptions): `startup-business-analyst`, `before-you-build`, `executive-mentor`.

## Checklist

- [ ] Written hypothesis, success and failure thresholds, with a date, before any test
- [ ] 8-12 past-behaviour interviews per segment, with notes in a standard format
- [ ] Recruited beyond friends and family; recorded reply rates
- [ ] Commitments (time, money, reputation) counted separately from compliments
- [ ] At least one demand test with a real call to action
- [ ] A real price quoted to qualified prospects
- [ ] Results reported with a 95% interval, not just a percentage
- [ ] Bottom-up market size and alternatives map completed
- [ ] Consent, privacy and no-deception rules followed
- [ ] Go / adjust / stop decision logged on the scheduled date

## Open questions

- Base rates for solo, bootstrapped and non-tech businesses: the failure studies above cover VC-backed or high-growth tech samples. I found no comparable source.
- Original CB Insights "no market need" (42%) report: only secondary summaries were seen; edition and date unconfirmed.
- Guest et al. 2006: the quoted 92% for 12 interviews does not match 100/114; check the paper.
- Primary text of Fitzpatrick's rules, Alvarez's book, Migicovsky's talk and the NN/g interview-sample-size article could not be retrieved; claims about them rest on secondary notes or snippets.
- Rules for minimum sample sizes of ads-driven smoke tests, LOI conversion rates and pre-sale benchmarks: no authoritative source found.
- Dropbox and Kickstarter figures are secondary or third-party; the Kickstarter overall success rate is unverified.
- The ASA statement's exact wording was not readable in the fetched PDF.
- ESOMAR or national market-research codes and local privacy law were not checked.

## Sources

Accessed 2026-11-11. "Snippet only" means I saw only search-result text, not the page.

1. [CB Insights, startup failure reasons (5 Mar 2026)](https://www.cbinsights.com/research/startup-failure-reasons-top/)
2. [Top 20 Reasons Startups Fail: CB Insights (secondary; snippet only)](https://startupnews.com.au/news/top-20-reasons-startups-fail-cb-insights/)
3. [TechCrunch, Blackbox/Startup Genome data (1 Sep 2011)](https://techcrunch.com/2011/09/01/a-deeper-look-at-blackboxs-data-on-startup-failure-and-its-top-cause-premature-scaling-infographic)
4. [Nielsen Norman Group, Why You Only Need to Test with 5 Users (2000)](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
5. [Guest, Bunce and Johnson 2006, via ALNAP (snippet only)](https://library.alnap.org/node/58582)
6. [Migicovsky, How to Talk to Users (blog, 2019 with 2025 note)](https://ericmigi.com/blog/startup-school-how-to-talk-to-users)
7. [The Mom Test book site](https://www.momtestbook.com/)
8. [Mom Test summary (snippet only)](https://www.supersummary.com/the-mom-test/summary/)
9. [Jonathan Stark, Notes on Lean Customer Development (secondhand)](https://jonathanstark.com/notes-on-lean-customer-development)
10. [Lean B2B, cold emails for customer interviews (undated)](https://leanb2bbook.com/blog/b2b-customer-interviews-with-cold-emails/)
11. [Jobs to be Done, switch interview](https://jobstobedone.org/switch-interview/)
12. [The Startup Owner's Manual (snippet only)](https://smeportal.unescwa.org/sites/default/files/2019-12/The_Startup_Owner%20s_Manual-A%20step%20by%20step%20guide%20for%20building%20a%20great%20company.pdf)
13. [Ries, pivot post (22 Jun 2009)](https://www.startuplessonslearned.com/2009/06/pivot-dont-jump-to-new-vision.html)
14. [Shortform, pivot types (snippet only; secondary)](https://shortform.com/blog/?p=7909)
15. [Berman, The ultimate guide to willingness-to-pay, Lenny's Newsletter (13 Feb 2024)](https://www.lennysnewsletter.com/p/the-ultimate-guide-to-willingness)
16. [Marketbridge, survey pricing methodologies (snippet only; vendor)](https://marketbridge.com/article/survey-pricing-methodologies/)
17. [Wikipedia, Binomial proportion confidence interval](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval)
18. [arXiv 2109.12464, Wilson score interval properties (snippet only)](https://arxiv.org/pdf/2109.12464)
19. [ASA statement on p-values, 2016 (PDF unreadable; summary via search)](https://www.stat.berkeley.edu/%7Ealdous/Real_World/ASA_statement.pdf)
20. [Buffer, Idea to Paying Customers in 7 Weeks (16 Feb 2011)](https://buffer.com/resources/idea-to-paying-customers-in-7-weeks-how-we-did-it)
21. [Unbounce SaaS conversion benchmarks (vendor; gated report)](https://unbounce.com/conversion-benchmark-report/saas-conversion-rate/)
22. [YourStory on Dropbox demo video (2026; page not opened, snippet only)](https://yourstory.com/2026/02/dropbox-fake-demo-video-75k-signups-mvp)
23. [Kickstarter, 2025 year in review](https://updates.kickstarter.com/a-year-in-review-2025-kickstarter-highlights/)
24. [Search Logistics, Kickstarter stats (snippet only; third party)](https://searchlogistics.com/learn/statistics/kickstarter-stats-facts)
25. [Rosso, Concierge MVP slides (snippet only)](https://www.slideshare.net/TheLeanStartup/manuel-rosso-food-on-the-table)
26. [Waveup, top-down vs bottom-up market sizing (vendor)](https://waveup.com/blog/top-down-and-bottom-up-market-size-calculation/)
27. [Texas A&M, deception and incomplete disclosure in research (snippet only)](https://vpr.tamu.edu/research-compliance/human-research-protection-program/using-deception-and-incomplete-disclosure-in-research)
