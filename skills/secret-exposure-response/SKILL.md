---
name: secret-exposure-response
description: When a user pastes an API key, password, token or other secret into a chat, flag the exposure, advise rotating it, and avoid using or repeating it. Use whenever a message contains what looks like a live credential.
---

# Secret exposure response

A credential pasted into a chat is now stored in the conversation. The user should treat it as exposed. The response should be calm and specific, not alarmist.

## What to do

1. **Do not use the secret.** Do not call the service with it, even if asked. Explain that the key is exposed and should be rotated first.
2. **Do not repeat it.** Refer to it as "the key you pasted". Never echo any part of it back, even partially.
3. **Advise rotation.** Tell the user to revoke or rotate the key in the provider's dashboard, and to check its usage log for unexpected calls.
4. **Offer a safe path.** Explain how to store the key outside chat (an environment variable or the service's secret manager), and that you can work from public sources in the meantime.
5. **Check for others.** If the same message contains other secrets, list them as "also exposed" by type only.
6. **Move on.** Once the user confirms rotation, carry on with the original task.

## Tone

State the risk once, plainly. Do not lecture or repeat the warning in every reply. If the user insists on using the key anyway, decline in one sentence and offer the alternative again.

## Limits

- You cannot revoke a key yourself.
- Keys sent in chat may already be logged by the platform, so rotation is the only real fix.
