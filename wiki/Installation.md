# Installation Guide

Complete guide to installing and configuring the DotClaude Marketplace and its plugins.

## Prerequisites

- **Claude Code** (latest version)
- **Git** installed and configured
- Internet connection for downloading plugins

## Installation Methods

### Method 1: Complete Marketplace (Recommended)

Install all 14 plugins at once:

```bash
/plugin marketplace add dotclaude/marketplace
```

**What this does:**
- Downloads the marketplace repository
- Installs all 14 plugins automatically
- Makes 100+ commands immediately available
- Registers 100+ specialized agents

**Installation time:** ~30 seconds

---

### Method 2: Individual Plugin Installation

Install specific plugins only:

```bash
# Install single plugin
/plugin install dotclaude/marketplace/plugins/frontend-excellence

# Install multiple plugins
/plugin install dotclaude/marketplace/plugins/infra-pipeline
/plugin install dotclaude/marketplace/plugins/observability-ops
/plugin install dotclaude/marketplace/plugins/cli-mastery
```

**When to use:**
- You only need specific functionality
- Limited disk space
- Want to try plugins incrementally

---

## Verification

After installation, verify plugins are available:

```bash
# List installed plugins
/plugin list

# Try a command from each category
/analyze "test question" simple              # personalities
/react "build component"                     # frontend-excellence
/infra "setup infrastructure"                # infra-pipeline
/data "transform JSON"                       # data-intelligence
```

## Plugin Categories & Installation

### Core Intelligence Plugins

```bash
# All core intelligence plugins
/plugin install dotclaude/marketplace/plugins/cognitive-orchestration
/plugin install dotclaude/marketplace/plugins/adaptive-learning
/plugin install dotclaude/marketplace/plugins/dev-accelerator
/plugin install dotclaude/marketplace/plugins/insight-engine
/plugin install dotclaude/marketplace/plugins/personalities
```

**Best for:** Learning, decision-making, development workflows, innovation

---

### Infrastructure & Operations

```bash
# Infrastructure and monitoring
/plugin install dotclaude/marketplace/plugins/infra-pipeline
/plugin install dotclaude/marketplace/plugins/observability-ops
```

**Best for:** DevOps engineers, SREs, infrastructure teams

---

### Development Tools

```bash
# Frontend and backend development
/plugin install dotclaude/marketplace/plugins/frontend-excellence
/plugin install dotclaude/marketplace/plugins/backend-security
/plugin install dotclaude/marketplace/plugins/cli-mastery
```

**Best for:** Software developers, full-stack engineers

---

### Data & Distributed Systems

```bash
# Data processing and queues
/plugin install dotclaude/marketplace/plugins/data-intelligence
/plugin install dotclaude/marketplace/plugins/queue-orchestrator
```

**Best for:** Data engineers, backend architects

---

### Product & Project Management

```bash
# UX and project management
/plugin install dotclaude/marketplace/plugins/ux-product
/plugin install dotclaude/marketplace/plugins/project-delivery
```

**Best for:** Product managers, UX designers, project managers

---

## Configuration

### Default Configuration

Plugins work out-of-the-box with sensible defaults. No configuration required.

### Custom Configuration

Some plugins support optional configuration:

**Example: Observability Ops**
```bash
# Set default monitoring platform
export DOTCLAUDE_MONITORING_PLATFORM="datadog"

# Set default environment
export DOTCLAUDE_DEFAULT_ENV="production"
```

**Example: Infra Pipeline**
```bash
# Set default IaC tool
export DOTCLAUDE_IAC_TOOL="terraform"

# Set default cloud provider
export DOTCLAUDE_CLOUD_PROVIDER="aws"
```

See individual plugin READMEs for configuration options.

---

## Updating Plugins

### Update All Plugins

```bash
/plugin marketplace update dotclaude/marketplace
```

### Update Individual Plugin

```bash
/plugin update dotclaude/marketplace/plugins/frontend-excellence
```

### Check for Updates

```bash
/plugin marketplace check-updates
```

---

## Uninstallation

### Remove Specific Plugin

```bash
/plugin uninstall frontend-excellence
```

### Remove All Marketplace Plugins

```bash
/plugin marketplace remove dotclaude/marketplace
```

**Warning:** This removes all 14 plugins and their commands.

---

## Troubleshooting

### Plugin Not Found

**Problem:** `/plugin marketplace add dotclaude/marketplace` fails

**Solutions:**
1. Check internet connection
2. Verify Git is installed: `git --version`
3. Try direct plugin installation
4. Check Claude Code version

### Commands Not Available

**Problem:** Installed plugin but commands don't work

**Solutions:**
1. Restart Claude Code
2. Verify installation: `/plugin list`
3. Check plugin directory exists
4. Reinstall plugin

### Permission Errors

**Problem:** Permission denied during installation

**Solutions:**
1. Check filesystem permissions
2. Ensure write access to plugin directory
3. Run with appropriate permissions

### Slow Installation

**Problem:** Installation takes too long

**Solutions:**
1. Check internet speed
2. Try individual plugins instead of marketplace
3. Check disk space availability
4. Use cached installation if available

---

## Advanced Installation

### Offline Installation

1. Clone repository manually:
```bash
git clone https://github.com/dotclaude/marketplace.git
```

2. Install from local path:
```bash
/plugin marketplace add file:///path/to/marketplace
```

### Development Installation

For plugin development:

```bash
# Clone with all branches
git clone --recurse-submodules https://github.com/dotclaude/marketplace.git

# Install in development mode
/plugin marketplace add file:///path/to/marketplace --dev
```

### Custom Plugin Location

Install to custom directory:

```bash
export CLAUDE_CODE_PLUGINS_DIR="/custom/path"
/plugin marketplace add dotclaude/marketplace
```

---

## Next Steps

After installation:

1. **[Quick Start Guide](./Quick-Start.md)** - Try your first commands
2. **[Plugin Catalog](./Plugin-Catalog.md)** - Explore all plugins
3. **[Workflow Patterns](./Workflow-Patterns.md)** - Learn real-world usage
4. **[Command Reference](./Command-Reference.md)** - Browse all commands

---

## Getting Help

- **[Troubleshooting Guide](./Troubleshooting.md)** - Common issues
- **[GitHub Issues](https://github.com/dotclaude/marketplace/issues)** - Report problems
- **[Discussions](https://github.com/dotclaude/marketplace/discussions)** - Ask questions

---

**Installation complete?** Head to the [Quick Start Guide](./Quick-Start.md) to begin using your new plugins!
