#!/usr/bin/env python3
"""
Auto-generate comprehensive agent and command catalog markdown files.

Creates formatted catalog documents with:
- Per-plugin agent listings with descriptions
- Per-plugin command listings with examples
- Summary statistics
- Cross-references

Designed to be run as part of CI/CD or pre-commit hooks.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

MARKETPLACE_ROOT = Path(__file__).parent.parent
PLUGINS_DIR = MARKETPLACE_ROOT / "plugins"
OUTPUT_DIR = MARKETPLACE_ROOT / "docs"

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown file."""
    if not content.startswith('---\n'):
        return {}

    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return {}

    # Simple YAML parsing for key-value pairs
    frontmatter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip().strip('"\'')

    return frontmatter

def parse_agent_file(file_path):
    """Parse an agent file and extract metadata."""
    content = file_path.read_text()
    metadata = extract_frontmatter(content)

    # Extract description from content if not in frontmatter
    description = metadata.get('description', '')
    if not description:
        lines = content.split('\n')
        for line in lines:
            if line.strip() and not line.startswith('#') and not line.startswith('---'):
                description = line.strip()
                break

    return {
        'name': file_path.stem,
        'description': description,
        'model': metadata.get('model', 'sonnet'),
        'tags': metadata.get('tags', '').split(',') if metadata.get('tags') else []
    }

def parse_command_file(file_path):
    """Parse a command file and extract metadata."""
    content = file_path.read_text()

    # Extract first heading and description
    lines = content.split('\n')
    title = ''
    description = ''

    for i, line in enumerate(lines):
        if line.startswith('# '):
            title = line[2:].strip()
        elif title and line.strip() and not line.startswith('#'):
            description = line.strip()
            break

    return {
        'name': file_path.stem,
        'title': title or file_path.stem,
        'description': description,
        'path': str(file_path.relative_to(PLUGINS_DIR))
    }

def scan_plugin(plugin_dir):
    """Scan a plugin directory for agents and commands."""
    agents = []
    commands = []

    # Scan agents
    agents_dir = plugin_dir / "agents"
    if agents_dir.exists():
        for agent_file in sorted(agents_dir.glob("*.md")):
            agents.append(parse_agent_file(agent_file))

    # Scan commands (recursively)
    commands_dir = plugin_dir / "commands"
    if commands_dir.exists():
        for command_file in sorted(commands_dir.glob("**/*.md")):
            commands.append(parse_command_file(command_file))

    return agents, commands

def generate_agent_catalog():
    """Generate comprehensive agent catalog."""
    print("Generating agent catalog...")

    catalog = {}
    total_agents = 0

    for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
        if not plugin_dir.is_dir() or plugin_dir.name.startswith('.'):
            continue

        agents, _ = scan_plugin(plugin_dir)
        if agents:
            catalog[plugin_dir.name] = agents
            total_agents += len(agents)

    # Generate markdown
    markdown = f"""# Agent Catalog

**Auto-generated agent reference for DotClaude Marketplace**

Total Agents: **{total_agents}** across **{len(catalog)}** plugins

Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Table of Contents

"""

    # Add TOC
    for plugin_name in sorted(catalog.keys()):
        plugin_display = plugin_name.replace('-', ' ').title()
        markdown += f"- [{plugin_display}](#{plugin_name}) ({len(catalog[plugin_name])} agents)\n"

    markdown += "\n---\n\n"

    # Add detailed listings
    for plugin_name in sorted(catalog.keys()):
        plugin_display = plugin_name.replace('-', ' ').title()
        agents = catalog[plugin_name]

        markdown += f"## {plugin_display}\n\n"
        markdown += f"**Plugin:** `{plugin_name}`  \n"
        markdown += f"**Agents:** {len(agents)}\n\n"

        for agent in sorted(agents, key=lambda x: x['name']):
            markdown += f"### {agent['name']}\n\n"
            if agent['description']:
                markdown += f"{agent['description']}\n\n"
            markdown += f"**Model:** `{agent['model']}`  \n"
            if agent['tags']:
                markdown += f"**Tags:** {', '.join(agent['tags'])}  \n"
            markdown += f"**Location:** `.claude/agents/{agent['name']}.md`\n\n"
            markdown += "---\n\n"

    # Add footer
    markdown += f"""
---

## Statistics by Model

"""

    # Count agents by model
    model_counts = {}
    for agents in catalog.values():
        for agent in agents:
            model = agent['model']
            model_counts[model] = model_counts.get(model, 0) + 1

    for model, count in sorted(model_counts.items(), key=lambda x: -x[1]):
        markdown += f"- **{model}**: {count} agents\n"

    markdown += "\n---\n\n"
    markdown += "*This catalog is automatically generated from plugin agent files.*\n"
    markdown += "*To update, run: `python scripts/generate_catalog.py`*\n"

    return markdown

