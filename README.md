# One_Man_Army
One Many Company Creation

A toolkit of Claude skills for building and running a company as a one-person team.

## Skills

| Skill | Description |
|---|---|
| [country-business-research](./skills/country-business-research/) | Turns "I want to run this business in that country" into a sourced market report (competitors, macro and valuations, a demand verdict, six stakeholder viewpoints, niches, key people, company setup routes) plus a dated project board, with optional meetings, alerts, and a recurring refresh. |

## Installing a skill

Each skill lives in its own folder under `skills/` with a `SKILL.md` (the instructions Claude follows) and a `README.md` (for people).

- **Claude Code:** `cp -r skills/<skill-name> ~/.claude/skills/`, then restart Claude Code.
- **Claude.ai / Desktop:** zip the skill folder and upload it under **Settings → Capabilities → Skills**.
