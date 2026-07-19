#!/usr/bin/env python3
"""
Validate plugin catalog by counting actual agents and commands.
Generates a report showing current counts and identifies documentation discrepancies.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Base directory - plugins folder
MARKETPLACE_ROOT = Path(__file__).parent.parent
PLUGINS_DIR = MARKETPLACE_ROOT / "plugins"


README_COUNT_PATTERNS = {
    "plugins": [
        re.compile(r"badge/plugins-(\d+)-"),
        re.compile(r"with (\d+) specialized plugins", re.IGNORECASE),
        re.compile(r"Plugin Ecosystem \((\d+) Plugins\)", re.IGNORECASE),
        re.compile(r"Install (?:the complete marketplace \(all |all )(\d+) plugins", re.IGNORECASE),
        re.compile(r"- \*\*(\d+) Plugins\*\* covering", re.IGNORECASE),
        re.compile(r"access (\d+) specialized plugins", re.IGNORECASE),
    ],
    "agents": [
        re.compile(r"badge/agents-(\d+)-"),
        re.compile(r"- \*\*(\d+) Specialized Agents\*\*", re.IGNORECASE),
        re.compile(r"and (\d+) expert agents", re.IGNORECASE),
    ],
    "commands": [
        re.compile(r"badge/commands-(\d+)-"),
        re.compile(r"- \*\*(\d+) Commands\*\*", re.IGNORECASE),
        re.compile(r"plugins, (\d+) commands", re.IGNORECASE),
    ],
}


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

def find_readme_count_discrepancies(file_path, expected_counts):
    """Find stale marketplace totals in the README summary."""
    if not file_path.exists():
        return [
            {
                "line": 0,
                "content": "README.md is missing",
                "kind": "readme",
                "claimed": None,
                "expected": None,
            }
        ]

    content = file_path.read_text()
    lines = content.split('\n')
    discrepancies = []

    for line_number, line in enumerate(lines, 1):
        for kind, patterns in README_COUNT_PATTERNS.items():
            for pattern in patterns:
                match = pattern.search(line)
                if match is None:
                    continue

                claimed = int(match.group(1))
                expected = expected_counts[kind]
                if claimed != expected:
                    discrepancies.append({
                        "line": line_number,
                        "content": line.strip(),
                        "kind": kind,
                        "claimed": claimed,
                        "expected": expected,
                    })

    return discrepancies


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

    expected_counts = {
        "plugins": plugin_count,
        "agents": total_agents,
        "commands": total_commands,
    }
    discrepancies = find_readme_count_discrepancies(
        MARKETPLACE_ROOT / "README.md",
        expected_counts,
    )

    if not discrepancies:
        print("✅ No documentation discrepancies found!")
    else:
        print("\nREADME.md:")
        for discrepancy in discrepancies:
            print(
                f"  Line {discrepancy['line']}: "
                f"{discrepancy['kind']} claims {discrepancy['claimed']}, "
                f"expected {discrepancy['expected']}"
            )
            print(f"    {discrepancy['content']}")
        print("\n⚠️  Found documentation discrepancies")
        print("    Update README marketplace totals to match the catalog.")

    print()
    print("=" * 80)

    return {
        "plugin_count": plugin_count,
        "total_agents": total_agents,
        "total_commands": total_commands,
        "plugins": plugins,
        "timestamp": timestamp,
        "has_discrepancies": bool(discrepancies),
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