def generate_command_catalog():
    """Generate comprehensive command catalog."""
    print("Generating command catalog...")

    catalog = {}
    total_commands = 0

    for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
        if not plugin_dir.is_dir() or plugin_dir.name.startswith('.'):
            continue

        _, commands = scan_plugin(plugin_dir)
        if commands:
            catalog[plugin_dir.name] = commands
            total_commands += len(commands)

    # Generate markdown
    markdown = f"""# Command Catalog

**Auto-generated command reference for DotClaude Marketplace**

Total Commands: **{total_commands}** across **{len(catalog)}** plugins

Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Table of Contents

"""

    # Add TOC
    for plugin_name in sorted(catalog.keys()):
        plugin_display = plugin_name.replace('-', ' ').title()
        markdown += f"- [{plugin_display}](#{plugin_name}) ({len(catalog[plugin_name])} commands)\n"

    markdown += "\n---\n\n"

    # Add detailed listings
    for plugin_name in sorted(catalog.keys()):
        plugin_display = plugin_name.replace('-', ' ').title()
        commands = catalog[plugin_name]

        markdown += f"## {plugin_display}\n\n"
        markdown += f"**Plugin:** `{plugin_name}`  \n"
        markdown += f"**Commands:** {len(commands)}\n\n"

        for command in sorted(commands, key=lambda x: x['name']):
            command_path = command['name']
            if '/' in command['path']:  # Workflow command
                parts = command['path'].split('/')
                command_path = f"/{parts[-2]}:{command['name']}"
            else:
                command_path = f"/{command['name']}"

            markdown += f"### `{command_path}`\n\n"
            if command['description']:
                markdown += f"{command['description']}\n\n"
            markdown += f"**Location:** `.claude/commands/{command['path']}`\n\n"

            # Add example usage
            markdown += f"**Example:**\n```bash\n{command_path} <args>\n```\n\n"
            markdown += "---\n\n"

    # Add footer
    markdown += "\n---\n\n"
    markdown += "*This catalog is automatically generated from plugin command files.*\n"
    markdown += "*To update, run: `python scripts/generate_catalog.py`*\n"

    return markdown

def main():
    """Generate all catalog files."""
    print("=" * 80)
    print("CATALOG GENERATION")
    print("=" * 80)
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"✓ Output directory: {OUTPUT_DIR}")
    print()

    # Generate agent catalog
    agent_catalog = generate_agent_catalog()
    agent_file = OUTPUT_DIR / "AGENT_CATALOG.md"
    agent_file.write_text(agent_catalog)
    print(f"✓ Created: {agent_file}")
    print()

    # Generate command catalog
    command_catalog = generate_command_catalog()
    command_file = OUTPUT_DIR / "COMMAND_CATALOG.md"
    command_file.write_text(command_catalog)
    print(f"✓ Created: {command_file}")
    print()

    print("=" * 80)
    print("✅ CATALOG GENERATION COMPLETE")
    print("=" * 80)
    print()
    print(f"Generated files:")
    print(f"  - {agent_file}")
    print(f"  - {command_file}")
    print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
