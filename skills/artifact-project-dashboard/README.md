# Artifact Project Dashboard

> A private, one-page project dashboard with cards, deadlines, an Ask Claude box and voice input, driven by a single JSON block.

Builds a single HTML dashboard published as a private artifact. The layout and logic stay fixed; all project data lives in one `<script type="application/json" id="board-data">` block. Because of that split, the page can be updated safely by hand or automatically by [`scheduled-artifact-refresh`](../scheduled-artifact-refresh/).

## When to use it

- "Build me a dashboard for my three projects with deadlines."
- "I want a status page for the team that I can open and update."
- "Make a project board I can talk to."

## What you get

- A **focus card** showing the one most urgent item, why it matters, and its deadline
- **Project cards** with status, description, next actions (stable ids and due dates), and activity links
- Events, automations, and links to related chats
- An optional **Ask Claude** box and **voice input / read-back** using the browser speech API
- A pre-publish check: JSON parse, script syntax check, and wide and narrow layout render

## How it works

```
Confirm projects & options (one round of questions)
   → Gather data (no invented deadlines)
   → Write the JSON block
   → Declare capabilities at first publish
   → Validate → Publish → Explain how to update it
```

## Limits

- Checkbox state persists only in that browser; it doesn't update the underlying data.
- Chats inside a project can't always be linked individually.
- Voice depends on the browser and device; OS dictation is the fallback.

## Install

**Claude Code:** `cp -r skills/artifact-project-dashboard ~/.claude/skills/` from the repo root, then restart Claude Code.

**Claude.ai / Desktop:** zip the `artifact-project-dashboard` folder and upload it under **Settings → Capabilities → Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).
