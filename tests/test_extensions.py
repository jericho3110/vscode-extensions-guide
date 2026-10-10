import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from extensions import (
    MAX_LIST_BYTES,
    parse_list,
    parse_recommendations,
    parse_txt,
    plan,
    strip_jsonc,
    validate,
)


class ValidateTests(unittest.TestCase):
    def test_accepts_real_ids(self):
        for ok in ["ms-python.python", "rust-lang.rust-analyzer", "vadimcn.vscode-lldb",
                   "ms-python.python@2026.8.0", "golang.Go"]:
            self.assertEqual(validate(ok), ok)

    def test_rejects_anything_cmd_exe_could_interpret(self):
        # On Windows `code` is a .cmd file, so these would reach cmd.exe's parser.
        for bad in ['ms-python.python & calc', 'a.b"', "a.b|whoami", "a.b%PATH%", "a.b^",
                    "--force", "../evil.vsix", "a.b\nc.d", "nopublisher", "a.b@latest", ""]:
            with self.assertRaises(ValueError, msg=bad):
                validate(bad)


class ParseTests(unittest.TestCase):
    def test_txt_with_comments_and_blanks(self):
        self.assertEqual(parse_txt("# python\nms-python.python\n\n charliermarsh.ruff  # linter\n"),
                         ["ms-python.python", "charliermarsh.ruff"])

    def test_txt_rejects_bad_line(self):
        with self.assertRaises(ValueError):
            parse_txt("ms-python.python\nevil.ext & del x\n")

    def test_jsonc_comments_and_trailing_commas(self):
        text = """{
          // See https://go.microsoft.com/fwlink/?LinkId=827846
          "recommendations": [
            "ms-python.python", /* the core */
            "charliermarsh.ruff",
          ],
        }"""
        self.assertEqual(parse_recommendations(text), ["ms-python.python", "charliermarsh.ruff"])

    def test_jsonc_keeps_slashes_inside_strings(self):
        self.assertEqual(strip_jsonc('{"u": "https://x.org/a"}'), '{"u": "https://x.org/a"}')

    def test_recommendations_must_be_strings(self):
        with self.assertRaises(ValueError):
            parse_recommendations('{"recommendations": [1, 2]}')

    def test_oversized_list_refused(self):
        with self.assertRaises(ValueError):
            parse_list("x.txt", "a.b\n" * (MAX_LIST_BYTES // 4 + 1))


class PlanTests(unittest.TestCase):
    def test_case_insensitive_versions_ignored_duplicates_dropped(self):
        to_install, present = plan(
            ["MS-Python.Python@2026.8.0", "rust-lang.rust-analyzer", "rust-lang.rust-analyzer"],
            ["ms-python.python"])
        self.assertEqual(to_install, ["rust-lang.rust-analyzer"])
        self.assertEqual(present, ["MS-Python.Python@2026.8.0"])

    def test_repo_recommendations_file_is_valid(self):
        recs = parse_list("extensions.json", (ROOT / ".vscode" / "extensions.json").read_text(encoding="utf-8"))
        self.assertIn("charliermarsh.ruff", recs)

    def test_example_list_is_valid(self):
        self.assertGreaterEqual(len(parse_list("x.txt", (ROOT / "examples" / "multi-language.txt").read_text(encoding="utf-8"))), 10)


if __name__ == "__main__":
    unittest.main()
