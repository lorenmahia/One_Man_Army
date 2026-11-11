# Early-stage fundraising: instruments, terms, valuation, dilution and process

> Last verified: 2026-11-11. Research and planning support only; not legal, tax, investment or financial advice.

## Summary

- **Instrument choice is mostly settled at pre-seed:** about 93% of pre-seed rounds on Carta in Q2 2026 were SAFEs, so expect a post-money SAFE first and a priced round later. [Carta: State of Pre-Seed Q2 2026](https://carta.com/data/state-of-pre-seed-q2-2026/) (figure via search snippet; page not openable, so Carta-platform only).
- **A post-money SAFE fixes the investor's percentage, so later SAFEs and the option pool dilute you, not earlier SAFE holders.** Model every SAFE before you sign the next one. [Torys, 2021](https://www.torys.com/insights/publications/2021/02/pre-money-versus-post-money-safe).
- **Priced-round terms are fairly standardized:** 1x non-participating preference in about 96% of Cooley-handled Q2 2026 deals, and broad-based weighted-average anti-dilution is near-universal. The negotiable levers are valuation, option-pool size and placement, board control and protective provisions. [Cooley Q2 2026](https://www.cooley.com/news/insight/2026/2026-08-17-q2-2026-venture-financing-report).
- **Benchmarks vary widely by source and geography:** US seed median pre-money is about $16M for 2025 (PitchBook-NVCA) and median seed round size about $3M (Crunchbase); expect roughly 18-20% dilution at seed. Treat these as ranges, not targets.
- **Plan for months, not weeks, and for professional help:** legal fees averaged under $10k at pre-seed and about $17k at seed in one dataset (Feb 2024), and seed-to-Series A now often takes over two years.

## 1. Instruments compared

### 1.1 Post-money SAFE (and the older pre-money form)

- **What it is (Fact):** a Simple Agreement for Future Equity, created at Y Combinator in 2013; YC standardized on the post-money version in 2018. It has no interest and no maturity date. [YC documents page](https://www.ycombinator.com/documents) (accessed 2026-11-11).
- **Valuation cap (Fact):** the highest valuation at which the SAFE converts. In the post-money form the cap includes the SAFE money, so ownership sold is roughly investment divided by cap (YC's example: $1M at a $6.7M cap sells about 15%). [YC documents page](https://www.ycombinator.com/documents).
- **Discount (Fact):** converts at a percentage below the priced-round price; YC says discounts are commonly 10-20%. If a SAFE has both cap and discount, the investor generally gets whichever price is lower (Inference from standard mechanics; confirm in the actual form). [YC documents page](https://www.ycombinator.com/documents).
- **MFN (Fact):** no cap or discount; adopts the best terms of later SAFEs. YC notes the MFN date is the later of signing or wire receipt, so fund lower-cap SAFEs first. [YC documents page](https://www.ycombinator.com/documents).
- **Pro rata (Fact):** not in the SAFE itself; offered through an optional standardized side letter giving a right, not an obligation, to invest in a future priced round. Versions exist for US, Canada, Cayman and Singapore companies. [YC documents page](https://www.ycombinator.com/documents).
- **Pre-money vs post-money (Fact):** in a pre-money SAFE the capitalization excludes shares from other SAFEs, so later SAFEs dilute earlier SAFE holders and the investor cannot easily compute their stake. In a post-money SAFE the capitalization includes all SAFE conversion shares, so dilution from later SAFEs falls on founders and employees. The post-money form also excludes the option-pool increase made in the priced round. [Torys, 2021](https://www.torys.com/insights/publications/2021/02/pre-money-versus-post-money-safe) (older than two years, but the mechanics are definitional).
- **Market share (Fact, Carta platform only):** about 91% of SAFEs on Carta were post-money, and 94% of post-money SAFEs in H1 2026 had a valuation cap. [Carta: SAFE valuation caps Q2 2026](https://carta.com/data/safe-valuation-caps-q2-2026/) (via search snippet).
- **Founder pros:** fast and cheap, no debt, no repayment deadline, flexible when the next round is uncertain. **Cons:** stacked SAFEs compound dilution and the shift can feel sudden unless modelled; investors have fewer enforcement tools, which some dislike. [Stripe: notes vs SAFEs](https://stripe.com/resources/more/convertible-notes-vs-safes).
- **Used for:** first money in, typically before a lead investor exists.

### 1.2 Convertible note

- **What it is (Fact):** debt that converts into equity at the next financing. Principal plus accrued interest converts. [Cooley GO: convertible debt](https://www.cooleygo.com/convertible-debt/).
- **Interest:** historically 6-10%; early-stage notes more often carry about 4%, because interest acts as an extra discount. Zero interest can create accounting and tax issues. [Cooley GO](https://www.cooleygo.com/convertible-debt/).
- **Maturity:** a repayment date; repayment is often impractical, so extension or an investor election between repayment and conversion is common. Practitioner guides often cite 18-24 months (Estimate; sourced only to a startup legal guide seen in search, not opened).
- **Discount and cap:** discount typically 15-25% off the new investors' price; cap and discount usually apply "in the alternative". A qualified-financing floor is usually 1-2x the principal. [Cooley GO](https://www.cooleygo.com/convertible-debt/).
- **Founder pros:** structure some investors expect; can suit a round expected soon. **Cons:** interest raises the converting amount, maturity creates timing pressure, balance-sheet debt and tracking work. A steep discount into preferred stock can create a liquidation-preference windfall. [Stripe](https://stripe.com/resources/more/convertible-notes-vs-safes); [Cooley GO](https://www.cooleygo.com/convertible-debt/).
- **Used for:** mostly bridges and extensions today; Carta showed notes at about 7% of pre-seed rounds in Q1 2026 (secondary relay, see [Carta pre-seed data](https://carta.com/data/linkedin-safes-won-battle-convertible-notes/)).

### 1.3 Priced equity round (preferred stock)

- **What it is (Fact):** investors buy a new series of preferred stock at a negotiated price per share, with a full set of rights (see section 2). Standard US documents are the NVCA model charter, stock purchase agreement and investors' rights agreement (updated October 2025), voting agreement (June 2026) and ROFR/co-sale agreement (April 2026). [NVCA model legal documents](https://nvca.org/model-legal-documents/).
- **Founder pros:** a clear price, defined rights, no overhang of unconverted instruments. **Cons:** more legal cost and time (section 5), a board and veto rights from day one, and valuation is fixed in negotiation.
- **Used for:** seed (when a lead sets terms) and everything later.

### 1.4 Regional equivalents (only what I could source)

- **UK ASA (advance subscription agreement):** investor pays now, shares issue later on the earliest of a qualifying round, a longstop date, a sale or insolvency. It is not debt and not repayable; typical terms are a discount (20% is a common example) and a valuation ceiling. A longstop of 6-12 months is usual, but HMRC guidance for SEIS/EIS expects no more than 6 months. [Ashfords: ASA](https://www.ashfords.co.uk/expertise/solutions/business-scale-up-hub/investment-faqs/what-is-an-asa-advance-subscription-agreement) (undated page, copyright 2026).
- **Other Europe (not independently verified):** search results describe France's BSA-AIR (a warrant-based SAFE analogue), Sweden's WISE, Norway's SLIP, and Finnish law-firm commentary that SAFEs fit Finnish law poorly. These come from search summaries and commercial sites, so treat them as leads only; see [Castren & Snellman on Finland](https://www.castren.fi/safe-financing-explained-why-its-complicated-under-finnish-law/) and [Hectelion on BSA-AIR](https://www.hectelion.com/en-us/publications/safe-vs-bsa-air-seed-fundraising). Convertible loans remain common in Europe (Seedblink, a commercial source).

**So what for a solo founder:** default to a post-money SAFE with a cap for first money in the US; in the UK ask a lawyer about an ASA vs a SAFE; keep a running spreadsheet of every SAFE's cap so you know your real ownership before the priced round.

## 2. Priced-round terms a first-time founder must understand

- **Pre- vs post-money (Fact, definitional):** post-money = pre-money + new cash. The investor's percentage = new cash / post-money. Fully diluted share counts (including pool and converting instruments) should be used when computing price per share.
- **Option pool and the "pool shuffle":** investors often require a post-round unallocated pool, counted inside the pre-money, so only existing holders fund it. The classic example: $2M at $8M pre with a 20%-of-post pool gives a $1.00 price (not $1.33) and an effective pre-money of $6M; a smaller pool tied to a 12-month hiring plan lifts it to $7M. [Venture Hacks, 2007](https://venturehacks.com/option-pool-shuffle) (old, but arithmetic unchanged). Cooley GO also flags that pool placement in the fully diluted pre-money drives dilution. [Cooley GO: negotiating term sheets](https://www.cooleygo.com/negotiating-term-sheets/).
- **Pool size data (Estimate):** Carta analyses put the median post-seed employee pool at about 11.8-14% depending on the post and sample. [Carta: employee option pool size](https://carta.com/data/newsletter-employee-option-pool-size/); [Carta: pool by stage](https://carta.com/data/linkedin-employee-option-pool-by-company-stage/) (search snippets; which post carries which figure is unconfirmed).
- **Liquidation preference:** 1x non-participating is the norm. In Cooley's Q2 2026 sample (166 financings, not the whole market) 96.4% of deals were non-participating and 95.8% had a 1x preference. [Cooley Q2 2026](https://www.cooley.com/news/insight/2026/2026-08-17-q2-2026-venture-financing-report). Canada's 2025 data: 1x in 94.6%, senior ranking in 20.4% (25.6% in 2024), participating in 3.2% (6.9% average of the prior four years); the same page quotes Wilson Sonsini US figures of about 21% senior and about 5% participating. [Osler 2025 Deal Points](https://www.osler.com/en/insights/reports/2025-deal-points-report-venture-capital-financings/financing-terms-intelligence-preferred-share-financings/). Fenwick says greater-than-1x and participating terms "remained rare" in Q1 2026. [Fenwick Q1 2026](https://fenwick.com/insights/publication/q1-2026-venture-beacon-key-vc-market-trends) (published June 2026).
- **Anti-dilution:** broad-based weighted average was in 100% of 2025 Canadian financings, and the same source quotes 100% for US financings (Wilson Sonsini). [Osler](https://www.osler.com/en/insights/reports/2025-deal-points-report-venture-capital-financings/financing-terms-intelligence-preferred-share-financings/). Cooley GO says to move on if it is broad-based and to talk to your lawyer about a full ratchet. [Cooley GO](https://www.cooleygo.com/negotiating-term-sheets/). A Chambers guide chapter (search snippet) says about 80% of deals with protection use weighted average and about 2% full ratchet; sample and region unclear. [Chambers VC 2025](https://gpg-pdf.chambers.com/view/998044102/11/).
- **Board composition:** Cooley GO describes three seats after an initial financing (one investor, two common) as typical. [Cooley GO](https://www.cooleygo.com/negotiating-term-sheets/). Canadian 2025 data show average board size 4.9 across all rounds and common directors first losing their majority after Series A. [Osler](https://www.osler.com/en/insights/reports/2025-deal-points-report-venture-capital-financings/financing-terms-intelligence-preferred-share-financings/).
- **Protective provisions:** investor vetoes over listed actions (sales, new share series, charter changes, debt and others). Watch wording: a veto may reach any new series or charter amendment, not just financings. [Cooley GO](https://www.cooleygo.com/negotiating-term-sheets/). I could not verify a prevalence figure (see Open questions).
- **Founder vesting:** the questions to settle are vesting start date, acceleration on termination without cause, and double-trigger acceleration on a change of control. [Cooley GO](https://www.cooleygo.com/negotiating-term-sheets/). Founders on restricted stock generally have 30 days from grant to file a Section 83(b) election, a deadline that cannot be cured. [Cooley GO: 83(b)](https://www.cooleygo.com/section-83b-election-file-one).
- **Drag/tag:** in Canada 2025, 77.1% of drag-alongs used a single preferred-holder threshold and 22.9% multiple thresholds (9.5% in 2024). [Osler](https://www.osler.com/en/insights/reports/2025-deal-points-report-venture-capital-financings/financing-terms-intelligence-preferred-share-financings/). Cooley GO calls ROFR and co-sale/tag-along "customary". [Cooley GO](https://www.cooleygo.com/negotiating-term-sheets/).
- **Information rights:** largely boilerplate; not worth heavy negotiation unless out of market. [Cooley GO](https://www.cooleygo.com/negotiating-term-sheets/).
- **Pro rata:** in priced rounds usually sits in the investors' rights agreement for larger investors (Inference; confirm in the NVCA IRA via [NVCA model documents](https://nvca.org/model-legal-documents/)).
- **Redemption rights:** rare: 4% (Wilson Sonsini), 3.2% (Cooley) and 7.4% in Canada 2025. [Osler](https://www.osler.com/en/insights/reports/2025-deal-points-report-venture-capital-financings/financing-terms-intelligence-preferred-share-financings/).
- **Market direction:** Cooley's Q2 2026 sample had 83.6% up rounds, 4.3% flat and 12.1% down (Q1 2026: 86.6%, 2.5%, 10.9%). [Cooley Q2 2026](https://www.cooley.com/news/insight/2026/2026-08-17-q2-2026-venture-financing-report). Law-firm samples skew to firm clients and larger deals.

**So what for a solo founder:** spend your negotiating capital on valuation, pool size/placement, board control and protective-provision scope; do not burn goodwill on 1x non-participating or broad-based anti-dilution, which are the market default.

## 3. Valuation and round-size benchmarks (pre-seed and seed)

Figures differ by definition (pre- vs post-money, priced-only vs SAFE caps), platform and period. Do not anchor on one number.

| Metric | Figure | Source and date |
|---|---|---|
| US median seed pre-money | $16M (2025) | [NVCA 2026 Yearbook](https://nvca.org/?p=124853) (PitchBook data to 12/31/2025) |
| US median seed pre-money, Q1 2026 | $18.4M (AI $18.7M, non-AI $18.0M) | [PitchBook-NVCA Q1 2026](https://nvca.org/wp-content/uploads/2026/04/Q1-2026-PitchBook-NVCA-Venture-Monitor.pdf) (PDF unreadable here; figure via search summary, treat as secondary) |
| US median seed round | about $3M; quartiles $1M and $5.6M (2025) | [Crunchbase News, 2026-05-26](https://news.crunchbase.com/seed/data-bigger-deals-longer-seriesa-2026/) |
| Seed pre-money by region, SaaS (Carta) | Bay Area $33.3M, New York $24.5M, rest of US $12.7M (Q1 2026) | [Carta](https://carta.com/data/seed-valuations-saas-sf-nyc/) (search snippet; page not openable) |
| Pre-seed SAFE post-money caps | $7.5M (under $250k), $10M ($250-500k) in Q2 2025; $12.5M for $1-1.9M raises (Oct 2024-Mar 2025) | [Carta pre-seed benchmarks](https://carta.com/data/linkedin-preseed-safe-valuation-benchmarks-q4/) (over a year old; snippet) |
| Large pre-seed SAFEs (over $2.5M) | median cap $35M, 75th percentile near $60M (Q2 2026) | [Carta SAFE caps Q2 2026](https://carta.com/data/safe-valuation-caps-q2-2026/) (snippet) |

- **Conflicts to note:** the $16M (2025) vs $18.4M (Q1 2026) gap is mostly period and data-vintage. Secondary aggregators quote a Carta-attributed median seed of $3.8M at $14M pre and a $24M post-money median; I could not trace these to a Carta page (Open questions).
- **Caveats (Fact/Inference):** (a) **Survivorship and disclosure:** medians cover rounds that closed and were reported; failed raises are invisible. (b) **Skew:** 14 seed or pre-seed deals exceeded $100M in 2025 and AI took 65.4% of US deal value, which inflates upper tails. [NVCA 2026 Yearbook](https://nvca.org/?p=124853). (c) **Geography and sector:** the Carta metro split above shows a 2.6x spread for SaaS seed. (d) **Platform bias:** Carta covers its own customers, Cooley and Fenwick their own clients. (e) **Stage labels** vary; Crunchbase says its newest quarters are preliminary because early deals appear late.
- **Fast-moving flag:** all figures above are 2025-2026 and can change materially within a year.

**So what for a solo founder:** use these as a sanity range (for a US seed, roughly $12M to $33M pre-money depending on region and sector), then anchor on comparable deals your own investors and advisers have actually seen.

## 4. Dilution math

### 4.1 Typical dilution (sourced)

- Seed: median about 19.5% across 5,118 priced seed rounds; Carta describes seed and Series A as "20%", with median drift to 19% (seed) and 18% (Series A) in 2025; under 10% of 2025 software seed rounds sold 30% or more. [Carta: seed dilution](https://carta.com/data/linkedin-20-percent-dilution-seed-durable/); [Carta: under 30%](https://carta.com/data/linkedin-seed-dilution-30-percent-under-10/); [Carta: dilution not rising](https://carta.com/data/linkedin-dilution-not-rising-vc-data/) (search snippets; 2025 data).
- Series A: 17.9% median in Q1 2025 vs 20.9% a year earlier. [Carta Q1 2025 round data](https://carta.com/data/linkedin-q1-2025-round-data-cheatsheet/) (snippet; older than a year). Healthcare ran higher (seed 20%, Series A 21.8%, Q1 2025). [Carta healthcare](https://carta.com/sg/en/data/healthcare-sector-dilution-q1-2025/).

### 4.2 Formulae

Let F = founder shares, P0 = existing pool, I = SAFE investment, C = post-money cap, N = new money, V = pre-money, p = target unallocated pool as a share of post-round fully diluted shares.

1. Company capitalization before the SAFE: K = F + P0.
2. SAFE ownership = I / C, so SAFE shares S = K x (I/C) / (1 - I/C). Cap price = C / (K + S).
3. Priced-round investor share x = N / (V + N).
4. Post-round fully diluted shares T = (F + S) / (1 - x - p) when the pool is topped up to exactly p (founders plus SAFE shares are the only fixed holders).
5. Round price = V / (T - investor shares). The SAFE converts at the lower of cap price and round price (or discounted price if any).
6. Effective pre-money to existing holders = V - (pool top-up shares x round price).

### 4.3 Worked example (ILLUSTRATIVE, made-up numbers)

Assumptions: founders hold 8,000,000 shares; existing pool 1,000,000; a $500,000 post-money SAFE at a $5,000,000 cap with no discount; then a $2,000,000 priced round at $10,000,000 pre-money, with investors requiring a 10% post-round unallocated pool created pre-money.

| Step | Calculation | Result |
|---|---|---|
| Capitalization before SAFE | 8,000,000 + 1,000,000 | 9,000,000 |
| SAFE ownership | 500,000 / 5,000,000 | 10% |
| SAFE shares | 9,000,000 x 0.10 / 0.90 | 1,000,000 |
| Cap price | 5,000,000 / 10,000,000 | $0.50 |
| Check | 1,000,000 / 10,000,000 | 10% (OK) |
| Investor share | 2,000,000 / 12,000,000 | 16.667% |
| Post-round FD shares | 9,000,000 / (1 - 0.16667 - 0.10) | about 12,272,727 |
| Investor shares | 12,272,727 x 0.16667 | about 2,045,455 |
| Pool after top-up | 12,272,727 x 0.10 | about 1,227,273 (top-up about 227,273) |
| Round price | 10,000,000 / (12,272,727 - 2,045,455) | about $0.9778 |
| Check | 2,045,455 x 0.9778 | about $2,000,000 (OK) |

Post-round ownership: founders 8,000,000 / 12,272,727 = 65.19%; SAFE holder 8.15%; pool 10.00%; new investor 16.67% (sum 100%). Founders were 80.0% (8,000,000 / 10,000,000) just after the SAFE, so the priced round cost them about 14.8 percentage points. The SAFE shares convert at $0.50 versus a $0.9778 round price, so $500,000 becomes about $977,778 of stock at round price (about 1.96x).

Pool-shuffle effect: the top-up is worth about 227,273 x $0.9778 = $222,222, so the effective pre-money for existing holders is about $9.78M, not $10M. With no top-up (pool stays at 1,000,000) the total would be 12,000,000 shares at $1.00 and founders would hold 66.67%, so the top-up costs founders about 1.5 percentage points here. (All arithmetic recomputed with a script; these are not market data.)

**So what for a solo founder:** build this model before you sign any SAFE; the combination of stacked post-money SAFEs and a pre-money pool top-up is where first-time founders are most often surprised.

## 5. Process and timeline

1. **Preparation (Estimate: 2-6 weeks):** decide the amount and runway (use the `unit-economics-model` skill), clean the cap table, confirm entity type and IP assignment, build a short deck and data room, pick a lawyer. Fix your SAFE/note ledger first.
2. **Pipeline:** build a target list segmented by stage fit, check size and geography; get warm introductions where possible (`founder-outreach-drafts` skill).
3. **First meetings and follow-ups (Estimate: 4-10 weeks):** run meetings in a compressed window so interest overlaps; send requested data promptly. Secondary sources attribute a median of 56 days from first meeting to funds to Carta (not verified, see Open questions).
4. **Term sheet:** mostly non-binding except exclusivity (no-shop) and confidentiality. Cooley GO says exclusivity of 30-45 days is usually enough. [Cooley GO](https://www.cooleygo.com/negotiating-term-sheets/).
5. **Diligence and legal docs (Estimate: 2-4 weeks from term sheet to close):** one startup-law guide gives 2-4 weeks for term-sheet negotiation through definitive documents and closing; treat as a floor for simple deals. Expect cap table, IP, contracts, privacy and employment checks (`data-protection-readiness` skill).
6. **Closing and funds:** signatures, wires, board consents, updated cap table. For SAFEs this can be days.
7. **Time between rounds (Fact):** US seed-to-Series A has stretched to over two years since 2023; the graduation rate for 2023 seed cohorts is 24% and 16% for 2024 (cohorts still maturing). [Crunchbase News, 2026-05-26](https://news.crunchbase.com/seed/data-bigger-deals-longer-seriesa-2026/). Carta data via SaaStr: in Q3 2025 23% raised Series A within 1.5-2 years and 39% took three or more, versus 41% and 19% in Q3 2019 (the article's own wording is internally inconsistent). [SaaStr, Oct 2025](https://www.saastr.com/your-seed-round-now-needs-to-last-3-years-what-3365-startups-tell-us-about-the-new-series-a-timeline).

### 5.1 Legal cost ranges

- Pilot's data (9,059 transactions, published Feb 2024, so older than two years): average legal fees just under $10,000 at pre-seed, about $17,000 at seed and nearly $40,000 at Series A. [Pilot](https://pilot.com/insights/how-much-does-it-cost-to-raise-a-round). Methodology is not described.
- Other guides quote roughly $3-7k for SAFE rounds and $15-25k for priced seed; I could not trace these to primary data (Open questions). Costs vary by firm and city.

### 5.2 Cap table hygiene (Inference, practitioner norm)

Keep one source of truth (cap table tool or lawyer-maintained ledger); record every SAFE with cap, discount and MFN; issue founder stock with vesting and a timely 83(b) election where applicable; avoid informal equity promises; keep board and stockholder consents on file.

### 5.3 Employee option basics

- Private companies in the US typically obtain a 409A valuation before the first option grant; options priced below fair market value risk a 20% federal penalty plus interest on the employee, per practitioner guides. [Promise Legal](https://blog.promise.legal/startup-central/startup-stock-option-plan-409a-valuation/) (search snippet; not primary).
- ISOs are limited by the $100,000 annual first-exercisable rule under IRC section 422(d); excess is treated as NSOs. Verify with a tax adviser (same source).
- Typical vesting is four years with a one-year cliff (Inference; common practitioner convention, not sourced here).

### 5.4 Jurisdiction notes

- **US/Delaware:** US VCs often require non-US companies to flip into a Delaware corporation as a condition of investment (a custom, not law). A flip should be done early and needs all holders to participate; tax outcomes depend on holders' jurisdictions. [MoFo, 2023-06-28](https://mofo.com/resources/insights/230628-company-that-was-formed-in-another-country) (older than two years). One UK platform argues a flip is often unnecessary, saying investors mainly insist at very early stages or through accelerators such as YC or Techstars, and that a flip after SEIS/EIS investment needs HMRC pre-approval. [SeedLegals](https://seedlegals.com/resources/should-you-do-a-delaware-flip) (commercial source; undated).
- **UK SEIS/EIS:** gov.uk guidance (last updated 25 May 2023) states SEIS limits of GBP 250,000 per company, gross assets of GBP 350,000 or less, fewer than 25 full-time-equivalent employees, and trade not older than three years; advance assurance from HMRC is optional. [GOV.UK: SEIS](https://www.gov.uk/guidance/venture-capital-schemes-apply-to-use-the-seed-enterprise-investment-scheme). BDO (secondary) reports SEIS income-tax relief of 50% up to GBP 200,000 per investor per year, and EIS company limits raised from 6 April 2026 (GBP 10M annual and GBP 24M lifetime for standard companies; GBP 20M and GBP 40M for knowledge-intensive). [BDO guide](https://www.bdo.co.uk/en-gb/insights/tax/corporate-tax/enterprise-investment-scheme-guide-for-companies). Further technical changes take effect 6 April 2027. [GOV.UK: changes](https://www.gov.uk/government/publications/changes-to-the-seed-enterprise-investment-scheme-enterprise-investment-scheme-and-venture-capital-trusts/changes-to-venture-capital-schemes). Instrument design matters: debt-like instruments may jeopardize relief, which is why ASAs exist. [Ashfords](https://www.ashfords.co.uk/expertise/solutions/business-scale-up-hub/investment-faqs/what-is-an-asa-advance-subscription-agreement).
- **Other regions:** Europe has local SAFE analogues (section 1.4); I did not source other regions.

**So what for a solo founder:** budget a few months from first outreach to money in the bank (Estimate) and tens of thousands of dollars at most for legal work at seed (Pilot, Feb 2024); decide your entity and jurisdiction before the first investor conversation, not after the term sheet.

## 6. What to hand to professionals

This playbook is not legal or tax advice. Hand these to a startup lawyer and an accountant:

- **Startup lawyer:** entity formation or Delaware flip; drafting or reviewing SAFE/note/ASA and the priced-round documents; reviewing the term sheet; founder stock, vesting and the 83(b) timing; option plan and board consents; securities-law exemptions and filings; IP assignment; diligence responses.
- **Accountant/tax adviser:** 409A valuation and option tax treatment; cap table and financial statements for diligence; SEIS/EIS or QSBS-type relief eligibility; cross-border tax of a flip; bookkeeping of SAFEs/notes.
- **Questions to ask:** What is your fixed fee and what is out of scope? What is my exact ownership after each SAFE converts? Is the pool inside the pre-money, and what pool do we actually need for 12-18 months of hiring? Which protective provisions go beyond the model documents? Does the instrument preserve SEIS/EIS eligibility? What must I file, and by when?

**So what for a solo founder:** get fixed-fee quotes, ask for the cap-table model in writing, and never sign a document you could not explain to a friend.

## 7. In-repo skills

- `unit-economics-model` for runway and how much to raise.
- `data-protection-readiness` for diligence on privacy and data handling.
- `founder-outreach-drafts` for investor outreach and follow-ups.

## Checklist

- [ ] Ledger of every SAFE/note (amount, cap, discount, MFN, date, signed/funded).
- [ ] Cap-table model that converts all SAFEs at a hypothetical priced round, with pool top-up.
- [ ] Entity and jurisdiction decision (Delaware, UK SEIS/EIS) confirmed with a lawyer.
- [ ] Founder stock issued with vesting; 83(b) filed within 30 days if applicable.
- [ ] Target raise, runway and use of funds documented (`unit-economics-model`).
- [ ] Data room and privacy basics ready (`data-protection-readiness`).
- [ ] Investor pipeline with warm intros and a compressed meeting window (`founder-outreach-drafts`).
- [ ] Term sheet reviewed for pool size/placement, board, protective provisions, vesting acceleration, exclusivity length.
- [ ] Fixed-fee quote and scope from counsel; 409A valuation before the first option grant.

## Open questions

- Carta's own Q1-Q2 2026 pre-seed and seed medians (round size, cap, dilution) could not be opened (HTTP 403); several figures here are search snippets or secondary relays. Verify on carta.com.
- PitchBook-NVCA Q1 2026 PDF was unreadable by the fetch tool; the $18.4M median and about $3.0M median deal size come from a search summary.
- The $3.8M median at $14M pre and the $24M post-money seed median attributed to Carta by aggregators were not traced.
- Prevalence of protective provisions (one blog cites over 90% from Cooley Q2 2025) and Fenwick/Wilson Sonsini US anti-dilution tables were not verified.
- Whether YC still offers a combined cap-and-discount post-money form: the YC page I read lists three forms (cap, discount, MFN); secondary sites disagree.
- Convertible-note maturity norms (18-24 months) lack a primary source here.
- The 56-day first-meeting-to-funds Carta figure and the DocSend closing-time statistics are secondary only.
- Legal-cost ranges for SAFE ($3-7k) and priced seed ($15-25k) lack primary data; Pilot's figures are from February 2024.
- SEIS current limits and investor relief rates should be re-checked on gov.uk (guidance page dated 2023; BDO is secondary).
- European instrument details (BSA-AIR, WISE, SLIP) and non-US/UK jurisdictions were not verified against primary law or regulator sources.

## Sources

All accessed 2026-11-11. "Snippet" means the page itself returned an error to the fetch tool and the figure came from a search-result summary.

1. [Y Combinator: documents (SAFE)](https://www.ycombinator.com/documents)
2. [Torys: pre-money vs post-money SAFE (2021)](https://www.torys.com/insights/publications/2021/02/pre-money-versus-post-money-safe)
3. [Cooley GO: convertible debt](https://www.cooleygo.com/convertible-debt/)
4. [Stripe: convertible notes vs SAFEs](https://stripe.com/resources/more/convertible-notes-vs-safes)
5. [Carta: State of Pre-Seed Q2 2026](https://carta.com/data/state-of-pre-seed-q2-2026/) (snippet)
6. [Carta: SAFE valuation caps Q2 2026](https://carta.com/data/safe-valuation-caps-q2-2026/) (snippet)
7. [Carta: SAFEs vs notes](https://carta.com/data/linkedin-safes-won-battle-convertible-notes/) (snippet)
8. [Ashfords: what is an ASA](https://www.ashfords.co.uk/expertise/solutions/business-scale-up-hub/investment-faqs/what-is-an-asa-advance-subscription-agreement)
9. [Castren & Snellman: SAFE under Finnish law](https://www.castren.fi/safe-financing-explained-why-its-complicated-under-finnish-law/) (snippet)
10. [Hectelion: SAFE vs BSA-AIR](https://www.hectelion.com/en-us/publications/safe-vs-bsa-air-seed-fundraising) (snippet)
11. [NVCA model legal documents](https://nvca.org/model-legal-documents/)
12. [Cooley Q2 2026 Venture Financing Report](https://www.cooley.com/news/insight/2026/2026-08-17-q2-2026-venture-financing-report)
13. [Osler 2025 Deal Points Report](https://www.osler.com/en/insights/reports/2025-deal-points-report-venture-capital-financings/financing-terms-intelligence-preferred-share-financings/)
14. [Fenwick Q1 2026 Venture Beacon](https://fenwick.com/insights/publication/q1-2026-venture-beacon-key-vc-market-trends)
15. [Cooley GO: negotiating term sheets](https://www.cooleygo.com/negotiating-term-sheets/)
16. [Cooley GO: 83(b) election](https://www.cooleygo.com/section-83b-election-file-one)
17. [Chambers: Venture Capital 2025](https://gpg-pdf.chambers.com/view/998044102/11/) (snippet)
18. [Venture Hacks: option pool shuffle (2007)](https://venturehacks.com/option-pool-shuffle)
19. [Carta: employee option pool size](https://carta.com/data/newsletter-employee-option-pool-size/) (snippet)
20. [Carta: option pool by company stage](https://carta.com/data/linkedin-employee-option-pool-by-company-stage/) (snippet)
21. [NVCA 2026 Yearbook](https://nvca.org/?p=124853)
22. [PitchBook-NVCA Venture Monitor Q1 2026](https://nvca.org/wp-content/uploads/2026/04/Q1-2026-PitchBook-NVCA-Venture-Monitor.pdf) (unreadable; figure via search summary)
23. [Crunchbase News: seed deals bigger, Series A odds fall (2026-05-26)](https://news.crunchbase.com/seed/data-bigger-deals-longer-seriesa-2026/)
24. [Carta: seed valuations SF and NYC](https://carta.com/data/seed-valuations-saas-sf-nyc/) (snippet)
25. [Carta: pre-seed SAFE benchmarks](https://carta.com/data/linkedin-preseed-safe-valuation-benchmarks-q4/) (snippet)
26. [Carta: 20 percent seed dilution](https://carta.com/data/linkedin-20-percent-dilution-seed-durable/) (snippet)
27. [Carta: under 10 percent of seed rounds sell 30 percent](https://carta.com/data/linkedin-seed-dilution-30-percent-under-10/) (snippet)
28. [Carta: dilution not rising](https://carta.com/data/linkedin-dilution-not-rising-vc-data/) (snippet)
29. [Carta: Q1 2025 round data cheatsheet](https://carta.com/data/linkedin-q1-2025-round-data-cheatsheet/) (snippet)
30. [Carta: healthcare dilution Q1 2025](https://carta.com/sg/en/data/healthcare-sector-dilution-q1-2025/) (snippet)
31. [Pilot: cost to raise a round (Feb 2024)](https://pilot.com/insights/how-much-does-it-cost-to-raise-a-round)
32. [SaaStr on Carta time-to-Series A (Oct 2025)](https://www.saastr.com/your-seed-round-now-needs-to-last-3-years-what-3365-startups-tell-us-about-the-new-series-a-timeline)
33. [Promise Legal: stock options and 409A](https://blog.promise.legal/startup-central/startup-stock-option-plan-409a-valuation/) (snippet)
34. [MoFo: non-US company and Delaware (2023-06-28)](https://mofo.com/resources/insights/230628-company-that-was-formed-in-another-country)
35. [SeedLegals: should you do a Delaware flip](https://seedlegals.com/resources/should-you-do-a-delaware-flip)
36. [GOV.UK: SEIS guidance](https://www.gov.uk/guidance/venture-capital-schemes-apply-to-use-the-seed-enterprise-investment-scheme)
37. [GOV.UK: changes to venture capital schemes](https://www.gov.uk/government/publications/changes-to-the-seed-enterprise-investment-scheme-enterprise-investment-scheme-and-venture-capital-trusts/changes-to-venture-capital-schemes)
38. [BDO: EIS and VCT guide for companies](https://www.bdo.co.uk/en-gb/insights/tax/corporate-tax/enterprise-investment-scheme-guide-for-companies) (snippet)
