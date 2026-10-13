"""Integration and portability smoke tests for offline toolkit in a clean unrelated project."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

STARTER_FILES = [
    "AGENTS.md",
    "KERNEL.md",
    "README.md",
    "REGISTER.md",
    "SECURITY.md",
    "docs/CLAIMS.md",
    "docs/PROFILES.md",
    "docs/RECORDS.md",
    "docs/WINDOWS-FIRST-RUN.md",
    "tooling/offline/README.md",
    "tooling/offline/check_pr_hygiene.py",
    "tooling/offline/evaluate_scope.py",
    "tooling/offline/parse_contract.py",
    "tooling/offline/preflight_check.py",
    "tooling/offline/preview_role_handoff.py",
]


def compute_dir_hashes(root_dir: Path) -> dict[str, str]:
    """Computes SHA-256 hashes for all regular files in a directory tree."""
    hashes: dict[str, str] = {}
    for p in sorted(root_dir.rglob("*")):
        if p.is_file():
            rel = str(p.relative_to(root_dir)).replace("\\", "/")
            hashes[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return hashes


class TestCleanBootstrap(unittest.TestCase):
    """Smoke test suite exercising offline toolkit in an unrelated clean project."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_root = Path(self.temp_dir.name)

        # 1. Copy all eight starter documents, recipe, and toolkit preserving relative layout
        for rel_path in STARTER_FILES:
            src_file = REPO_ROOT / rel_path
            dest_file = self.project_root / rel_path
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, dest_file)

        # 2. Build unrelated project layout (generic repo components)
        src_dir = self.project_root / "src"
        src_dir.mkdir(parents=True, exist_ok=True)
        (src_dir / "demo.py").write_text(
            '"""Demo application module."""\n\ndef run() -> int:\n    return 0\n',
            encoding="utf-8",
        )

        docs_dir = self.project_root / "docs"
        docs_dir.mkdir(parents=True, exist_ok=True)
        (docs_dir / "guide.md").write_text(
            "# User Guide\n\nDemo project documentation.\n",
            encoding="utf-8",
        )

        # 3. Create named fixture files BEFORE establishing the baseline hash snapshot
        fixtures_dir = self.project_root / "fixtures"
        fixtures_dir.mkdir(parents=True, exist_ok=True)

        # Preflight valid issue contract
        (fixtures_dir / "valid_issue.md").write_text(
            "# [Demo] Add demo functionality\n\n"
            "### Allowed paths\n"
            "- src/demo.py\n"
            "- docs/guide.md\n",
            encoding="utf-8",
        )

        # Preflight valid PR description
        (fixtures_dir / "valid_pr.md").write_text(
            "## Primary Issue\n"
            "Fixes #1\n\n"
            "## Summary\n"
            "Add demo functionality and documentation.\n\n"
            "## Scope\n"
            "- src/demo.py\n"
            "- docs/guide.md\n\n"
            "## Verification\n"
            "Automated unit tests.\n\n"
            "## Documentation\n"
            "User guide updated.\n",
            encoding="utf-8",
        )

        # Preflight valid changed-files manifest
        (fixtures_dir / "valid_files.json").write_text(
            json.dumps([
                {"filename": "src/demo.py", "previous_filename": None, "status": "modified"},
                {"filename": "docs/guide.md", "previous_filename": None, "status": "modified"},
            ]),
            encoding="utf-8",
        )

        # Preflight manifest with renamed file whose previous_filename is outside scope
        (fixtures_dir / "renamed_files.json").write_text(
            json.dumps([
                {
                    "filename": "src/demo.py",
                    "previous_filename": "legacy/unauthorized_old_file.py",
                    "status": "renamed",
                }
            ]),
            encoding="utf-8",
        )

        # Preflight PR body missing ## Documentation heading
        (fixtures_dir / "pr_missing_doc.md").write_text(
            "## Primary Issue\n"
            "Fixes #1\n\n"
            "## Summary\n"
            "Add demo functionality.\n\n"
            "## Scope\n"
            "- src/demo.py\n"
            "- docs/guide.md\n\n"
            "## Verification\n"
            "Automated unit tests.\n",
            encoding="utf-8",
        )

        # Role preview valid snapshot (all 3 roles)
        (fixtures_dir / "valid_snapshot.json").write_text(
            json.dumps({
                "capture_time_utc": "2026-10-12T19:00:00Z",
                "repo": "GenericOrg/demo-service",
                "pr_number": 1,
                "pr_title": "[Demo] Add demo functionality",
                "pr_state": "OPEN",
                "pr_merged": False,
                "live_pr_head_sha": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "live_pr_base_sha": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                "pr_base_ref": "main",
                "repo_default_branch": "main",
                "live_default_branch_sha": "cccccccccccccccccccccccccccccccccccccccc",
                "base_sync_status": "synced",
                "base_has_moved": False,
                "primary_issue_number": 1,
                "primary_issue_title": "[Demo] Add demo functionality",
                "primary_issue_state": "OPEN",
                "decision_governance": {
                    "required": None,
                    "proposed_option": None,
                    "status": "NOT_REQUIRED",
                    "approval_source": None,
                },
                "local_workspace": {
                    "branch": "feat/demo",
                    "head_sha": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "clean",
                },
            }),
            encoding="utf-8",
        )

        # Role preview inactive snapshot (closed / merged task)
        (fixtures_dir / "inactive_snapshot.json").write_text(
            json.dumps({
                "capture_time_utc": "2026-10-12T19:00:00Z",
                "repo": "GenericOrg/demo-service",
                "pr_number": 1,
                "pr_title": "[Demo] Add demo functionality",
                "pr_state": "CLOSED",
                "pr_merged": True,
                "live_pr_head_sha": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "live_pr_base_sha": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                "pr_base_ref": "main",
                "repo_default_branch": "main",
                "live_default_branch_sha": "cccccccccccccccccccccccccccccccccccccccc",
                "base_sync_status": "synced",
                "base_has_moved": False,
                "primary_issue_number": 1,
                "primary_issue_title": "[Demo] Add demo functionality",
                "primary_issue_state": "CLOSED",
                "decision_governance": {
                    "required": None,
                    "proposed_option": None,
                    "status": "NOT_REQUIRED",
                    "approval_source": None,
                },
                "local_workspace": {
                    "branch": "feat/demo",
                    "head_sha": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "clean",
                },
            }),
            encoding="utf-8",
        )

        # Role preview snapshot with unknown state
        (fixtures_dir / "unknown_state_snapshot.json").write_text(
            json.dumps({
                "capture_time_utc": "2026-10-12T19:00:00Z",
                "repo": "GenericOrg/demo-service",
                "pr_number": 1,
                "pr_title": "[Demo] Add demo functionality",
                "pr_state": "PENDING_REVIEW",
                "pr_merged": False,
                "live_pr_head_sha": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "live_pr_base_sha": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                "pr_base_ref": "main",
                "repo_default_branch": "main",
                "live_default_branch_sha": "cccccccccccccccccccccccccccccccccccccccc",
                "base_sync_status": "synced",
                "base_has_moved": False,
                "primary_issue_number": 1,
                "primary_issue_title": "[Demo] Add demo functionality",
                "primary_issue_state": "OPEN",
                "decision_governance": {
                    "required": None,
                    "proposed_option": None,
                    "status": "NOT_REQUIRED",
                    "approval_source": None,
                },
                "local_workspace": {
                    "branch": "feat/demo",
                    "head_sha": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "status": "clean",
                },
            }),
            encoding="utf-8",
        )

        # 4. Record baseline recursive file paths and SHA-256 hashes
        self.baseline_hashes = compute_dir_hashes(self.project_root)

        # Assert no pre-existing bytecode cache
        bytecode_files = [
            k for k in self.baseline_hashes if "__pycache__" in k or k.endswith(".pyc")
        ]
        self.assertEqual(
            bytecode_files,
            [],
            f"Pre-existing bytecode files found in clean fixture tree: {bytecode_files}",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def run_cli(self, args: list[str]) -> subprocess.CompletedProcess[str]:
        """Executes copied CLI in a child subprocess with project root as cwd."""
        cmd = [sys.executable] + args
        env = os.environ.copy()
        env.pop("PYTHONPATH", None)
        env.pop("PYTHONDONTWRITEBYTECODE", None)

        proc = subprocess.run(
            cmd,
            cwd=str(self.project_root),
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )

        # Assert non-mutation of regular files inside the project tree
        current_hashes = compute_dir_hashes(self.project_root)
        self.assertEqual(
            current_hashes,
            self.baseline_hashes,
            "CLI invocation modified regular files inside the copied project tree.",
        )

        # Assert bytecode writes were suppressed (no pycache / pyc)
        pycache_paths = [
            str(p.relative_to(self.project_root)).replace("\\", "/")
            for p in self.project_root.rglob("*")
            if "__pycache__" in p.parts or p.name.endswith(".pyc")
        ]
        self.assertEqual(
            pycache_paths,
            [],
            f"Bytecode cache files detected in copied project: {pycache_paths}",
        )

        return proc

    def test_copied_starter_and_toolkit_layout_and_relative_links(self) -> None:
        """Verifies copied files exist and internal relative documentation links resolve."""
        # 1. Assert all 15 starter and toolkit files exist
        for rel_path in STARTER_FILES:
            target_path = self.project_root / rel_path
            self.assertTrue(target_path.is_file(), f"Missing copied file: {rel_path}")

        # 2. Assert synthetic project files exist
        self.assertTrue((self.project_root / "src" / "demo.py").is_file())
        self.assertTrue((self.project_root / "docs" / "guide.md").is_file())

        # 3. Verify relative markdown links across copied documentation
        link_pattern = re.compile(r"\[(?:[^\]]*)\]\(([^)]+)\)")
        for rel_path in STARTER_FILES:
            if not rel_path.endswith(".md"):
                continue
            doc_file = self.project_root / rel_path
            content = doc_file.read_text(encoding="utf-8")
            for match in link_pattern.finditer(content):
                target = match.group(1).strip()
                # Skip external URLs, mailto, and in-page anchor fragments
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                # Strip in-page anchors and query strings
                cleaned_target = target.split("#")[0].split("?")[0].strip()
                if not cleaned_target:
                    continue

                resolved = (doc_file.parent / cleaned_target).resolve()
                self.assertTrue(
                    resolved.exists(),
                    f"Broken relative link in '{rel_path}': '{target}' -> '{resolved}' does not exist.",
                )
                self.assertTrue(
                    resolved.is_relative_to(self.project_root),
                    f"Relative link in '{rel_path}' points outside project root: '{target}'.",
                )

    def test_valid_scoped_preflight_passes_with_not_verified_notice(self) -> None:
        """Valid preflight returns 0 with PASS report and NOT VERIFIED notice."""
        proc = self.run_cli([
            "tooling/offline/preflight_check.py",
            "--issue-body-file", "fixtures/valid_issue.md",
            "--pr-body-file", "fixtures/valid_pr.md",
            "--files-json", "fixtures/valid_files.json",
        ])
        self.assertEqual(proc.returncode, 0, f"Stderr: {proc.stderr}")
        self.assertIn("Scope check:   PASS", proc.stdout)
        self.assertIn("PR hygiene check: PASS", proc.stdout)
        self.assertIn("NOT VERIFIED: Authority/approval", proc.stdout)

    def test_renamed_old_path_outside_scope_fails_without_leaking_raw_filename(self) -> None:
        """Renamed file with out-of-scope old name returns 1 without echoing raw path."""
        proc = self.run_cli([
            "tooling/offline/preflight_check.py",
            "--issue-body-file", "fixtures/valid_issue.md",
            "--pr-body-file", "fixtures/valid_pr.md",
            "--files-json", "fixtures/renamed_files.json",
        ])
        self.assertEqual(proc.returncode, 1)
        self.assertIn("Scope check:   FAIL", proc.stdout)
        self.assertIn(
            "Scope violation: item at manifest index 0 violates allowed contract paths.",
            proc.stdout,
        )
        # Verify raw out-of-scope filename is NOT echoed in stdout or stderr
        self.assertNotIn("unauthorized_old_file", proc.stdout)
        self.assertNotIn("legacy/unauthorized_old_file.py", proc.stdout)
        self.assertNotIn("unauthorized_old_file", proc.stderr)

    def test_missing_documentation_heading_fails_with_fixed_diagnostic(self) -> None:
        """PR body missing required Documentation heading returns 1 with fixed diagnostic."""
        proc = self.run_cli([
            "tooling/offline/preflight_check.py",
            "--issue-body-file", "fixtures/valid_issue.md",
            "--pr-body-file", "fixtures/pr_missing_doc.md",
            "--files-json", "fixtures/valid_files.json",
        ])
        self.assertEqual(proc.returncode, 1)
        self.assertIn("PR hygiene check: FAIL", proc.stdout)
        self.assertIn(
            "Hygiene error: missing required section heading '## Documentation'.",
            proc.stdout,
        )

    def test_valid_snapshot_preview_for_all_three_roles(self) -> None:
        """Valid snapshot formats bounded preview for implementer, coordinator, reviewer."""
        for role in ("implementer", "coordinator", "reviewer"):
            proc = self.run_cli([
                "tooling/offline/preview_role_handoff.py",
                "--snapshot-file", "fixtures/valid_snapshot.json",
                "--role", role,
            ])
            self.assertEqual(proc.returncode, 0, f"Role {role} failed: {proc.stderr}")
            self.assertIn(
                "Role Handoff Preview (Historical snapshot, unverified-current):",
                proc.stdout,
            )
            self.assertIn(
                "Authority: This preview grants no push, execution, publication, approval, or merge authority.",
                proc.stdout,
            )
            self.assertIn(f"Role: {role.capitalize()}", proc.stdout)

            word_count = len(proc.stdout.split())
            self.assertLessEqual(
                word_count,
                180,
                f"Role {role} preview exceeded 180 words: {word_count}",
            )

    def test_merged_or_closed_task_shows_inactive_preview_and_no_restart(self) -> None:
        """Merged or closed task generates inactive notice directing no restart."""
        proc = self.run_cli([
            "tooling/offline/preview_role_handoff.py",
            "--snapshot-file", "fixtures/inactive_snapshot.json",
            "--role", "implementer",
        ])
        self.assertEqual(proc.returncode, 0, f"Inactive preview failed: {proc.stderr}")
        self.assertIn("Status: Task is closed or merged (inactive).", proc.stdout)
        self.assertIn("never restart implementation", proc.stdout)
        self.assertIn(
            "Stop Boundary: Stop immediately. Do not execute code or resume implementation.",
            proc.stdout,
        )

        word_count = len(proc.stdout.split())
        self.assertLessEqual(word_count, 180)

    def test_unknown_task_state_returns_nonzero_without_preview(self) -> None:
        """Unknown task state returns nonzero and suppresses preview text."""
        proc = self.run_cli([
            "tooling/offline/preview_role_handoff.py",
            "--snapshot-file", "fixtures/unknown_state_snapshot.json",
            "--role", "implementer",
        ])
        self.assertEqual(proc.returncode, 1)
        self.assertIn("ERROR: Snapshot schema validation failed", proc.stderr)
        self.assertEqual(proc.stdout.strip(), "")


if __name__ == "__main__":
    unittest.main()
