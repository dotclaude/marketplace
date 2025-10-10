#!/usr/bin/env python3
"""
Migrate wiki/ directory files to GitHub wiki format.

GitHub wikis have specific requirements:
1. Separate git repository (*.wiki.git)
2. Flat structure (no subdirectories)
3. Special _Sidebar.md for navigation
4. Links without .md extensions

This script prepares wiki files for GitHub wiki migration.
"""

import re
import sys
from pathlib import Path
from datetime import datetime

MARKETPLACE_ROOT = Path(__file__).parent.parent
WIKI_DIR = MARKETPLACE_ROOT / "wiki"
OUTPUT_DIR = MARKETPLACE_ROOT / "wiki-github"

def sanitize_wiki_name(filename):
    """Convert filename to GitHub wiki page name format."""
    # Remove .md extension
    name = filename.replace('.md', '')
    # GitHub wiki uses - for spaces and special chars
    return name

def rewrite_wiki_links(content):
    """
    Rewrite internal wiki links for GitHub wiki format.

    GitHub wiki links:
    - Don't use .md extension
    - Don't use ./ or ../ prefixes
    - Use [[Page Name]] syntax or [Text](Page-Name) format
    """
    # Convert [[./Page.md]] or [[Page.md]] to [[Page]]
    content = re.sub(r'\[\[\.?/?([\w-]+)\.md\]\]', r'[[\1]]', content)

    # Convert [Text](./Page.md) or [Text](Page.md) to [Text](Page)
    content = re.sub(r'\[([^\]]+)\]\(\.?/?([\w-]+)\.md\)', r'[\1](\2)', content)

    # Convert relative paths in links [Text](./wiki/Page.md) to [Text](Page)
    content = re.sub(r'\[([^\]]+)\]\(\.?/?wiki/([\w-]+)\.md\)', r'[\1](\2)', content)

    return content

def generate_sidebar(wiki_files):
    """Generate _Sidebar.md for GitHub wiki navigation."""
    sidebar_content = """# Navigation

## Quick Start
- [Home](Home)
- [Installation](Installation)
- [Plugin Catalog](Plugin-Catalog)

## Documentation
- [Command Reference](Command-Reference)
- [Agent Reference](Agent-Reference)
- [Security Guide](Security)
- [Troubleshooting](Troubleshooting)

## Guides
- [Workflow Patterns](Workflow-Patterns)
- [Integration Guide](Integration)
- [Quick Start](Quick-Start)

---

[📦 Marketplace](https://github.com/dotclaude/marketplace)
"""
    return sidebar_content

def process_wiki_file(file_path, output_dir):
    """Process a single wiki file for GitHub wiki format."""
    content = file_path.read_text()

    # Rewrite links
    content = rewrite_wiki_links(content)

    # Add metadata comment at top
    metadata = f"<!-- Migrated from {file_path.name} on {datetime.now().strftime('%Y-%m-%d')} -->\n\n"
    content = metadata + content

    # Output with same filename
    output_path = output_dir / file_path.name
    output_path.write_text(content)

    print(f"✓ Processed: {file_path.name} → {output_path.name}")
    return output_path

def create_migration_guide(output_dir):
    """Create a guide for completing the migration."""
    guide_content = """# GitHub Wiki Migration Guide

This directory contains wiki files prepared for GitHub wiki migration.

## Migration Steps

### 1. Clone the GitHub Wiki Repository

```bash
# Clone the wiki repository (separate from main repo)
git clone https://github.com/dotclaude/marketplace.wiki.git
cd marketplace.wiki.git
```

### 2. Copy Prepared Files

```bash
# Copy all files from wiki-github/ to the wiki repository
cp ../marketplace/wiki-github/*.md .
```

### 3. Commit and Push

```bash
# Add all files
git add .

# Commit
git commit -m "docs: migrate wiki from main repository

- Migrated Home, Installation, and Plugin-Catalog pages
- Added _Sidebar for navigation
- Rewritten links for GitHub wiki format
- All documentation now accurate (78 agents, 70 commands)
"

# Push to wiki
git push origin master
```

### 4. Verify on GitHub

Visit https://github.com/dotclaude/marketplace/wiki to verify:
- [ ] All pages load correctly
- [ ] Sidebar navigation works
- [ ] Internal links function properly
- [ ] No broken images or references

### 5. Update Main Repository

After successful migration, update main repository README.md:

```markdown
## 📚 Documentation

Visit our [Wiki](https://github.com/dotclaude/marketplace/wiki) for complete documentation:
- [Installation Guide](https://github.com/dotclaude/marketplace/wiki/Installation)
- [Plugin Catalog](https://github.com/dotclaude/marketplace/wiki/Plugin-Catalog)
- [Command Reference](https://github.com/dotclaude/marketplace/wiki/Command-Reference)
```

## Maintaining Bi-Directional Sync (Optional)

During transition, you can maintain both:
1. Keep wiki/ directory in main repo as backup
2. Set up GitHub Action to sync changes (advanced)
3. After stable migration, archive wiki/ directory

## Rollback Plan

If issues occur:
1. Wiki changes are in separate git repository
2. Can revert commits in wiki.git repository
3. Original wiki/ directory unchanged in main repo

## Notes

- GitHub wikis are public if repository is public
- Wiki has separate permissions from main repository
- Anyone with write access can edit wiki pages
- Wiki changes don't trigger CI/CD workflows

---

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    guide_path = output_dir / "MIGRATION_GUIDE.md"
    guide_path.write_text(guide_content)
    print(f"✓ Created: {guide_path.name}")

def main():
    """Main migration preparation function."""
    print("=" * 80)
    print("GITHUB WIKI MIGRATION PREPARATION")
    print("=" * 80)
    print(f"Source: {WIKI_DIR}")
    print(f"Output: {OUTPUT_DIR}")
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"✓ Created output directory: {OUTPUT_DIR}")
    print()

    # Get all wiki markdown files
    wiki_files = list(WIKI_DIR.glob("*.md"))
    if not wiki_files:
        print(f"❌ No wiki files found in {WIKI_DIR}")
        sys.exit(1)

    print(f"Found {len(wiki_files)} wiki files to process:")
    print()

    # Process each file
    processed_files = []
    for wiki_file in sorted(wiki_files):
        output_file = process_wiki_file(wiki_file, OUTPUT_DIR)
        processed_files.append(output_file)

    print()

    # Generate sidebar
    sidebar_content = generate_sidebar(processed_files)
    sidebar_path = OUTPUT_DIR / "_Sidebar.md"
    sidebar_path.write_text(sidebar_content)
    print(f"✓ Generated: {sidebar_path.name}")
    print()

    # Create migration guide
    create_migration_guide(OUTPUT_DIR)
    print()

    print("=" * 80)
    print("✅ MIGRATION PREPARATION COMPLETE")
    print("=" * 80)
    print()
    print(f"Next steps:")
    print(f"1. Review files in: {OUTPUT_DIR}/")
    print(f"2. Read migration guide: {OUTPUT_DIR}/MIGRATION_GUIDE.md")
    print(f"3. Clone wiki repo: git clone https://github.com/dotclaude/marketplace.wiki.git")
    print(f"4. Copy files and push to wiki")
    print()
    print(f"Files prepared: {len(processed_files) + 1} (including _Sidebar.md)")
    print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
