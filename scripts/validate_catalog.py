#!/usr/bin/env python3
"""
Validate plugin catalog by counting actual agents and commands.
Generates a report showing current counts and identifies documentation discrepancies.
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Base directory - plugins folder
MARKETPLACE_ROOT = Path(__file__).parent.parent
PLUGINS_DIR = MARKETPLACE_ROOT / "plugins"
WIKI_DIR = MARKETPLACE_ROOT / "wiki"

def count_plugin_files(plugin_path, subdir):
    """Count markdown files in a plugin's agents or commands directory (including subdirectories)."""
    target_dir = plugin_path / subdir
    if not target_dir.exists():
        return 0
    # Use ** to search recursively
    return len(list(target_dir.glob("**/*.md")))

def scan_plugins():
    """Scan all plugins and count agents and commands."""
    plugins = {}
    total_agents = 0
    total_commands = 0

    for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
        if not plugin_dir.is_dir() or plugin_dir.name.startswith('.'):
            continue

        agent_count = count_plugin_files(plugin_dir, "agents")
        command_count = count_plugin_files(plugin_dir, "commands")

        plugins[plugin_dir.name] = {
            "agents": agent_count,
            "commands": command_count
        }

        total_agents += agent_count
        total_commands += command_count

    return plugins, total_agents, total_commands

def find_documentation_claims(file_path, search_patterns):
    """Find lines in documentation that make claims about counts."""
    if not file_path.exists():
        return []

    content = file_path.read_text()
    lines = content.split('\n')
    claims = []

    for i, line in enumerate(lines, 1):
        for pattern in search_patterns:
            if pattern.lower() in line.lower():
                claims.append({
                    "line": i,
                    "content": line.strip()
                })
                break

    return claims

def generate_report(plugins, total_agents, total_commands):
    """Generate a comprehensive validation report."""
    plugin_count = len(plugins)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("=" * 80)
    print("DOTCLAUDE MARKETPLACE CATALOG VALIDATION REPORT")
    print("=" * 80)
    print(f"Generated: {timestamp}")
    print(f"Marketplace Root: {MARKETPLACE_ROOT}")
    print()

    print("📊 ACTUAL COUNTS")
    print("-" * 80)
    print(f"Total Plugins:  {plugin_count}")
    print(f"Total Agents:   {total_agents}")
    print(f"Total Commands: {total_commands}")
    print()

    print("📦 PER-PLUGIN BREAKDOWN")
    print("-" * 80)
    print(f"{'Plugin':<30} {'Agents':>8} {'Commands':>10}")
    print("-" * 80)
    for plugin_name in sorted(plugins.keys()):
        data = plugins[plugin_name]
        print(f"{plugin_name:<30} {data['agents']:>8} {data['commands']:>10}")
    print("-" * 80)
    print(f"{'TOTAL':<30} {total_agents:>8} {total_commands:>10}")
    print()

    print("🔍 DOCUMENTATION CLAIMS ANALYSIS")
    print("-" * 80)

    # Check documentation files for problematic claims
    search_patterns = ["100+", "100 ", "hundred"]
    files_to_check = [
        ("README.md", MARKETPLACE_ROOT / "README.md"),
        ("wiki/Home.md", WIKI_DIR / "Home.md"),
        ("wiki/Plugin-Catalog.md", WIKI_DIR / "Plugin-Catalog.md")
    ]

    discrepancies_found = False
    for file_label, file_path in files_to_check:
        claims = find_documentation_claims(file_path, search_patterns)
        if claims:
            discrepancies_found = True
            print(f"\n{file_label}:")
            for claim in claims:
                print(f"  Line {claim['line']}: {claim['content']}")

    if not discrepancies_found:
        print("✅ No documentation discrepancies found!")
    else:
        print("\n⚠️  Found potential documentation discrepancies")
        print("    Review lines above and update with actual counts:")
        print(f"    - Use '{total_agents} specialized agents' or '{total_agents} agents'")
        print(f"    - Use '{total_commands} commands' or '70+ commands'")

    print()
    print("=" * 80)

    return {
        "plugin_count": plugin_count,
        "total_agents": total_agents,
        "total_commands": total_commands,
        "plugins": plugins,
        "timestamp": timestamp,
        "has_discrepancies": discrepancies_found
    }

def save_json_report(data, output_path):
    """Save validation data as JSON for automation."""
    output_path.write_text(json.dumps(data, indent=2))
    print(f"📄 JSON report saved to: {output_path}")

def generate_badge_data(total_agents, total_commands):
    """Generate data for README badges."""
    badge_data = {
        "schemaVersion": 1,
        "label": "agents",
        "message": str(total_agents),
        "color": "blue"
    }

    print("\n📛 BADGE DATA (for README)")
    print("-" * 80)
    print(f"Agents: {total_agents}")
    print(f"Commands: {total_commands}")
    print(f"Badge JSON: {json.dumps(badge_data)}")
    print()

def main():
    """Main validation function."""
    try:
        plugins, total_agents, total_commands = scan_plugins()

        # Generate report
        data = generate_report(plugins, total_agents, total_commands)

        # Save JSON report
        output_path = MARKETPLACE_ROOT / "scripts" / "catalog_validation.json"
        save_json_report(data, output_path)

        # Generate badge data
        generate_badge_data(total_agents, total_commands)

        # Exit with error code if discrepancies found
        if data["has_discrepancies"]:
            print("❌ VALIDATION FAILED: Documentation discrepancies detected")
            sys.exit(1)
        else:
            print("✅ VALIDATION PASSED: All documentation is accurate")
            sys.exit(0)

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(2)

if __name__ == "__main__":
    main()
