import tempfile
import unittest
from pathlib import Path

from validate_catalog import find_readme_count_discrepancies


class ReadmeCountValidationTests(unittest.TestCase):
    def test_accepts_matching_summary_counts(self):
        content = """
[![Plugins](https://img.shields.io/badge/plugins-18-blue)]
[![Agents](https://img.shields.io/badge/agents-91-green)]
[![Commands](https://img.shields.io/badge/commands-85-orange)]
Install the marketplace and access 18 specialized plugins, 85 commands, and 91 expert agents.
"""
        self.assertEqual(self._validate(content), [])

    def test_reports_each_stale_summary_count(self):
        content = """
[![Plugins](https://img.shields.io/badge/plugins-17-blue)]
[![Agents](https://img.shields.io/badge/agents-90-green)]
[![Commands](https://img.shields.io/badge/commands-82-orange)]
"""
        discrepancies = self._validate(content)

        self.assertEqual(
            [(item["kind"], item["claimed"], item["expected"]) for item in discrepancies],
            [
                ("plugins", 17, 18),
                ("agents", 90, 91),
                ("commands", 82, 85),
            ],
        )

    @staticmethod
    def _validate(content):
        expected = {"plugins": 18, "agents": 91, "commands": 85}
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(directory) / "README.md"
            readme.write_text(content)
            return find_readme_count_discrepancies(readme, expected)


if __name__ == "__main__":
    unittest.main()
