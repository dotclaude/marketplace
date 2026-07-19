# Hermes Tweet

**Hermes Agent X/Twitter workflows with guarded read and action guidance**

Guide social discovery, public tweet reads, and explicitly approved write actions with Hermes Tweet.

## Installation

```bash
# Add the DotClaude marketplace
/plugin marketplace add dotclaude/marketplace

# Install this plugin when your Claude Code build prompts for individual installs
/plugin install hermes-tweet@dotclaude-plugins
```

Install the Hermes Agent package where Hermes runs:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

## Quick Start

```bash
"Explore available Hermes Tweet routes for a launch-monitoring task"
"Read public X/Twitter posts for this campaign query"
"Prepare an approval-gated reply workflow with Hermes Tweet"
```

## Use Cases

- **Route Discovery** - Inspect bundled route metadata before choosing a workflow
- **Public Reads** - Read public X/Twitter data after `XQUIK_API_KEY` is configured
- **Action Preparation** - Prepare write actions only after explicit user approval
- **Safety Checks** - Keep credentials in the local environment and out of prompts

## License

MIT License - see LICENSE file for details

## Source

Hermes Tweet source and tests live at [Xquik-dev/hermes-tweet](https://github.com/Xquik-dev/hermes-tweet).

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
