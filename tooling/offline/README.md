# Optional Offline Preflight and Role-Preview Toolkit

> **Notice:** This toolkit is an **optional, stack-neutral, offline** utility bundle. It requires only the Python standard library (Python 3.10+). Execution of runtime utilities is strictly operator-invoked and opt-in.

---

## 1. Overview & Contents

This toolkit provides local, offline utilities for validating task contracts and generating compact role-bound handoff previews. Tools are designed for read-only execution without network access, credentials, or file writes. Verified behavior is bounded by source inspection and enumerated synthetic test suites (patched I/O calls and recursive directory hash invariance); this is an application-level design and runtime intent, not operating system process or filesystem isolation:

- **`preflight_check.py`**: Operator-invoked scope and PR hygiene preflight. Validates an Issue contract description, Pull Request body text, and a JSON manifest of changed files against defined task boundaries.
- **`preview_role_handoff.py`**: Operator-invoked role handoff preview generator. Consumes an existing handoff snapshot JSON file and formats a bounded, role-specific summary (<=180 words) for `implementer`, `coordinator`, or `reviewer`.
- **Pure Helpers**:
  - `parse_contract.py`: Pure parsing functions for task contracts (`### Allowed paths`, `Unconstrained`) and primary issue extraction (`## Primary Issue`, closing keywords).
  - `evaluate_scope.py`: Path pattern matching (`/**`, `/`, exact match) and file manifest checking.
  - `check_pr_hygiene.py`: Heading presence verification (`## Summary`, `## Scope`, `## Verification`, `## Documentation`) and primary issue reference validation.

---

## 2. Source Provenance & Extraction Differences

- **Source Repository**: [`Tiflit/DXVK-Companion`](https://github.com/Tiflit/DXVK-Companion)
- **Pinned Source Revision**: Commit [`1ce8b28f983ceb9b610c5e495fac02dac5c5a72f`](https://github.com/Tiflit/DXVK-Companion/commit/1ce8b28f983ceb9b610c5e495fac02dac5c5a72f) (following merges of PR #86 / Issue #85 and PR #88 / Issue #87).
- **Extraction Differences**:
  1. **Removed GitHub API & Network Access**: Omitted all live GitHub API clients, curl calls, tokens, authorization headers, and pagination loops present in source CI helpers.
  2. **Removed Credential Acquisition**: Zero token acquisition (`GH_TOKEN`, `GITHUB_TOKEN`) or environment credential lookups.
  3. **Removed Subprocess Invocation**: Omitted git CLI subprocess calls (`git diff`, `git status`, worktree commands).
  4. **Removed Project Defaults**: Replaced all repository-specific host paths, project identifiers, and default flags with generic, stack-neutral inputs.
  5. **Pure Standard Library**: All extracted tools and helpers rely exclusively on the Python standard library.

---

## 3. Input Schemas & Synthetic Examples

### A. Preflight Check (`preflight_check.py`)

#### Inputs:
1. `--issue-body-file <path>`: Markdown file containing the task contract with an explicit `### Allowed paths` section.
2. `--pr-body-file <path>`: Markdown file containing required PR template headings (`## Summary`, `## Scope`, `## Verification`, `## Documentation`, and `## Primary Issue` or `Fixes #X`).
3. `--files-json <path>`: JSON file containing an array of changed file objects (`[{"filename": "path/to/file", "previous_filename": null}]`).

#### Example Issue Contract (`issue.md`):
```markdown
## Task Contract

### Allowed paths
- src/example/module.py
- docs/guides/**
```

Alternatively, for unconstrained tasks:
```markdown
### Allowed paths
- Unconstrained
```

#### Example Pull Request Description (`pr.md`):
```markdown
## Primary Issue

Fixes #123

## Summary

Implemented scoped feature update.

## Scope

Confined to allowed paths.

## Verification

Synthetic cloud tests passed.

## Documentation

Documented in README.md.
```

#### Example Changed Files Manifest (`files.json`):
```json
[
  {
    "filename": "src/example/module.py",
    "previous_filename": null
  },
  {
    "filename": "docs/guides/overview.md",
    "previous_filename": null
  }
]
```

#### Usage:
```bash
python tooling/offline/preflight_check.py \
  --issue-body-file issue.md \
  --pr-body-file pr.md \
  --files-json files.json
```

---

### B. Role Handoff Preview (`preview_role_handoff.py`)

#### Inputs:
1. `--snapshot-file <path>`: JSON file conforming to the handoff snapshot schema.
2. `--role <implementer|coordinator|reviewer>`: Role to format the preview for.

#### Example Snapshot Data (`snapshot.json`):
```json
{
  "repo": "example-org/sample-repo",
  "pr_number": 42,
  "primary_issue_number": 10,
  "pr_state": "OPEN",
  "pr_merged": false,
  "primary_issue_state": "OPEN",
  "live_pr_head_sha": "1111111111111111111111111111111111111111",
  "live_pr_base_sha": "2222222222222222222222222222222222222222",
  "live_default_branch_sha": "3333333333333333333333333333333333333333"
}
```

#### Usage:
```bash
python tooling/offline/preview_role_handoff.py \
  --snapshot-file snapshot.json \
  --role implementer
```

---

## 4. Limitations & Disclaimers

> **Historical snapshot, unverified-current.**
> Live refs, CI freshness, and human approval are **NOT VERIFIED**.

> **Authority Disclaimer:**
> This preview and preflight grant **no push, execution, publication, approval, or merge authority**.

- The preflight check performs local syntactic and path matching only. It does not certify code correctness, build status, test pass rates, or repository branch rules.
- The role handoff preview renders a historical snapshot; it does not query live GitHub state, branch heads, or PR reviews.
- Closed or merged tasks always emit inactive status notices and instruct agents to stop immediately without code execution or implementation restarts.
- **Not Operating-System Isolation:** Tools do not provide process confinement, operating-system sandboxing, or filesystem isolation. Verified non-mutation behavior reflects runtime intent, intercepted mock boundaries, and recursive regular-file path/hash invariance in clean temporary test directories. Test guards do not cover untested flags (such as standalone `O_TRUNC`) or general environment isolation.
- Use of this toolkit is entirely opt-in and does not alter the candidate/unadopted status of the surrounding workflow template.
