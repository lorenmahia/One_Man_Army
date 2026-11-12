# SEO and GEO Playbook: Being Found by Search Engines and AI Answer Engines (2026)

> Last verified: 2026-11-11. Research and planning support only; not legal, tax, investment or financial advice.

**Summary**

- AI answers reduce clicks on classic results, but the size is disputed: studies range from roughly a one-third to a 58% CTR drop where an AI Overview appears, while Google says total clicks are "relatively stable" without publishing figures (Section 1).
- Google's own documentation says there is nothing special to do for AI Overviews and AI Mode beyond sound SEO: indexable, crawlable, helpful, first-hand content (Sections 2 and 4). Most "GEO" advice beyond that is correlation data from tool vendors.
- A new site with no authority should win narrow, specific topics with original data and first-hand experience, not volume or scaled AI content, which Google treats as spam if it adds no value (Section 3).
- AI citations correlate with being mentioned across the web (YouTube, Reddit, press, directories), not with llms.txt or schema tricks; measure with manual prompt tests, Search Console and Bing reports, and referral logs (Sections 4 to 6).
- Plan for slow results: only about 1.7% of new pages reached the Google top 10 within a year in one vendor study. Do not rely on one channel (Sections 6 to 8).

---

## 1. How discovery changed

**Fact (Pew, data March 2025, published 2025-07-22; older than 12 months):** In a browsing panel of 900 US adults (68,879 unique Google searches), users clicked a traditional result in 8% of visits to pages with an AI summary versus 15% without. About 1% of visits clicked a link inside the summary, and 26% of visits with a summary ended the session versus 16% without. About 18% of searches showed a summary; 53% of searches with 10+ words did versus 8% of one- or two-word searches ([Pew Research](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)). Google disputed the methodology ([9to5Google via search snippet](https://9to5google.com/2025/07/23/google-ai-overview-link-click-study/)).

**Fact, vendor data (Ahrefs, published 2026-02-04, data December 2025; vendor sells SEO tools):** For 150,000 keywords with an AI Overview, average desktop position-1 CTR was 58% lower than a forecast without it (0.016 versus 0.037). Reductions by position ran from 58.0% (position 1) to 19.4% (position 10). It is a correlation with a modeled counterfactual, desktop only ([Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/)). Its earlier version (April 2025) found 34.5% (reported in [search snippets](https://ahrefs.com/blog/ai-overviews-reduce-clicks/)).

**Range (position-1 CTR loss where an AI Overview shows): about 34.5% (Ahrefs, 2025) to 58% (Ahrefs, 2026).** Pew's 8% versus 15% implies roughly 47% fewer result clicks, a different metric from a different population.

**Fact, snippet only (Similarweb, mid-2025; older than 12 months):** News-related searches ending with no click rose from about 56% to about 69% between May 2024 and May 2025; Google called the methodology flawed ([Search Engine Roundtable snippet](https://www.seroundtable.com/similarweb-google-zero-click-search-growth-39706.html), [TechCrunch snippet](https://techcrunch.com/2025/07/02/chatgpt-referrals-to-news-sites-are-growing-but-not-enough-to-offset-search-declines)). News is not your market; treat as direction only.

**Google's position (2025-08-06; older than 12 months):** VP Liz Reid wrote that total organic click volume is "relatively stable" year over year and "quality" clicks slightly up, calling reports of steep declines flawed. The post publishes no click figures, and says traffic is shifting toward forums, video and first-hand perspectives ([Google blog](https://blog.google/products-and-platforms/products/search/ai-search-driving-more-queries-higher-quality-clicks/)).

**AI referral value (conflicting, vendor-flavored):** Semrush (June 2025, snippet only) reported AI-search visitors convert about 4.4x better than organic. An Amsive analysis (reported by Search Engine Land, snippet only) found 4.6% organic versus 4.87% LLM conversion with no statistically significant difference and LLM traffic under 1% of sessions ([Search Engine Land snippet](https://searchengineland.com/ai-search-clicks-arent-always-better-traffic-study-457488), [Semrush](https://www.semrush.com/blog/ai-search-seo-traffic-study/)).

**Inference:** For a new site, informational head terms are the worst place to compete, since they are the ones that trigger AI summaries (longer, question-style queries trigger them most). Queries with transactional, local, product-comparison or brand intent, and queries needing first-hand evidence, are better odds. Expect lower click volume per ranking than older benchmarks imply, and plan for brand mentions to matter as much as rankings.

**So what for a solo founder:** Budget for fewer clicks per impression, target specific intents, and do not forecast traffic from pre-2024 CTR curves.

---

## 2. Foundations that still matter

Google states that AI Overviews and AI Mode have "no additional requirements": a page must be indexed and eligible to show with a snippet ([Google: AI features](https://developers.google.com/search/docs/appearance/ai-features)). Its May 2026 guide treats optimizing for generative features as SEO ([Google: AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)). So the basics are also your GEO baseline.

- **Crawlability and indexing.** Google mostly finds pages through links from pages it already knows; give every page you care about at least one internal link, using real `<a href>` elements and descriptive anchor text ([Google: crawlable links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)). Verify the site in Search Console and use URL Inspection to see what Google sees ([Google: SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)).
- **robots.txt.** It controls crawling, not indexing; a blocked URL can still be indexed if linked. Use `noindex` or authentication to keep pages out, and do not block CSS or JavaScript the page needs ([Google: robots.txt intro](https://developers.google.com/search/docs/crawling-indexing/robots/intro)).
- **Sitemaps.** Optional; a list of URLs you care about, often auto-generated by your CMS ([Google: SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)). Submit one in Search Console.
- **Canonicals.** Google's support docs say canonicals can be indicated via sitemap, HTML tags or Search Console ([search-snippet summary of Google docs](https://support.google.com/webmasters/answer/10267942)); pick one URL per page and keep it consistent. I did not open the canonical page itself.
- **Core Web Vitals.** Good thresholds at the 75th percentile, mobile and desktop separately: LCP at most 2.5 s, INP at most 200 ms, CLS at most 0.1 ([web.dev](https://web.dev/articles/vitals)).
- **Mobile, HTTPS.** Mobile-first indexing and HTTPS are standard; I only saw third-party summaries, not Google pages, in this research (see Open questions). Ship responsive design and HTTPS-only with redirects regardless.
- **Structured data.** Not required for AI features and no special AI schema exists; markup must match visible text ([Google: AI features](https://developers.google.com/search/docs/appearance/ai-features)). Use Organization, Product and Article where they apply to your pages for rich-result eligibility. **FAQ rich results are deprecated:** Google's page says the feature stopped showing from 2026-05-07 and the documentation was removed 2026-06-15 ([Google: FAQ structured data](https://developers.google.com/search/docs/appearance/structured-data/faqpage)). Do not invest in FAQ schema for Google; an FAQ section is still fine for readers.
- **Information architecture.** Keep a clear site purpose; Google lists "a clear primary purpose or focus" as a people-first signal ([Google: helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)). Practical layout (Inference): one hub page per topic cluster, linking to detail pages and back.
- **Preview controls.** `nosnippet`, `max-snippet`, `data-nosnippet` and `noindex` limit what shows, including in AI features ([Google: AI features](https://developers.google.com/search/docs/appearance/ai-features)).

Changes can take hours to several months to show; Google suggests waiting a few weeks before judging ([Google: SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)).

**So what for a solo founder:** A day of technical setup (Search Console, sitemap, clean URLs, fast mobile pages) removes the only hard blockers; everything else is content and reputation.

---

## 3. Content strategy with no authority

- **Narrow cluster first.** Google warns against covering many unrelated topics and against "summarizing others without adding value" ([Google: helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)). Inference: pick one problem your product solves and publish 10 to 20 interlinked pages that cover it completely before expanding.
- **Search intent types (standard framework, not a Google ranking factor):** informational, navigational, commercial investigation, transactional. Map each page to one. Pages with first-hand comparisons, pricing, setup walkthroughs and "X for [specific audience]" angles fit commercial intent and are less exposed to AI summaries (Inference).
- **Hand-written versus programmatic.** Google says generative AI can help research and structure content, but generating many pages without adding value may violate the scaled content abuse policy, "no matter how it's created" ([Google: generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content), [Google: spam policies](https://developers.google.com/search/docs/essentials/spam-policies)). Programmatic pages are safe only if each carries unique data or utility (Inference). Start hand-written.
- **AI-assisted drafting.** Allowed if it meets Search Essentials; Google advises fact-checking everything, including titles, meta descriptions and structured data, and explaining how content was made when readers would wonder ([Google: generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)).
- **E-E-A-T: evidence versus folklore.** Fact: Google says E-E-A-T is not a specific ranking factor, trust is the most important element, and quality raters do not directly control rankings ([Google: helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)). Fact: Google asks for clear "who, how, why", with bylines and author background, and calls fabricated creator profiles deceptive. Folklore: that a particular badge, author-schema tag or "E-E-A-T score" exists. Inference: show a real founder byline, real customer evidence and dated updates.
- **Original data and first-hand experience as the moat.** Google's AI guide recommends non-commodity content with a unique first-hand perspective ([Google: AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)); its 2025 blog post says sites with forums, video and first-hand perspectives are gaining ([Google blog](https://blog.google/products-and-platforms/products/search/ai-search-driving-more-queries-higher-quality-clicks/)). Ideas: your own survey, benchmark, teardown, pricing study or anonymized product data.
- **Keyword research with free tools.** Search Console queries (once you have impressions), Google Trends, Google Keyword Planner and autocomplete/People Also Ask are commonly used free sources; I did not verify tool specifics in this research (Inference). Prefer long, specific queries: a vendor study found only 0.3% of new pages reached the top 10 within a year for keywords with 10,000+ monthly searches ([Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/)).

**So what for a solo founder:** One tight topic, hand-written, with something only you can say (data, screenshots, real customer cases), beats 200 generic AI pages.

---

## 4. GEO/AEO: known versus speculative

### Fact (platform documentation)

- **Google:** No special requirements; no new files, markup, chunking or rewrites for AI; no ideal page length. Do not create content variations to manipulate AI answers or pursue inauthentic "mentions" (this may fall under spam policies) ([Google: AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)). Google says its spam policies explicitly cover manipulating generative responses ([Google: spam policies](https://developers.google.com/search/docs/essentials/spam-policies)).
- **llms.txt:** Google says its Search does not use these files; creating one neither helps nor harms Search ([Google: AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)). I found no OpenAI, Anthropic or Perplexity documentation that treats it as a citation signal (absence in the pages I opened, not proof).
- **OpenAI:** `OAI-SearchBot` surfaces sites in ChatGPT search (opt-outs can still appear as navigational links); `GPTBot` is for training; `ChatGPT-User` is user-initiated and may not follow robots.txt; robots changes take about 24 hours ([OpenAI bots](https://developers.openai.com/docs/bots)).
- **Anthropic:** `ClaudeBot` (training), `Claude-User` (user-requested fetches), `Claude-SearchBot` (search quality); disabling the latter two may reduce visibility; all honor robots.txt ([Anthropic support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)).
- **Perplexity:** `PerplexityBot` surfaces and links sites and is not used for foundation-model training; `Perplexity-User` generally ignores robots.txt; no citation is promised ([Perplexity docs](https://docs.perplexity.ai/guides/bots)).
- **Implication:** Do not block the search bots (OAI-SearchBot, Claude-SearchBot, PerplexityBot, Googlebot) if you want visibility. Training bots are a separate business choice.

### Reproducible or published studies (mostly vendor, correlational)

- **Peer-reviewed:** The GEO paper (KDD 2024, arXiv 2023) reports up to 40% visibility gains from content strategies in a research benchmark and that effectiveness varies by domain ([arXiv](https://arxiv.org/abs/2311.09735)). Older than 12 months and tested on a research setup, not live engines; secondary blogs disagree on per-tactic figures, so I do not quote them.
- **Citations overlap with rankings, conflicting.** Ahrefs (July 2025, 1.9M citations): 76.1% of AI Overview citations were from the Google top 10 ([Ahrefs](https://ahrefs.com/blog/search-rankings-ai-citations)). Later vendor figures in search snippets are far lower (BrightEdge about 17%, Surfer 67.82% of cited pages outside the top 10, Conductor 43% inside); they measure different things and I did not open the originals ([search summary](https://apiserpent.com/blog/ai-overview-citations-vs-rankings-overlap)). **Range: 17% to 76%.** Ranking still helps but does not guarantee citation.
- **Brand mentions.** Ahrefs (published 2025-12-12, about 75,000 brands, DR above 40): YouTube mentions correlate about 0.74 with AI visibility, branded web mentions 0.66 to 0.71, backlinks very weakly; the author says this is correlation and may reflect existing brand strength ([Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations)). Vendor sells the tool used.
- **Cited domains.** Pew found Wikipedia, YouTube and Reddit top both summary sources and standard results; .gov sites were 6% of summary sources versus 2% of standard results ([Pew](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)). A Peec AI analysis (30M sources, snippet only) ranks Reddit first across engines, while other analyses put Wikipedia first for ChatGPT; shares vary widely by study and window ([Search Engine Land snippet](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138), [Contently](https://contently.com/2026/04/29/top-sources-llms-cite/)).
- **llms.txt data (vendor):** SE Ranking (page dated 2026-10-15, about 300,000 domains, 10.13% had the file) found no relationship with citation frequency; its model, sampled LLMs and window are not disclosed, and the firm sells AI visibility tools ([SE Ranking](https://seranking.com/blog/llms-txt/)). Snippet-only reports say an Ahrefs study found 97% of llms.txt files received no requests in May 2026; unverified.

### Inference (reasonable, not proven)

- Clear entity facts on your own site (who you are, what you sell, for whom, pricing, location), consistent across your site, LinkedIn, directories and review sites, make it easier for any system to describe you correctly.
- Q&A-style headings and direct, quotable answers make extraction easier; Google says chunking is unnecessary for its systems, so this is for readers first.
- Third-party mentions (communities, YouTube, press, comparison and review sites) probably feed AI answers because the studies above show those domains are heavily cited. Genuine participation is fine; Google flags inauthentic mentions as a risk.

### Vendor hype to discount

Claims of a guaranteed "AI ranking factor", paid "AI schema", llms.txt as a lever, or tools claiming access to Google's internal metrics. Google specifically warns about the last ([Google: AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)).

### How to measure

1. **Manual prompt tests (free, Inference):** monthly, run 15 to 25 fixed prompts (category, comparison, "best X for Y", your brand name) in Google AI Mode, ChatGPT search, Perplexity and Claude with search on, logged in a sheet: cited? mentioned? accurate? which competitor? Results vary run to run, so repeat each three times.
2. **Search Console Generative AI performance report:** announced 2026-06-03, global from 2026-08-31; shows impressions, pages, countries, devices in AI Overviews and AI Mode, but only impressions, not clicks ([Google Search Central blog](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports)).
3. **Bing Webmaster Tools AI Performance report:** public preview from February 2026 per third-party coverage, citations in Copilot and Bing AI summaries, no clicks; I saw only secondary reports ([Search Engine Land snippet](https://searchengineland.com/bing-webmaster-tools-testing-new-ai-performance-report-468039)).
4. **Referral analysis:** in analytics, filter referrers for chatgpt.com, perplexity.ai, claude.ai, copilot and similar; expect small numbers (one study found LLM traffic under 1% of sessions, see Section 1). Check server logs for the bots named above.
5. **Paid tools:** vendor trackers exist; treat as directional and pilot one only after you have steady content.

**So what for a solo founder:** Do the SEO basics, keep search bots allowed, build real mentions on the few platforms your buyers use, and track with a spreadsheet before paying for a tool.

---

## 5. Off-site: links, mentions, reviews, local

- **Links worth earning.** Editorial links from relevant sites you did not pay for. Google's spam policy treats links made mainly to manipulate ranking as spam; paid links need `rel="nofollow"` or `rel="sponsored"`, and automated links, excessive exchanges and low-quality directory links should be avoided ([Google: spam policies](https://developers.google.com/search/docs/essentials/spam-policies)). User-generated links should use `ugc`.
- **Digital PR for a small company (Inference).** Publish a data point a journalist or newsletter would cite, offer expert comments on topics you know, and announce real news. Secondary sources say such coverage often has no followed link, but it creates the mentions AI studies correlate with. Google's own link-building guidance was not found in this research; claims attributed to Google staff here are unverified.
- **Directories and communities.** Use a small set of relevant, real profiles (product directories, industry associations, review sites such as G2 or Capterra if applicable) and answer questions in forums where you add value and disclose your affiliation. Pew and other studies show forums and video are heavily cited, but Google warns against inauthentic mentions.
- **Reviews.** Ask real customers; never buy or fake them. For local businesses, Google says review count and score factor into local ranking ([Google Business Profile help](https://support.google.com/business/answer/7091?hl=en), search-snippet summary).
- **Google Business Profile (local businesses only).** Local ranking rests on relevance, distance and prominence; businesses cannot pay to rank higher ([Google Business Profile help](https://support.google.com/business/answer/7091?hl=en), snippet summary). Complete every field, keep hours and categories accurate. Eligibility rules (real address, in-person service) came from third-party guides; verify in Google's guidelines first.
- **Bought links, PBNs, expired-domain tricks:** policy violations ([Google: spam policies](https://developers.google.com/search/docs/essentials/spam-policies)).

**So what for a solo founder:** Ten genuine mentions on the sites your buyers read beat a hundred bought links, and reviews matter most if you serve a local area.

---

## 6. Measurement, baselines and timeline

- **Setup (Week 1):** Verify Search Console (domain property), submit sitemap, install analytics with conversion events, and verify Bing Webmaster Tools. Record baselines: indexed pages, impressions, clicks, average position, branded versus non-branded queries, AI-referral sessions, and your manual prompt-test log.
- **Weekly:** indexing and coverage errors, new queries. **Monthly:** prompt tests, top pages, conversions per channel. Search Console reports AI Overview and AI Mode traffic inside the normal Web search type, not separately ([Google: AI features](https://developers.google.com/search/docs/appearance/ai-features)); the new report adds impressions only.
- **Timelines (with caveats).** Google says changes can take hours to months ([Google: SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)). Ahrefs (published 2025-05-15, data collected 2023; older than 12 months; vendor): 1.74% of new pages reached the top 10 within a year (6.11% under an English-only filter); of those that did, 40.82% did so within one month; 72.9% of top-10 pages are over three years old; page age is correlation only ([Ahrefs](https://ahrefs.com/blog/how-long-does-it-take-to-rank/)). **Range: 1.74% to 6.11% for the same study, depending on filter.**
- **90-day plan.** Days 1 to 30: technical setup, baselines, cluster map, first 4 to 6 pages. Days 31 to 60: 6 to 8 more pages plus one original-data asset, outreach to 10 relevant sites or communities, first prompt-test review. Days 61 to 90: update pages from Search Console queries, add comparison and use-case pages, review what is indexed and cited.
- **Realistic expectations (Estimate):** within 90 days expect indexing, some impressions on long-tail queries and a few clicks; meaningful traffic usually takes 6 to 12 months or more, consistent with the study above. Do not judge the channel before about 3 months of consistent publishing, and do not depend on it for early revenue.

**So what for a solo founder:** Set baselines on day one and judge progress by impressions, indexed pages and citations first, clicks and revenue later.

---

## 7. Risks

- **Penalties.** Violations can lower rankings or remove pages from results; automated systems plus manual actions; repeated circumvention can lead to broader removal ([Google: spam policies](https://developers.google.com/search/docs/essentials/spam-policies)).
- **AI-content pitfalls.** Scaled content without added value, unverified facts, fake author profiles, and undisclosed automation where readers would expect it ([Google: generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content), [Google: helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)). Ecommerce sellers should label AI-generated product text per Google's guidance.
- **Link schemes and site reputation abuse.** Paid or exchanged links, expired-domain repurposing, and hosting third-party content on a strong domain to borrow its signals.
- **Manipulating AI answers.** Google says its spam policies cover this and warns against inauthentic mentions; fake Reddit or review activity also breaks platform rules (Inference: and invites reputational damage).
- **One-channel reliance.** Click volume per ranking has fallen (Section 1) and algorithms change. Build an email list, direct relationships, communities and a second acquisition channel.
- **Stale benchmarks.** Many figures here are 2025 data; AI features and studies change within months. Re-check before major decisions.

**So what for a solo founder:** The risky shortcuts (mass AI pages, bought links, fake mentions) are exactly what Google names as spam; the safe path is also the cheapest.

---

## 8. Staged plan

**Week 1**
- Verify Search Console and Bing Webmaster Tools; submit sitemap; confirm HTTPS, mobile layout, no accidental `noindex` or robots blocks.
- Allow Googlebot, OAI-SearchBot, Claude-SearchBot and PerplexityBot (decide training bots separately).
- Add Organization details to your site (name, what you do, contact, social profiles) and consistent profiles elsewhere.
- Record baselines; build a 20-prompt test sheet.

**Month 1**
- Choose one topic cluster; publish 4 to 6 hand-written pages with a real byline; interlink them.
- Fix Core Web Vitals issues reported in Search Console.
- Create 3 to 5 genuine third-party profiles and begin answering questions in one or two communities.
- First manual prompt test; check Search Console indexing.

**Quarter 1**
- 15 to 20 pages total, one original-data asset, a comparison page set, and outreach for coverage.
- Review Search Console queries and the Generative AI report monthly; update or prune weak pages.
- Ask real customers for reviews; set up Google Business Profile if local.
- Decide whether a paid tracker or agency is justified; probably not before month 6.

**Pointers by name only (not reviewed here):** third-party plugins `seo-content-creation`, `seo-technical-optimization`, `seo-analysis-monitoring`, `marketing-skills`; reading list repo `awesome-seo` (options only; its contents were not checked beyond its description).

---

## Checklist

- [ ] Search Console (domain) and Bing Webmaster Tools verified; sitemap submitted
- [ ] HTTPS only, responsive, pages pass LCP 2.5 s / INP 200 ms / CLS 0.1 at p75
- [ ] No `noindex` or robots blocks on pages you want found; search bots allowed
- [ ] Every key page linked internally with descriptive anchors
- [ ] One narrow topic cluster mapped to intents; real author byline and about page
- [ ] No scaled or unreviewed AI pages; all facts checked
- [ ] Organization and relevant Product/Article structured data valid and matching visible text; no reliance on FAQ rich results
- [ ] Baselines recorded; monthly prompt-test sheet running
- [ ] Genuine third-party mentions started; no paid links without `sponsored`/`nofollow`
- [ ] Google Business Profile complete (local only); reviews requested honestly
- [ ] A second acquisition channel planned

## Open questions

- Exact current wording of Google's canonical, mobile-first and HTTPS pages (only secondary summaries seen).
- Whether the llms.txt "97% unused" (Ahrefs, May 2026) and OtterlyAI log figures are accurate (seen only via a secondary summary).
- Current AI Overview citation overlap with the organic top 10 (17% to 76% depending on source, vendor methods unaudited).
- Bing AI Performance report scope and general availability (secondary sources only).
- Whether Google's Search generative AI opt-out control behaves exactly as described (taken from a snippet of Google's page).
- Google Business Profile eligibility rules (third-party only).
- Independent evidence that Q&A formatting, schema or entity markup increases AI citations (none found).
- Which free keyword tools remain best in 2026 (not verified).

## Sources

All accessed 2026-11-11. "Snippet" means only a search-result summary was seen.

1. [Pew Research: users less likely to click when an AI summary appears](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) (2025-07-22)
2. [Ahrefs: AI Overviews reduce clicks, update](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/) (2026-02-04)
3. [Ahrefs: AI Overviews reduce clicks (original, snippet)](https://ahrefs.com/blog/ai-overviews-reduce-clicks/) (2025)
4. [Search Engine Roundtable: Similarweb zero-click (snippet)](https://www.seroundtable.com/similarweb-google-zero-click-search-growth-39706.html) (2025)
5. [TechCrunch: ChatGPT referrals to news sites (snippet)](https://techcrunch.com/2025/07/02/chatgpt-referrals-to-news-sites-are-growing-but-not-enough-to-offset-search-declines) (2025-07-02)
6. [9to5Google: AI Overview click study (snippet)](https://9to5google.com/2025/07/23/google-ai-overview-link-click-study/) (2025-07-23)
7. [Google blog: AI in Search driving more queries, higher quality clicks](https://blog.google/products-and-platforms/products/search/ai-search-driving-more-queries-higher-quality-clicks/) (2025-08-06)
8. [Semrush: AI search traffic study (snippet)](https://www.semrush.com/blog/ai-search-seo-traffic-study/) (2025-06)
9. [Search Engine Land: AI search clicks and traffic quality (snippet)](https://searchengineland.com/ai-search-clicks-arent-always-better-traffic-study-457488) (2025)
10. [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) (undated)
11. [Google Search Central: Optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) (2026-05, per secondary coverage)
12. [Google Search Central: Generative AI performance reports blog](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) (2026-06-03)
13. [Google Search Central: Using generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) (undated)
14. [Google Search Central: Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) (undated)
15. [Google Search Central: Spam policies](https://developers.google.com/search/docs/essentials/spam-policies) (undated)
16. [Google Search Central: FAQ structured data](https://developers.google.com/search/docs/appearance/structured-data/faqpage) (updated 2026-06)
17. [Google Search Central: SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) (undated)
18. [Google Search Central: crawlable links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) (undated)
19. [Google Search Central: robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro) (undated)
20. [Google Search Console Help: canonical (snippet)](https://support.google.com/webmasters/answer/10267942) (undated)
21. [web.dev: Core Web Vitals](https://web.dev/articles/vitals) (undated)
22. [Google Business Profile help: improve local ranking (snippet)](https://support.google.com/business/answer/7091?hl=en) (undated)
23. [OpenAI: crawlers and bots](https://developers.openai.com/docs/bots) (undated)
24. [Anthropic support: web crawling and blocking](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) (undated)
25. [Perplexity docs: bots](https://docs.perplexity.ai/guides/bots) (undated)
26. [arXiv: GEO, Generative Engine Optimization](https://arxiv.org/abs/2311.09735) (2023; KDD 2024)
27. [Ahrefs: search rankings and AI citations](https://ahrefs.com/blog/search-rankings-ai-citations) (2025-07-21)
28. [Ahrefs: AI brand visibility correlations](https://ahrefs.com/blog/ai-brand-visibility-correlations) (2025-12-12)
29. [Ahrefs: how long it takes to rank](https://ahrefs.com/blog/how-long-does-it-take-to-rank/) (2025-05-15)
30. [SE Ranking: llms.txt study](https://seranking.com/blog/llms-txt/) (2026-10-15)
31. [Search Engine Land: AI engines cite Reddit, YouTube, LinkedIn (snippet)](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138) (undated)
32. [Contently: top sources LLMs cite (snippet)](https://contently.com/2026/04/29/top-sources-llms-cite/) (2026-04-29)
33. [Search summary: AI Overview citations versus rankings (snippet)](https://apiserpent.com/blog/ai-overview-citations-vs-rankings-overlap) (2026)
34. [Search Engine Land: Bing AI Performance report (snippet)](https://searchengineland.com/bing-webmaster-tools-testing-new-ai-performance-report-468039) (2026)
