---
name: scheduled-artifact-refresh
description: Set up a recurring scheduled task that rewrites only the data block of a published page, validates it, republishes, and notifies only for near deadlines or failed jobs. Use when a dashboard or report should stay current without the user opening a chat.
---

# Scheduled artifact refresh

Runs unattended. Each firing is a fresh session with no memory of the chat that set it up, so the prompt must contain everything: the artifact URL, the data sources, the exact edit rule, and the validation steps.

## Set up

1. **Confirm cadence and timezone.** Default is daily, early morning, in the user's timezone. Write the cron expression with the timezone prefix so it fires at the right local time.
2. **Confirm the notification rule.** Push or email only for deadlines inside a set window (for example, 3 days) and for failed scheduled jobs. Nothing else.
3. **Write a self-contained prompt.** It must say: nobody is watching, do not ask questions, and where something is ambiguous take the most reasonable reading and state it in one line. It must name each data source, in the order to read it, and give the exact edit rule.
4. **Set ownership.** If several tasks update the same page, each task owns only its own entries. Each prompt tells the task to copy other entries by id exactly as found.
5. **Edit rule.** Change only the JSON data block. Never touch the markup, styles or script. Keep stable ids for unchanged items. Drop items whose dates passed more than two days ago or that are done.
6. **Validate before publishing.** Parse the JSON. Run a syntax check on the inline script. If either fails, do not publish; send the user a one-line note instead.
7. **Publish to the same URL.** Do not pass capabilities or icon on republish.
8. **Notify** with a short message: the top item, up to three deadlines in the window, and any failed job.
9. **Tell the user** how to pause or delete the task, and how to ask for an immediate refresh in chat.

## Failure handling

If a data source is missing or a tool fails, keep the last good data, mark that section as stale with its date, and notify once. Never publish partial data as if it were complete.
