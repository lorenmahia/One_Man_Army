---
name: deadline-calendar-sync
description: Create all-day calendar deadlines that link back to the document or board card they belong to, and keep them in step when the dates change. Use when the user wants a deadline on their calendar tied to a report, task or project.
---

# Deadline calendar sync

A deadline is only useful if it appears where the user looks and points to the work it belongs to.

## Steps

1. **Confirm the deadline.** Get the date and the item. If the date is vague ("end of the month"), ask for the exact day. Use the user's timezone.
2. **Check for an existing event.** Search the calendar for the same title before creating one. If it exists, update it instead of duplicating.
3. **Create an all-day event.** Mark it as free time, so it does not block the calendar. Use the title format "[Project]: [item] due".
4. **Link it.** Put the link to the document or board card in the event description, with one line saying what done looks like.
5. **Set a reminder.** Default to one reminder on the day before. Ask only if the user wants more.
6. **Update on change.** If the item moves, update the event and the linked card together. Never leave the two out of step.
7. **Remove when done.** When the item is complete, ask before deleting the event. Do not delete without asking.

## Rules

- Times are in the user's timezone; state the timezone once.
- Do not add other people to the event without approval.
- If the calendar connector is not connected, give the user the event details to add by hand.
