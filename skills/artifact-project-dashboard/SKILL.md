---
name: artifact-project-dashboard
description: Build a private one-page project dashboard artifact with cards, deadlines, an Ask Claude box and voice input, keeping all data in one JSON block. Use when the user wants a personal or team dashboard, project board, or status page they can open and update.
---

# Artifact project dashboard

Builds a single HTML dashboard published as a private artifact. The markup and logic stay fixed; only one JSON block changes. That split is what makes the page safe to refresh automatically later (see scheduled-artifact-refresh).

## Why the data is kept apart

If data, layout and logic are mixed, every later update risks breaking the page. Keep the data in its own `<script type="application/json" id="board-data">` block. Future edits, by you or a scheduled task, touch only that block.

## Steps

1. **Confirm the shape.** Ask for the projects (name, one-line description, status, next action, deadline), what counts as "do first", and whether the user wants voice and an Ask Claude box. Ask one round of questions only.
2. **Gather the data.** Use what the user has already shared, plus any notes or chats they point to. Mark anything you could not verify. Never invent deadlines.
3. **Write the JSON.** Fields: `generatedAt`, `focus` (one most-urgent item with a short why and a deadline in the user's timezone), `projects[]` (id, name, status, statusLabel, description, actions[] with stable ids and due dates, activity[] with links), `events[]`, `automations[]`, `otherChats[]`.
4. **Declare capabilities at creation.** If the page embeds a chat box, declare the sample capability when the artifact is first created. Omit capabilities and icon on later republishes; they carry forward.
5. **Voice.** Use the browser speech API for input and text-to-speech for reading back. If the browser blocks the microphone, tell the user they can use OS dictation instead.
6. **Links.** Link project cards to the project itself when individual chats cannot be linked, and say so.
7. **Check before publishing.** Parse the JSON block, run a syntax check on the inline script, and render at a wide and a narrow width to check for horizontal overflow. Re-read the artifact first if it may have changed.
8. **Tell the user** what to say in chat to update the dashboard, and what the page cannot do (for example, ticking a box in the page does not update the data).

## Limits to state up front
- Checkbox state persists only in that browser.
- Chats inside a project cannot always be linked individually.
- Voice depends on the browser and device.
