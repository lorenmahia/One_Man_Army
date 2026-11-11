---
name: start-here
description: "Onboard a new founder: ask whether they want a step-by-step Journey (lifecycle stages) or a Departments view (by function), then build a tailored, dated plan from the One_Man_Army registry with the right skills and pinned plugins for their stage. Use when someone says they want to start a business, don't know where to begin, or asks for a roadmap, checklist or plan to build a company from scratch."
---

# Start here

Turns "I want to start a company" into a plan the founder can act on this week. The repo's registry already knows every skill and vetted plugin, tagged by lifecycle **stage** and by **department**. This skill asks a few questions, lets the founder choose how to see it, and returns only what applies to them.

## Why it works this way

New founders fail by doing the right things in the wrong order (building before validating, raising before there is traction) or by drowning in tools. The Journey view fixes order with exit gates. The Departments view fixes findability. Both come from one registry, so the founder can switch at any time without losing anything.

## Steps

1. **Load the registry.** Prefer a local `registry/registry.yaml` if the repo is open. Otherwise fetch `https://raw.githubusercontent.com/lorenmahia/One_Man_Army/main/registry/registry.yaml`. If neither works, say so and continue from the stage list in step 3, marking tool names as unverified.
2. **Ask one round of questions** (use AskUserQuestion if available, otherwise plain text; skip anything already answered):
   - **Lens:** Journey (step by step, recommended for first-time founders), Departments (jump to a function), or Both.
   - **The business:** one or two sentences, who it serves, how it earns.
   - **Stage today:** idea, validating, company not yet set up, building, launched, raising, or running. Map it to a stage id (`00-idea` to `07-scale`).
   - **Country** and whether the business is regulated (finance, health, food, education, telecom, crypto).
   - **Budget and weekly hours.**
   - **Priority departments** (Departments or Both only): up to three.
3. **Restate in three lines** what you understood, then proceed. The founder can correct it.
4. **Build the plan.**
   - **Journey:** from the current stage to the next two, give the stage's purpose, its **exit gate** (written in advance, as the registry states it), and the tasks that clear it. Do not outline later stages beyond one line each.
   - **Departments:** for each priority department, list the registered items grouped by stage, with the one to reach for first.
   - **Both:** use the Journey as the spine and tag each task with its department.
   - Put validation first for anyone who has not yet tested demand, whatever else they ask for. Say why in one sentence.
5. **Match tools.** For each task name the in-repo skill when one exists (for example `country-business-research`, `customer-discovery-interviews`, `unit-economics-model`, `data-protection-readiness`, `founder-outreach-drafts`). Where the registry has a pinned external plugin, show it as a **suggestion** with its install line. Never run an install yourself.
6. **Flag what runs code.** Any entry whose `runs_code` includes `hooks` or `mcp-server` is marked **REVIEW**. Tell the founder to read it first and point to `docs/EXTERNAL-REVIEW.md`, which also states what the vetting did not cover. Offer an unflagged alternative from the same stage when one exists.
7. **Make it actionable.** Output a board: each task has a verb-first title, owner (founder or a named professional), a real due date anchored to today in the founder's timezone, a definition of done, and its stage. The first seven days must be concrete enough to start tomorrow. Put professional-advice tasks (lawyer, accountant) on the board explicitly. Deliver it as a document or board artifact if an artifact tool exists, otherwise a markdown checklist file. Offer `artifact-project-dashboard` for a living dashboard and `deadline-calendar-sync` for calendar deadlines; create events only after approval.
8. **Close** with the verdict on where they are, the single next action, and one line on how to switch lens or move to the next stage ("run start-here again at the exit gate").

## Rules

- **Research and planning support only.** Not legal, tax, investment or financial advice. Say so once at the top of the plan and again beside any legal, tax or fundraising task.
- Install nothing and message nobody without explicit approval.
- Do not invent registry entries, plugin names or install lines. If an item is not in the registry, say it is not and suggest adding it.
- Do not push fundraising on a founder who has not validated demand. Raising belongs to stage `05-raise`; mention bootstrapping as a valid outcome.
- Regulated businesses: put licensing and compliance at the front of the plan, since it often decides feasibility.
- Keep the plan to what fits the founder's stated weekly hours. A plan they cannot finish is a bad plan.
