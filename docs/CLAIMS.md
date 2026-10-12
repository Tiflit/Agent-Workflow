# Evidentiary Claims & Empirical Limits

> **Status:** Candidate claims register (v0.1 draft). Demonstrated vs. reported properties under [`KERNEL.md`](../KERNEL.md).

## 1. Evidentiary Boundary Matrix

| Dimension | Shown (Directly Inspected) | Reported (Human / Agent Relayed) | Not Shown (Unverified / Unknown) |
| :--- | :--- | :--- | :--- |
| **Pushed Checkpoints** | Remote commits, diffs, CI logs, GitHub records. | File freshness and local worktree state. | Arbitrary machine-failure recovery; bare-repo recovery without clean base. |
| **Same-Vendor Recovery** | Pushed trial commits reconciled after conversation reset. | Retained local worktrees enabled recovery; deviations occurred. | Independent verification without local worktree files. |
| **Cross-Vendor Recovery** | Pushed commits contained stale `Next:` trailer and Section 2 conflict. | Recognized stale trailer; online tool returned 403; human-relayed; start timing missing. | Automated failover; unassisted platform writes; token efficiency. |
| **Policy Governance** | Written contracts and scope boundaries in public threads. | Cooperative compliance observed; deviations occurred and corrected. | Hardware/OS sandboxing; technical non-bypassable enforcement. |
| **Windows Assisted Onboarding** | Published trial configuration and one-row inventory patch inspected via GitHub Issue records and diff ([Issue #3](https://github.com/Tiflit/Agent-Workflow/issues/3#issuecomment-6103291947)). | Local adoption, toy repository commits, working tree clean status, file digest pairs, and agent-reported latency. | Unassisted clone-and-start onboarding; independent timing / session duration measurement; technical enforcement or sandboxing; token or efficiency improvements. |
| **Optional Offline Toolkit** | Extracted standard-library tools inspected at accepted head `bc20c5eb6d669dbe97bbd2737248be5e8ab7d924` and merged at `ccd0d3af02935b7a083fca31b7ad2d67f32589e0` ([PR #7](https://github.com/Tiflit/Agent-Workflow/pull/7#issuecomment-6132305703)); 32 Python 3.11 cloud tests passed in GitHub Actions run 38304826999 (job 114996204732) over synthetic checkout `d2e4890205734f75f1b1d56f4a774c42d0e3f161`, exercising preflight contracts, path scope, PR hygiene, role previews, and directory hash invariance. | Host execution state, tool startup invocations, and local clean status. | Operating-system or filesystem isolation; enforced task, merge, or authority gates; autonomous supervisor or dispatch; unassisted adoption; arbitrary-project portability. |

## 2. Empirical Reference Findings

Reference trials established critical empirical limits:
- **Posting & Memory Gaps**: Online Claude got HTTP 403 with memory caveats; Antigravity Claude lacked write tools. Relayed findings left acquisition timing unrecorded.
- **Distinct Deviations**: Antigravity local-listing check deviated from instructions, distinct from the UI fixture background launch.
- **Windows Assisted Usability Trial ([Issue #3](https://github.com/Tiflit/Agent-Workflow/issues/3#issuecomment-6103291947))**: A fresh Gemini agent adopted the manual starter and corrected a single documentation discrepancy on Windows PowerShell with coordinator assistance. Preserved qualifications: required planning replacement after initial planner exceeded scope and used unauthorized helpers; required coordinator review and publication repair after inline shell string escaping corrupted published Markdown with ASCII control characters (U+000B), leading to literal file publication (`--body-file`); pre-flight inspection included an unnecessary parent-directory listing; execution timing and session-ceiling adherence were agent-reported and not independently measured. No claim of unassisted usability, technical enforcement, timing precision, or token efficiency. See [`WINDOWS-FIRST-RUN.md`](WINDOWS-FIRST-RUN.md).
- **No Blanket Compliance**: Written rules do not guarantee compliance; deviations occurred across runs.
- **Withheld Claims**: No general claim of cross-vendor parity, automated recovery, or token efficiency.
- **Optional Offline Toolkit Extraction ([PR #7](https://github.com/Tiflit/Agent-Workflow/pull/7#issuecomment-6132305703), merged `ccd0d3af02935b7a083fca31b7ad2d67f32589e0`)**: Extracted offline preflight and role-preview utilities from DXVK-Companion into `tooling/offline/`. Inspected source at accepted head `bc20c5eb6d669dbe97bbd2737248be5e8ab7d924`. Cloud CI passed 32 Python 3.11 unit tests in run 38304826999 (attempt 1, job 114996204732) with synthetic checkout `d2e4890205734f75f1b1d56f4a774c42d0e3f161`, verifying contract parsing, path scope evaluation, PR hygiene headings, role-preview summaries, and recursive directory hash non-mutation across synthetic fixtures. No DXVK application-test counts presented as template evidence. Host execution state and startup invocations remain reported. Operating system isolation, automated authority/merge enforcement, autonomous supervisor dispatch, and unassisted adoption remain unshown.

## 3. Standard Operational Metrics

Track metrics prospectively without retroactive reconstruction:
- **Dispatch Count**: Activation messages directing an agent's turn.
- **Human Interventions**: Manual actions (*link relay*, *approval*, *clarification*, *manual repair*).
- **Task-Level Latency**: Elapsed time from acknowledged acquisition to accepted reconstruction (including pauses). Unrecorded timestamps remain **Unknown**.
