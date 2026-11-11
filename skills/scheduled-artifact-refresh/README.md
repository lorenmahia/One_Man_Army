# Scheduled Artifact Refresh

> Keeps a published dashboard or report current with a scheduled task that rewrites only its data block, validates it, republishes it, and notifies you only when it matters.

Runs unattended. Each firing is a fresh session with no memory of the chat that set it up, so the skill writes a fully self-contained prompt: the artifact URL, the data sources in order, the exact edit rule, and the validation steps.

## When to use it

- "Refresh my dashboard every morning at 7."
- "Keep this report up to date without me opening a chat."
- "Ping me only when a deadline is close or something breaks."

## What it sets up

- A **cron schedule** in your timezone (default: daily, early morning)
- A **notification rule**: push or email only for deadlines inside a set window (for example, 3 days) or for failed jobs
- An **edit rule**: change only the JSON data block, never the markup, styles or script; keep stable ids; drop items that are done or more than 2 days past their date
- **Ownership** when several tasks share a page: each task owns only its own entries and copies the others exactly
- **Validation before publishing**: JSON parse and inline-script syntax check. If either fails, nothing is published and you get a one-line note.

## Failure handling

If a source is missing or a tool fails, it keeps the last good data, marks that section as stale with its date, and notifies you once. It never publishes partial data as if it were complete.

## Works well with

[`artifact-project-dashboard`](../artifact-project-dashboard/), which builds pages with the separate data block this skill expects.

## Install

**Claude Code:** `cp -r skills/scheduled-artifact-refresh ~/.claude/skills/` from the repo root, then restart Claude Code.

**Claude.ai / Desktop:** zip the `scheduled-artifact-refresh` folder and upload it under **Settings → Capabilities → Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).
