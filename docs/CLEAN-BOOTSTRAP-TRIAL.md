# Clean Project Bootstrap Trial & Offline Toolkit Portability

## 1. Purpose

Validates the runtime portability and layout integrity of Agent-Workflow's manual starter documents and optional offline toolkit when copied into a fresh, unrelated synthetic project repository. Tests execute real CLIs in child processes without external packages, network access, GitHub credentials, or source-tree Python imports.

## 2. Copied Layout & Structure

The clean test project is provisioned with generic repository metadata (`GenericOrg/demo-service`), an application component (`src/demo.py`), a documentation file (`docs/guide.md`), and the complete relative workflow set:
- **Starter & Trial Documents (10 files)**: `README.md`, `KERNEL.md`, `REGISTER.md`, `AGENTS.md`, `SECURITY.md`, `docs/CLAIMS.md`, `docs/CLEAN-BOOTSTRAP-TRIAL.md`, `docs/PROFILES.md`, `docs/RECORDS.md`, and `docs/WINDOWS-FIRST-RUN.md`.
- **Offline Toolkit (6 files)**: `tooling/offline/README.md`, `tooling/offline/check_pr_hygiene.py`, `tooling/offline/evaluate_scope.py`, `tooling/offline/parse_contract.py`, `tooling/offline/preflight_check.py`, and `tooling/offline/preview_role_handoff.py`.
- **Pre-Baseline Fixtures (`fixtures/`)**: Synthetic contracts, PR descriptions, file manifests, and role-preview handoff JSON snapshots.

## 3. Fixture Cases & Execution Boundaries

The test suite exercises seven distinct test methods alongside shared per-invocation hash and cache non-mutation assertions:
1. **Layout & Link Integrity**: Confirms all 16 copied files exist and internal relative Markdown links resolve within the destination tree.
2. **Valid Preflight**: Returns exit code 0, reporting scope PASS, PR hygiene PASS, and explicit `NOT VERIFIED` notices.
3. **Renamed File Scope Violation**: Renaming an out-of-scope previous path returns exit code 1, reporting violation by manifest index without leaking raw filenames.
4. **Missing PR Hygiene Section**: Omission of `## Documentation` returns exit code 1 with a fixed sanitized diagnostic.
5. **Multi-Role Handoff Previews**: Formats bounded summaries (<=180 words) for `implementer`, `coordinator`, and `reviewer` with explicit non-authority disclaimers.
6. **Inactive Task Directives**: Closed or merged snapshots generate inactive notices prohibiting implementation restarts.
7. **Unknown State Rejection**: Invalid task states return nonzero and suppress preview output.
- **Shared Assertions (Hash Invariance & Zero Bytecode)**: Pre-baseline recursive directory SHA-256 comparison and absence of `__pycache__` / `.pyc` files run across every CLI invocation and in `setUp()`.

## 4. Cloud Command & Evidence Acquisition

- **Cloud CI Step**: `python -m unittest discover -s tests/bootstrap -p 'test_*.py' -v` under `.github/workflows/offline-toolkit-tests.yml`.
- **Evidence Fields**:
  - Workflow Run ID: 38331655467 (job 115082500638)
  - Tested PR Head SHA: `abbdf4d021b7ee1934dd2088e08e7f96ded7154d`
  - Tested Checkout SHA: `8ffb46a3bf9c4424e1914fb7e342368ec0aeed70`
  - Outcome: 32 offline tests OK + 7 bootstrap tests OK (accepted in PR #11)

## 5. Empirical Limitations

- **Smoke Test Only**: Demonstrates CLI portability and layout stability; does not prove or evaluate unassisted autonomous agent onboarding.
- **Assisted Preparation**: Reflects human-assisted template copying.
- **No Broad Claims**: Makes no timing, token efficiency, or universal environment portability claims.
- **No Governance Adoption**: Candidate trial only; does not adopt candidate kernel v0.4 or modify deployment policy.
