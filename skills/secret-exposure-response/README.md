# Secret Exposure Response

> When an API key, password or token is pasted into chat, flag it calmly, advise rotation, and never use or repeat it.

A credential pasted into a chat is stored in the conversation and should be treated as exposed. This skill makes Claude respond in a way that is specific and helpful, not alarmist.

## When it triggers

Whenever a message contains what looks like a live credential: API keys, passwords, tokens, connection strings, private keys.

## What Claude does

1. **Doesn't use the secret**, even if asked, until it has been rotated
2. **Doesn't repeat it**, not even partially; it refers to it as "the key you pasted"
3. **Advises rotation**: revoke or rotate it in the provider's dashboard and check the usage log for unexpected calls
4. **Offers a safe path**: environment variables or a secret manager, and works from public sources in the meantime
5. **Flags other secrets** in the same message, by type only
6. **Moves on** with the original task once you confirm rotation

## Tone

States the risk once, plainly. No lecturing and no repeated warnings. If you insist on using the key, it declines in one sentence and offers the alternative again.

## Limits

- Claude can't revoke keys itself.
- Keys sent in chat may already be logged by the platform, so rotation is the only real fix.

## Install

**Claude Code:** `cp -r skills/secret-exposure-response ~/.claude/skills/` from the repo root, then restart Claude Code.

**Claude.ai / Desktop:** zip the `secret-exposure-response` folder and upload it under **Settings → Capabilities → Skills**.

Full instructions are in [`SKILL.md`](./SKILL.md).
