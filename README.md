# One_Man_Army

**One-person company creation: a toolkit of Claude skills that lets a solo founder research, validate, plan, launch and run a business like a full team.**

Each skill is a self-contained folder that teaches Claude one job a company normally hires for: market research, customer discovery, financial modelling, compliance, outreach, reporting, and keeping it all on schedule. Install the ones you need, or all of them.

> Research and planning support only. Nothing here is legal, tax, investment, or financial advice.

## Choose how you want to build

Everything in this repo is tagged once in a single [registry](./registry/registry.yaml) and shown two ways. Pick the lens that suits you; both always agree.

| If you want... | Start here |
|---|---|
| **A step-by-step path from zero.** Eight stages (Idea → Validate → Foundation → Build → Launch → Raise → Operate → Scale), each with an exit gate. | [**Journey**](./journey/README.md) |
| **To jump to a function.** Strategy, legal, finance, engineering and CI/CD, agents, brand and SEO, sales, investors, networking, operations. | [**Departments**](./departments/README.md) |

How it works, and how to add to it: [Architecture](./docs/ARCHITECTURE.md) · [Contributing](./docs/CONTRIBUTING.md).

### Install in Claude Code

```
/plugin marketplace add lorenmahia/One_Man_Army
/plugin install one-man-army@one-man-army
```

That installs the skills in this repo. The same marketplace also lists **31 pinned third-party plugins** (from ECC, alirezarezvani/claude-skills, wshobson/agents and superpowers) plus 8 link-only references, each tagged to a stage and department. Every stage page in the [Journey](./journey/README.md) ends with the exact `/plugin install` lines for that stage. Anything that runs code (hooks, MCP servers) is flagged **REVIEW**; see [how external repos are reviewed](./docs/EXTERNAL-REVIEW.md), including what was *not* checked.

### Roadmap

- [x] Registry, generated Journey and Departments views, CI validation
- [x] External bundle: pinned, licence-checked references to ECC, claude-skills, wshobson/agents, superpowers and others via a plugin marketplace (spec-kit and awesome-lists are link-only)
- [x] [`start-here`](./skills/start-here/) onboarding skill that asks which lens you prefer and builds your plan
- [x] Raise-stage playbooks: [investor landscape and approach](./playbooks/05-raise/investor-landscape-and-approach.md), [pitch deck and data room](./playbooks/05-raise/pitch-deck-and-data-room.md), [instruments, terms and process](./playbooks/05-raise/instruments-terms-and-process.md)
- [x] Build and Launch playbooks: [CI/CD and release](./playbooks/03-build/cicd-and-release-pipeline.md), [security and secrets baseline](./playbooks/03-build/security-and-secrets-baseline.md), [SEO and GEO](./playbooks/04-launch/seo-and-geo-playbook.md), [go-to-market and first customers](./playbooks/04-launch/go-to-market-and-first-customers.md)
- [x] Remaining stage playbooks: [validation and experiments](./playbooks/01-validate/validation-and-experiment-design.md), [company setup, banking and tax](./playbooks/02-foundation/company-setup-banking-and-tax.md), [contracts, IP and equity](./playbooks/02-foundation/contracts-ip-and-equity.md), [networking and partnerships](./playbooks/04-launch/networking-communities-and-partnerships.md), [operating cadences and reporting](./playbooks/06-operate/operating-cadences-okrs-and-reporting.md), [hiring and scaling](./playbooks/07-scale/hiring-and-scaling-systems.md)
- [ ] Skills, agents and templates distilled from the playbooks

## Skills

### Start here

| Skill | What it does |
|---|---|
| [start-here](./skills/start-here/) | The front door. Asks whether you want a step-by-step Journey or a Departments view, then builds a dated plan with the right skills and pinned plugins for your stage. |

### Research & validation

| Skill | What it does |
|---|---|
| [country-business-research](./skills/country-business-research/) | Turns "I want to run this business in that country" into a sourced market report (competitors, macro and valuations, a demand verdict, six stakeholder viewpoints, niches, key people, company setup routes) plus a dated project board, with optional meetings, alerts, and a recurring refresh. |
| [customer-discovery-interviews](./skills/customer-discovery-interviews/) | Interview guides, a short question script, and a go / adjust / stop gate, so you learn whether people will pay before you build. |
| [unit-economics-model](./skills/unit-economics-model/) | Turns price, volume, fee, loss and cost assumptions into per-unit and annual economics, break-even, capital needs and sensitivity cases. |
| [recurring-research-digest](./skills/recurring-research-digest/) | A standing report every few days or weeks: one new sourced item per run, never repeated, with a research brief, contacts and a deadline. |
| [long-form-report-builder](./skills/long-form-report-builder/) | Builds long, sourced documents in stages (outline, research, fill, verify) so they don't drift or lose sources. |

### Compliance & security

| Skill | What it does |
|---|---|
| [data-protection-readiness](./skills/data-protection-readiness/) | Country-specific checklist for data-controller registration, consent, retention and breach response, linked to the regulator. |
| [secret-exposure-response](./skills/secret-exposure-response/) | When an API key or password is pasted into chat, flags it calmly, advises rotation, and never uses or repeats it. |

### Outreach

| Skill | What it does |
|---|---|
| [founder-outreach-drafts](./skills/founder-outreach-drafts/) | Short outreach messages in your saved voice with one clear ask each. Drafts only; never sent without approval. |

### Operations & dashboards

| Skill | What it does |
|---|---|
| [artifact-project-dashboard](./skills/artifact-project-dashboard/) | A private one-page project dashboard with cards, deadlines, an Ask Claude box and voice input, driven by a single JSON block. |
| [scheduled-artifact-refresh](./skills/scheduled-artifact-refresh/) | A scheduled task that rewrites only a page's data block, validates it, republishes it, and notifies you only for near deadlines or failures. |
| [deadline-calendar-sync](./skills/deadline-calendar-sync/) | All-day calendar deadlines linked to the document or card they belong to, kept in step when dates change. |

## How they fit together

```
country-business-research ──► customer-discovery-interviews ──► unit-economics-model
          │                                                            │
          ├──► founder-outreach-drafts                                 ▼
          ├──► data-protection-readiness                    go / adjust / stop
          ▼
artifact-project-dashboard ◄── scheduled-artifact-refresh
          │
          └──► deadline-calendar-sync ◄── recurring-research-digest ◄── long-form-report-builder
```

## Repository layout

```
registry/registry.yaml   # source of truth: every skill and external repo, tagged by stage and domain
skills/<skill-name>/
  SKILL.md               # instructions Claude follows (YAML frontmatter: name, description)
  README.md              # human overview: when to use, outputs, install
journey/  departments/   # GENERATED views of the registry (do not edit by hand)
scripts/                 # build_views.py, validate.py
docs/                    # ARCHITECTURE.md, CONTRIBUTING.md
```

## Installing a skill

- **Claude Code:** `cp -r skills/<skill-name> ~/.claude/skills/`, then restart Claude Code. To install everything: `cp -r skills/* ~/.claude/skills/`
- **Claude.ai / Desktop:** zip the skill folder and upload it under **Settings → Capabilities → Skills**.

Skills load automatically when a request matches their description; you don't need to name them.
