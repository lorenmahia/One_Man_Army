# Go-to-Market and First Customers: A Solo Founder Playbook

> Last verified: 2026-11-11. Research and planning support only; not legal, tax, investment or financial advice.

**Summary**

- **Pick one narrow beachhead and one channel.** Moore's test is a segment "big enough to matter, small enough to lead" ([Lenny's: Moore on beachheads, Jan 2024](https://www.lennysnewsletter.com/p/geoffrey-moore-on-finding-your-beachhead)); most consumer companies used one channel, never more than three, for their first users ([Lenny's: first 1,000 users, May 2020](https://www.lennysnewsletter.com/p/how-the-biggest-consumer-apps-got)).
- **Position against what buyers use today**, including spreadsheets and doing nothing, before you describe features ([Heinz Marketing on Dunford, secondary summary](https://www.heinzmarketing.com/blog/five-components-of-effective-positioning-an-obviously-awesome-book-summary-part-2/)).
- **Sell the first 10 yourself, by hand.** Graham's advice is to recruit users manually and track weekly growth ([Graham, 2013](https://paulgraham.com/ds.html)). Automate only after you know what works.
- **Benchmarks are noisy and vendor-biased.** Trial and freemium conversion, CAC payback and cold-email reply rates vary several-fold between sources. Use them as sanity ranges, never as targets.
- **Decide with a gate, not a mood.** Use retention cohorts, a "very disappointed" survey, and cash payback to choose go, adjust or stop (section 7).

---

## 1. Choosing the first market

**ICP (ideal customer profile).** Write one sentence naming who buys, what triggers the purchase, and who pays. Add 3 to 5 observable filters you can use to build a list (role, company size, tool in use, geography, trigger event). **Inference:** if you cannot build a list of 100 named targets from your filters, the segment is too vague to sell into.

**Beachhead selection.** Moore's "Crossing the Chasm" idea is to dominate one niche, then expand to adjacent segments ("bowling alley"). In a 2024 interview he gives the test as a segment that is big enough to matter, small enough to lead, and a good fit with your core strengths ([Lenny's, Jan 2024](https://www.lennysnewsletter.com/p/geoffrey-moore-on-finding-your-beachhead); the page names but does not detail the bowling-alley playbook). Practical scoring columns: pain intensity, ability to reach them cheaply, ability to serve them with today's product, presence of reference-able peers, willingness to pay.

**Jobs-to-be-done (JTBD).** Phrase the need as "when [situation], I want to [progress], so I can [outcome]". Ask for the last time it happened and what they did. Use the in-repo skill `customer-discovery-interviews` for the interview scripts.

**Honest bottom-up sizing.**

1. Count reachable accounts or people in the beachhead from a real list (directory, association, app store category, LinkedIn filter).
2. Multiply by realistic price and by the share you can contact and close in 12 months.
3. Compare with the revenue you need. **Estimate** only; label every input.

Avoid top-down "1% of a huge market" arguments; they hide the reachability question.

**Frameworks compared.**

| Framework | Core move | Best for | Limit |
|---|---|---|---|
| Dunford positioning | Start from competitive alternatives; derive value and best-fit customers | Products that exist and are not "getting it" | Secondary summaries only used here; read the book |
| Moore beachhead | One niche, whole product, references | B2B and tech products with pragmatic buyers | Written for a different era; the principle (focus) still holds |
| YC / Graham | Recruit by hand, pick enthusiastic users, track weekly growth | Pre-product-market-fit founders | Not a sizing method ([Graham, 2013](https://paulgraham.com/ds.html)) |
| a16z (Casado, via aggregator) | Close the first 10 to 20 deals personally; few aligned customers | B2B early sales | Seen only as an aggregator summary, unverified ([Echai summary, snippet](https://echai.ventures/startingup/path/get-your-first-customers)) |

**Reality check.** Graham advises launching somewhat broadly, then finding the most enthusiastic users and seeking more like them; Pinterest recruited at a design bloggers' conference ([Graham, 2013](https://paulgraham.com/ds.html)). Moore advises choosing first. **Inference:** the two are compatible: pick a provisional beachhead, then let early enthusiasm confirm or move it.

**So what for a solo founder:** write a one-line ICP and a list of 100 named prospects before you build more product.

---

## 2. Positioning and messaging

**Dunford's components (as summarised by a third party).** Competitive alternatives; unique attributes; value (with proof); target market characteristics; market category; and optionally relevant trends. Alternatives are often not products: a spreadsheet, an intern, or existing budget priorities ([Heinz Marketing, secondary summary](https://www.heinzmarketing.com/blog/five-components-of-effective-positioning-an-obviously-awesome-book-summary-part-2/)). The summary does not mention "do nothing" explicitly; treating it as an alternative is our **Inference**.

**One-page positioning canvas** (fill in this order):

1. Alternatives customers use today (include: spreadsheet, manual process, agency, WhatsApp groups, do nothing).
2. What you do that those alternatives cannot.
3. The outcome that difference creates, in the customer's words and numbers.
4. Who cares most (your ICP).
5. The category label that makes (1) to (4) obvious.
6. Proof: one named customer, one metric, one quote (with permission).

**Value-proposition tests.**

- Five-second test: can a target buyer repeat what you do after reading the headline?
- Interview test: after a 30-minute discovery call, do they describe the problem in your words?
- Commitment test: will they give time, data, an introduction or money? Fitzpatrick's "Mom Test" treats compliments, vague fluff and feature requests as bad data and a concrete next step as the real signal (secondary summaries only: [Mom Test book report](https://mtlynch.io/book-reports/the-mom-test/), search snippet).
- Switching-cost test: what must the buyer stop doing or migrate to adopt you?

**Proof and case studies.** Start with a single before-and-after number agreed with the customer in writing. Moore's "reference-based marketing" idea (secondary) holds that pragmatic buyers want peers like themselves; collect references inside the beachhead first.

**So what for a solo founder:** your first copy should name the alternative you replace; a case study from one customer in the beachhead beats ten generic claims.

---

## 3. Pricing basics

**Three anchors.**

- **Value-based:** price as a fraction of the measurable gain or cost avoided. Best default, but requires you to learn the customer's numbers.
- **Cost-plus:** floor only. Use to find the price below which you lose money (link to `unit-economics-model`).
- **Competitor-based:** a reference point, not a strategy; you may be mispositioned if you copy it.

**Packaging.** Start with one plan, or at most three tiers. Differentiate tiers by value metric (seats, usage, outcomes), not by arbitrary feature gates. Raise prices for early customers' successors, and grandfather the first few only with a stated end date.

**Trial vs freemium vs paid pilot.** ChartMogul and ProductLed's Feb 2026 survey (200 self-reported responses, skewed to small companies, so **vendor-adjacent and low-n**) reports:

| Model | "Good" | "Great" | Notes |
|---|---|---|---|
| Free trial | 4-6% | 10-15% | Card required: good 25-35%, great 50-60% |
| Freemium | 3-5% | 8-12% | Ungated freemium good 7-9% |
| Reverse trial | 4-6% | 8-12% | Small sample; difference not significant |

Source: [ChartMogul/ProductLed SaaS Conversion Report, Feb 2026](https://chartmogul.com/reports/saas-conversion-report/). Median free-to-paid is 8% but very few products sit there. Per 1,000 visitors the report estimates freemium yields about 5 paying customers and a no-card trial 3.6, so higher trial conversion disappears once signup rates are counted. Other aggregators report different numbers (for example, 15-30% B2B trial conversion, 2.6-5.8% freemium), but they cite each other and have unclear primary sources (search snippets only). **Conflict, shown as a range:** no-card trial conversion 8.9% to 18.2% by source; treat both as vendor claims.

**For a solo founder, a paid pilot is usually better than a free tier.** **Inference:** free users generate support load and noisy data; a paid or deposit-backed pilot filters for real pain. Pilot structure: fixed 30 to 90 days, written success metric, price credited to the first contract if it succeeds.

**Price testing with few customers.**

- Ask for a price in every discovery call and watch the reaction; vary the number between calls (for example, three prices across 15 calls).
- Van Westendorp finds a range; Gabor-Granger picks a point inside it. Sources disagree on sample sizes: about 30 as a floor (vendor blog) to 100-200 for Van Westendorp (skill page); with fewer than about 15 customers, conversations beat curves ([Koji blog, vendor, snippet](https://www.koji.so/blog/price-testing-methods-for-startups-compared)).
- A deposit or signed letter of intent tells you more than stated willingness to pay.
- Raise the price until you lose about one in five deals you would otherwise win. **Inference/heuristic, unsourced.**

**Link to unit economics.** Price must cover cost to serve plus acquisition: at a given price and gross margin, how many months to repay CAC? Run it in `unit-economics-model` before choosing a channel.

**So what for a solo founder:** quote a real price on call one, prefer paid pilots to free tiers, and let three different quotes teach you before you build a pricing page.

---

## 4. Channels by business type

Benchmarks below come mostly from vendor blogs. Treat as order-of-magnitude. None is a promise.

| Channel | Works when | Early metrics (sourced) | Cost and time | Failure modes |
|---|---|---|---|---|
| Founder-led sales | B2B, high price, unclear category | Casado (via aggregator) suggests the founder closes the first 10 to 20 deals ([Echai summary, snippet](https://echai.ventures/startingup/path/get-your-first-customers)) | Your time; weeks per deal | Never delegating; selling features |
| Cold outbound | Reachable named ICP | Belkins: 0.45% average reply on 7.5M emails sent in 2025, counted against sends; vendor blogs claim 3-6% ([Belkins, snippet](https://belkins.io/blog/cold-email-response-rates.md)) | Tools plus 5 to 10 hrs/week; 2 to 6 weeks to learn | Spam list, generic copy, deliverability |
| Content / SEO | Searchable problem, longer cycles | Agency benchmarks: first leads months 4 to 8; revenue attributed 9 to 15 months ([Starr Conspiracy, snippet](https://www.thestarrconspiracy.com/insights/benchmarks/b2b-seo-timeline-benchmarks-2025)) | Cheap in cash, slow | Quitting at month 3; thin content |
| Communities | Niche with active forums, groups | Lenny's: "go where users are" online and offline was a top route ([Lenny's, 2020](https://www.lennysnewsletter.com/p/how-the-biggest-consumer-apps-got)) | Time; weeks | Self-promotion bans; no trust |
| Partnerships / channels | Product fits an existing workflow or vendor | No reliable benchmark found | Long relationship build | Partner has no incentive |
| Paid acquisition | You know payback and have working conversion | CAC figures conflict ($150 to $400 vs $1,500 to $3,000 for seed SaaS, vendor blogs: [SaaS Hero, snippet](https://www.saashero.net/strategy/maxio-cac-benchmarks-b2b-saas/)) | Cash; days to test | Buying traffic before activation works |
| Product-led growth | Self-serve, fast time-to-value | See section 3 conversion ranges | Heavy product investment | No activation, free-user pile-up |
| Events | Concentrated beachhead, offline trust | Pinterest recruited at a design bloggers' event ([Graham, 2013](https://paulgraham.com/ds.html)) | Travel, time | Collecting badges, no follow-up |

**By business type.**

- **B2B SaaS:** founder-led sales and targeted outbound first; content as a slow compounding bet. Payback: sources range from 3 to 8 months (Growthspree) to under 18 months at seed (G-Squared) to 24-month medians (a Bessemer/OpenView-attributed table); all vendor-secondary ([SaaS Hero, snippet](https://www.saashero.net/strategy/maxio-cac-benchmarks-b2b-saas/)). **Flag:** large spread; do not anchor on any one.
- **B2C app:** recruit directly, go where users are, use waitlists/FOMO and press; Lenny's found no company used more than three of seven strategies ([Lenny's, 2020](https://www.lennysnewsletter.com/p/how-the-biggest-consumer-apps-got)). Older than two years on a fast-moving topic; verify current platform rules.
- **Marketplace:** nearly every company interviewed constrained geography or category first; OpenTable aimed for about 50-100 restaurants per city; Uber's launch target was over 30 drivers ([Lenny's, Nov 2019](https://www.lennysnewsletter.com/p/how-to-kickstart-and-scale-a-marketplace), older than two years). Seed the harder side by hand.
- **Local / service:** referrals, local communities, partnerships with adjacent trades, Google Business profile. No benchmark sourced; test with 20 outreach attempts.
- **Hardware:** pre-orders or deposits as demand test, crowdfunding, specialist communities, distributor partnerships. No sourced benchmark found; see Open questions.
- **Emerging-market mobile-first:** see section 8.

**So what for a solo founder:** choose the one channel where your ICP already gathers and where you can run 20 experiments in a month; ignore the rest until it fails.

---

## 5. The first 10 customers, then the first 100

**Founder-led sales process (first 10).**

1. List 100 named prospects from ICP filters. Draft messages with `founder-outreach-drafts`.
2. Send 10 to 20 per day; log replies. Warm intros first, then communities, then cold.
3. Run discovery calls (below), then a demo, then a scoped pilot or paid start.
4. After each deal, ask for two introductions.

Graham: the founder usually has to do the sales and marketing early on, and a salesperson does not replace that at first ([Graham, 2013](https://paulgraham.com/ds.html)). One founder write-up claims all ten of the first customers at a $1M ARR company were closed by the founder ([SaasClub, snippet](https://saasclub.io/playbooks/felix-hoffmann-ten-customers-founder-led-story/)); single anecdote.

**Discovery call structure (30 to 40 minutes).**

- Context: role, how they do the job today, last time the problem occurred.
- Pain: cost in time, money, risk; who else is affected; what they already tried.
- Alternatives: current tools and workarounds, including spreadsheets and doing nothing.
- Decision: who signs, budget, timeline, trigger.
- Close: concrete next step with a date. Do not pitch for the first 20 minutes. See `customer-discovery-interviews`.

**Demo and pilot.** Demo only their scenario using their data. Pilot: fixed scope, named owner on their side, weekly check-in, written success metric, price and conversion terms stated up front.

**Objection handling.** Treat objections as discovery: "too expensive" (compared with what?), "not now" (what would change that?), "we use X" (what do you wish it did?), "need approval" (who, and can I join?). Record every objection; the top three should change your positioning.

**Closing and onboarding.** Ask directly for the order. Onboard personally: first value within days, a short call at day 3 and day 14, and a record of the outcome metric for the case study.

**Referrals and testimonials.** Ask at a moment of success, with a specific request and a draft quote they can edit. Agree on name and logo use in writing.

**First 100: building repeatability.** Write down the sequence that actually produced customers (source, message, offer, price, time to close). Move to templates, a CRM, and one scripted demo only when the same steps closed at least 3 to 5 deals. Graham tracks weekly growth: 10% a week gives roughly 14,000 users after one year from 100 ([Graham, 2013](https://paulgraham.com/ds.html)). Lenny's notes tactics for the first 1,000 users differ from those for the next 10,000 ([Lenny's, 2020](https://www.lennysnewsletter.com/p/how-the-biggest-consumer-apps-got)).

**So what for a solo founder:** your job through customer 10 is learning plus closing; hire or automate only the steps you can already describe as a repeatable script.

---

## 6. Launch mechanics

**Pre-launch.** Build a waitlist of people from your ICP, not a general audience; Lenny's lists waitlists and invite-only access as a FOMO route (Superhuman, Robinhood, others). But founders warn: one well-documented 2024 Product Hunt launch removed its waitlist mid-day and called that the most important change, because users could try the product immediately ([Product Hunt story, Nov 2024](https://www.producthunt.com/stories/initially-failed-ph-launch-turned-around-to-get-us-850-paid-subscribers)).

**Channels.**

- **Hacker News (Show HN).** Per the official page, it is for things people can try; sign-up pages, landing pages and newsletters do not qualify; do not ask friends to upvote; be available to answer questions; avoid quickly generated one-offs ([Show HN rules](https://news.ycombinator.com/showhn.html)).
- **Product Hunt.** Reported outcomes vary widely. One launch: 16k signups and 850 paying users (about 5%) ([Product Hunt story, Nov 2024](https://www.producthunt.com/stories/initially-failed-ph-launch-turned-around-to-get-us-850-paid-subscribers)); other founder posts report near-zero paid conversion or churn within weeks (search snippets, self-reported, unverified). **Inference:** treat it as a signup spike, not a business model.
- **Communities.** Offer value first; follow each group's self-promotion rules.
- **Press.** One widely read article reportedly brought "north of 5,000" Superhuman signups; Airbnb's press bump "only lasted a week" ([Lenny's, 2020](https://www.lennysnewsletter.com/p/how-the-biggest-consumer-apps-got)).

**What moved numbers (founder write-ups).** In the Product Hunt case above: dropping the waitlist, posting on Hacker News, a shortened social post with much better reach, asking 2 or 3 larger accounts to amplify, and an in-app review prompt. **Caveat:** one founder's account of one launch; the page includes no agent-directed instructions.

**Launch checklist.**

- [ ] ICP list and 3 launch channels chosen, each with a written post.
- [ ] Product is tryable without a waitlist or heavy signup.
- [ ] Analytics for signup, activation and payment in place.
- [ ] Support path (email/WhatsApp) staffed for launch week.
- [ ] Follow-up email sequence for every signup within 24 hours.
- [ ] Plan to personally contact the top 20 signups.

**So what for a solo founder:** a launch is a data-gathering event; plan the follow-up conversations, not the upvotes.

---

## 7. Metrics that matter early

**Activation.** Define the first moment of value (for example, "first report sent") and measure the share of signups reaching it within 7 days. One vendor table links activation to trial conversion (about 3-5% when activation is under 20% versus 28-38% at 60-80%), but its source is unclear ([search snippet](https://userpilot.com/blog/free-trial-conversion-rate/)). Direction is plausible; numbers unverified.

**Retention and cohorts.** Plot retention by signup week. A curve that flattens above zero is the sign of a keepable user. Cohort data needs enough customers to be meaningful, which is why early founders lean on surveys ([Built In, snippet](https://builtin.com/articles/product-market-fit)).

**Product-market-fit survey.** Ask "how would you feel if you could no longer use it?" The commonly cited bar is 40% "very disappointed", derived by Ellis from nearly 100 startups. Superhuman started at 22%, narrowed to high-expectation users to reach 33%, and later reached 58% ([First Round Review, Nov 2018](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/); over two years old). Sample-size advice conflicts: about 30 (Ellis, reported) to 40-50 or 100+ (vendor blogs, snippets). Survey recently active users only.

**CAC payback and sales cycle.** Track CAC including your own time at a notional wage, months to repay it from gross margin, and days from first call to payment. Benchmark ranges conflict (section 4); decide your own tolerance from runway.

**NPS caveats.** Early scores are inflated by survivorship and early-adopter selection, often in the 60-80 range; NPS can hide unprofitable customers; timing of the survey changes the answer ([Lightspeed, Jan 2017](https://lsvp.com/?p=4231); over two years old, but the logic is general). Use NPS as a trend, never as proof of fit.

**Go / adjust / stop gate.** Set thresholds in advance; the numbers below are **illustrative placeholders to calibrate, not sourced benchmarks**.

| Signal | Go | Adjust | Stop or pivot |
|---|---|---|---|
| Paying customers in beachhead | 10+ with at least 3 referrals | 3 to 9; strong interest, slow close | 0 to 2 after 60 or more qualified conversations |
| "Very disappointed" | 40%+ among active users | 25% to 39%: refine ICP | Under 25% after two iterations |
| Retention cohort | Flattens above zero | Declines slowly; one fixable cause | Falls to near zero |
| Payback vs runway | Repays inside runway with margin | Repays only at a higher price | Cannot repay at any viable price |
| Channel | One repeatable | Several weak | None produces conversations |

Scale only on "go" across at least three rows. Link results back to `unit-economics-model`.

**So what for a solo founder:** write the gate before launch so a bad month cannot be rationalised into "we're early."

---

## 8. Emerging-market notes (sourced only)

- **Mobile money is large.** GSMA reports 2.3 billion registered mobile money accounts in 2025, 593 million 30-day active accounts, over $2 trillion in annual transactions, and most new accounts from sub-Saharan Africa ([GSMA press release, 24 Mar 2026](https://www.gsma.com/newsroom/press-release/mobile-money-accounted-for-2-trillion-in-transactions-in-2025-doubling-since-2021-as-active-accounts-continue-to-grow/)). Only about a quarter of accounts are active monthly (25.7%), so registered accounts overstate usable payers. **Inference:** verify that your target users actually transact monthly on the rail you plan to support.
- **WhatsApp as a business tool.** Vendor blogs claim roughly 80% of small businesses in India and Brazil use WhatsApp to run their business, and that 62% to 80% of Latin American WhatsApp users already message companies; these are secondary figures with unclear primary sources ([Rasayel and others, search snippets](https://learn.rasayel.io/en/blog/whatsapp-user-statistics/)). Use as a hint for where to test, not for planning.
- **Trust and offline channels.** I found no sourced benchmarks on trust, cash-on-delivery or agent networks. Do not infer; test with 20 prospects and note the objections.
- **Regulation and payments.** Rules vary by country; take local legal advice on payments licensing and messaging consent. Not covered here.

**So what for a solo founder:** design the first sale around the payment and messaging channel your customer already uses, and confirm it by observing real transactions.

---

## Staged plan

**Week 1**
- Write ICP, beachhead and the positioning canvas; list 100 named prospects.
- Book 10 discovery calls (use `customer-discovery-interviews`; outreach via `founder-outreach-drafts`).
- Draft the gate table with your own thresholds.

**Month 1**
- 30 or more conversations; quote a real price in each; vary the number.
- Sign 1 to 3 paid pilots; define success metrics.
- Pick the one channel to scale; set up simple tracking of source, stage and objections.
- Model CAC and payback in `unit-economics-model`.

**Quarter 1**
- Reach 10 customers; collect 2 to 3 referenced case studies.
- Run the PMF survey and cohort retention review; decide go, adjust or stop.
- Document the repeatable sales sequence; plan a soft launch (HN or community) only if the product is tryable without friction.
- Optional third-party plugins to explore by name only: `marketing-skills`, `commercial-skills`, `business-growth-skills`, `customer-sales-automation`. Their contents are not described or endorsed here.

## Checklist

- [ ] One-line ICP and 100 named prospects
- [ ] Beachhead chosen and sized bottom-up with labelled assumptions
- [ ] Positioning canvas with alternatives (including do nothing) and one proof point
- [ ] Price quoted in at least 15 conversations; paid pilot template ready
- [ ] One primary channel with weekly experiment log
- [ ] Discovery call script and objection log in use
- [ ] First 10 customers closed personally; referrals requested
- [ ] Launch plan (tryable product, follow-up, support) before posting anywhere
- [ ] Activation, cohort retention, PMF survey and CAC payback tracked
- [ ] Go / adjust / stop gate written before launch
- [ ] Local payment and messaging rails verified (if emerging market)

## Open questions

- Primary-source seed-stage CAC payback and cold-outbound meeting-booked benchmarks (current figures are conflicting vendor blogs).
- Verified benchmarks for hardware, local/service, partnership channels and events.
- Primary text of Dunford, Moore and Casado (only secondary summaries read).
- Sourced data on trust barriers and offline sales channels in emerging markets; primary WhatsApp Business adoption data.
- Current (2026) Product Hunt and Hacker News launch conversion data from audited sources.
- Whether the ChartMogul sample (200 self-reported, small-company skew) generalises.

## Sources

Accessed 2026-11-11. "Opened" means the page was fetched; "snippet" means only seen in search results.

1. [Do Things that Don't Scale, Paul Graham, 2013](https://paulgraham.com/ds.html) (opened)
2. [The SaaS Conversion Report, ChartMogul and ProductLed, Feb 2026](https://chartmogul.com/reports/saas-conversion-report/) (opened)
3. [Geoffrey Moore on finding your beachhead, Lenny's Newsletter, Jan 2024](https://www.lennysnewsletter.com/p/geoffrey-moore-on-finding-your-beachhead) (opened)
4. [How the biggest consumer apps got their first 1,000 users, Lenny's Newsletter, May 2020](https://www.lennysnewsletter.com/p/how-the-biggest-consumer-apps-got) (opened)
5. [Show HN rules, Hacker News](https://news.ycombinator.com/showhn.html) (opened)
6. [Initially failed PH launch turned around to 850 paid subscribers, Product Hunt, Nov 2024](https://www.producthunt.com/stories/initially-failed-ph-launch-turned-around-to-get-us-850-paid-subscribers) (opened)
7. [Mobile money accounted for $2 trillion in transactions in 2025, GSMA, 24 Mar 2026](https://www.gsma.com/newsroom/press-release/mobile-money-accounted-for-2-trillion-in-transactions-in-2025-doubling-since-2021-as-active-accounts-continue-to-grow/) (opened)
8. [Five Components of Effective Positioning, Heinz Marketing, secondary summary of Dunford](https://www.heinzmarketing.com/blog/five-components-of-effective-positioning-an-obviously-awesome-book-summary-part-2/) (opened)
9. [3 tips for growing your startup with Net Promoter Score, Lightspeed, Jan 2017](https://lsvp.com/?p=4231) (opened)
10. [How Superhuman built an engine to find product-market fit, First Round Review, Nov 2018](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/) (opened)
11. [How to kickstart and scale a marketplace business, Lenny's Newsletter, Nov 2019](https://www.lennysnewsletter.com/p/how-to-kickstart-and-scale-a-marketplace) (opened)
12. [Cold email response rates, Belkins](https://belkins.io/blog/cold-email-response-rates.md) (snippet)
13. [B2B SEO timeline benchmarks 2025, The Starr Conspiracy](https://www.thestarrconspiracy.com/insights/benchmarks/b2b-seo-timeline-benchmarks-2025) (snippet, agency)
14. [Maxio CAC benchmarks, SaaS Hero](https://www.saashero.net/strategy/maxio-cac-benchmarks-b2b-saas/) (snippet, vendor)
15. [Price testing methods for startups compared, Koji](https://www.koji.so/blog/price-testing-methods-for-startups-compared) (snippet, vendor)
16. [The Mom Test book report, M. Lynch](https://mtlynch.io/book-reports/the-mom-test/) (snippet, secondary)
17. [Get your first customers, Echai Ventures (aggregator citing a16z)](https://echai.ventures/startingup/path/get-your-first-customers) (snippet, unverified)
18. [Felix Hoffmann ten customers, SaasClub](https://saasclub.io/playbooks/felix-hoffmann-ten-customers-founder-led-story/) (snippet)
19. [Free trial conversion rate, Userpilot](https://userpilot.com/blog/free-trial-conversion-rate/) (snippet, vendor)
20. [Which metric to use for product-market fit, Built In](https://builtin.com/articles/product-market-fit) (snippet)
21. [WhatsApp statistics, Rasayel](https://learn.rasayel.io/en/blog/whatsapp-user-statistics/) (snippet, vendor)
