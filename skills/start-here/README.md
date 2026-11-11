# Start Here

> The front door. Tell it about your business and whether you want a step-by-step **Journey** or a **Departments** view, and it builds a dated plan from everything in this repo.

New founders usually fail from order, not effort: building before validating, raising before there is traction, or drowning in tools. This skill asks a few questions, lets you choose the lens, and returns only what applies to your stage, with the exact skills and pinned plugins to use.

**Research and planning support only. Not legal, tax, investment, or financial advice.**

## When to use it

- "I want to start a business and don't know where to begin."
- "Give me a roadmap to build a company from scratch."
- "I have an idea for X in Kenya. What should I do first?"
- "Show me everything for investors and fundraising."

## What it asks (one round)

| Question | Why |
|---|---|
| **Lens:** Journey, Departments, or Both | You choose how the plan is organised. Switch any time. |
| The business, in a sentence or two | Tailors tasks and tool matches. |
| Your stage today (idea → running) | Starts you at the right place, not at the beginning. |
| Country, and whether it is regulated | Licensing goes first for regulated sectors. |
| Budget and weekly hours | A plan you can't finish is a bad plan. |
| Up to three priority departments (Departments or Both) | Focuses the department view. |

## What you get

- **Journey:** your current stage and the next two, each with its **exit gate** (the test you must pass before moving on) and the tasks that clear it.
- **Departments:** the items for your chosen functions, grouped by stage, with the one to start with.
- **A board** with verb-first tasks, owners, real due dates, definitions of done, and a concrete first seven days. Professional-advice tasks (lawyer, accountant) are on it explicitly.
- **Tool matches:** in-repo skills by name, plus pinned third-party plugins with their `/plugin install` lines as suggestions. Anything that runs code (hooks, MCP servers) is flagged **REVIEW**.
- Offers to turn the board into a live dashboard ([`artifact-project-dashboard`](../artifact-project-dashboard/)) and calendar deadlines ([`deadline-calendar-sync`](../deadline-calendar-sync/)).

## Rules it follows

- Validation comes before building or raising unless you have already tested demand.
- It installs nothing and messages nobody without your approval.
- It never invents plugins or install lines; if something isn't in the [registry](../../registry/registry.yaml) it says so.
- Bootstrapping is a valid answer to "should I raise?".

## Pairs with

[`country-business-research`](../country-business-research/) · [`customer-discovery-interviews`](../customer-discovery-interviews/) · [`unit-economics-model`](../unit-economics-model/) · [`data-protection-readiness`](../data-protection-readiness/) · [`founder-outreach-drafts`](../founder-outreach-drafts/)

## Install

**Claude Code:** `/plugin marketplace add lorenmahia/One_Man_Army`, then `/plugin install one-man-army@one-man-army`.

**Claude.ai / Desktop:** zip the `start-here` folder and upload it under **Settings → Capabilities → Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).
