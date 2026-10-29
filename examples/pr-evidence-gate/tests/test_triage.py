"""Tests for the deliberately narrow, offline PR evidence gate."""
import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from triage import InvalidSnapshot, analyze, render_markdown  # noqa: E402

EXAMPLE = Path(__file__).resolve().parents[1] / "sample-approved.json"


class OfflineTriageTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def test_green_checks_still_require_human_review(self):
        result = analyze(self.data)
        self.assertEqual(result["decision"], "HUMAN_REVIEW_REQUIRED")
        self.assertEqual(result["ignored_own_comment_echoes"], 1)
        self.assertEqual(result["external_comments_to_review"], 1)
        self.assertIn("NOT approval", render_markdown(result))

    def test_scope_violation_blocks_even_with_green_ci(self):
        self.data["changed_files"].append("private/credentials.txt")
        result = analyze(self.data)
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertEqual(result["outside_scope"], ["private/credentials.txt"])

    def test_ci_failure_blocks(self):
        self.data["checks"][0]["conclusion"] = "failure"
        result = analyze(self.data)
        self.assertEqual(result["decision"], "BLOCKED")
        self.assertIn("Unit tests", result["ci_not_successful"])

    def test_queued_check_blocks(self):
        self.data["checks"][0].update(status="queued", conclusion=None)
        self.assertEqual(analyze(self.data)["decision"], "BLOCKED")

    def test_no_checks_is_invalid(self):
        self.data["checks"] = []
        with self.assertRaises(InvalidSnapshot):
            analyze(self.data)

    def test_duplicate_check_names_rejected(self):
        self.data["checks"].append(copy.deepcopy(self.data["checks"][0]))
        with self.assertRaises(InvalidSnapshot):
            analyze(self.data)

    def test_commit_must_be_exact_sha(self):
        self.data["commit"] = "1234"
        with self.assertRaises(InvalidSnapshot):
            analyze(self.data)

    def test_path_traversal_rejected(self):
        self.data["changed_files"] = ["docs/../private.key"]
        with self.assertRaises(InvalidSnapshot):
            analyze(self.data)

    def test_actor_echo_case_insensitive(self):
        self.data["actor"] = "CURSOR[BOT]"
        result = analyze(self.data)
        self.assertEqual(result["ignored_own_comment_echoes"], 1)

    def test_external_comment_not_automatically_approved(self):
        self.data["events"] = [{"kind": "comment", "author": "Reviewer"}]
        result = analyze(self.data)
        self.assertEqual(result["external_comments_to_review"], 1)
        self.assertEqual(result["decision"], "HUMAN_REVIEW_REQUIRED")

    def test_missing_expected_fields_fail_closed(self):
        del self.data["changed_files"]
        with self.assertRaises(InvalidSnapshot):
            analyze(self.data)

    def test_odd_status_invalid(self):
        self.data["checks"][0]["status"] = "maybe"
        with self.assertRaises(InvalidSnapshot):
            analyze(self.data)

    def test_boolean_pr_number_rejected(self):
        self.data["pr_number"] = True
        with self.assertRaises(InvalidSnapshot):
            analyze(self.data)


if __name__ == "__main__":
    unittest.main()
