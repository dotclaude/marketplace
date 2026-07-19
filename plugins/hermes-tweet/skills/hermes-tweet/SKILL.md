---
name: hermes-tweet
description: "Guide Hermes Agent X/Twitter workflows for route discovery, public tweet reads, and approval-gated actions through Xquik. Use when the user asks to install Hermes Tweet, inspect X/Twitter data, or prepare social media actions with Hermes Agent."
argument-hint: "<task>"
---

# Hermes Tweet

Hermes Tweet adds X/Twitter workflows to Hermes Agent. Use it for social discovery, public tweet reads, and explicitly approved write actions.

## Required Argument

`<task>` describes the Hermes Tweet workflow the user wants.

If the task is missing, ask once for the X/Twitter workflow they want to run.

## Steps

1. Confirm whether the user needs installation help, route discovery, reads, or write actions.
2. Install Hermes Tweet in the Hermes Agent environment when needed:

   ```bash
   hermes plugins install Xquik-dev/hermes-tweet --enable
   ```

3. Configure `XQUIK_API_KEY` in the local environment before read workflows.
4. Require explicit user approval before any write workflow.
5. Confirm `HERMES_TWEET_ENABLE_ACTIONS=true` is intentionally configured before write actions.
6. Search bundled route metadata with `tweet_explore` before choosing a route.
7. Read public X/Twitter data with `tweet_read` after credentials are configured.
8. Execute write actions with `tweet_action` only when approval and action enablement are both present.
9. Keep credentials in the local environment. Never place them in prompts, logs, generated files, or repository content.

## Source

Full package, tests, route metadata, and release notes live at `https://github.com/Xquik-dev/hermes-tweet`.

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
