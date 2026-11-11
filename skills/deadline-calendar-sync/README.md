# Deadline Calendar Sync

> All-day calendar deadlines that link back to the document or board card they belong to, and stay in step when dates change.

A deadline is only useful if it appears where you look and points to the work it belongs to. This skill creates calendar events that do both, and avoids duplicates.

## When to use it

- "Put the licence application deadline on my calendar and link it to the board."
- "The pilot moved to the 20th. Update everything."
- "Add deadlines for each task in this report."

## What it does

- Confirms the exact date (it won't accept "end of the month") in your timezone
- Searches for an existing event first and **updates instead of duplicating**
- Creates an **all-day event marked as free time**, titled `[Project]: [item] due`
- Puts the link to the document or card and a one-line "what done looks like" in the description
- Adds one reminder the day before by default
- When a date moves, updates the event **and** the linked card together
- Asks before deleting events when work is done

## Boundaries

- Never adds other people to an event without your approval.
- If no calendar connector is connected, gives you the event details to add by hand.

## Works well with

[`recurring-research-digest`](../recurring-research-digest/) · [`artifact-project-dashboard`](../artifact-project-dashboard/) · [`country-business-research`](../country-business-research/)

## Install

**Claude Code:** `cp -r skills/deadline-calendar-sync ~/.claude/skills/` from the repo root, then restart Claude Code.

**Claude.ai / Desktop:** zip the `deadline-calendar-sync` folder and upload it under **Settings → Capabilities → Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).
