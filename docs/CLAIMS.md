# Evidentiary Claims & Empirical Limits

> **Status:** Candidate claims register (v0.1 draft). Demonstrated vs. reported properties under [`KERNEL.md`](../KERNEL.md).

## 1. Evidentiary Boundary Matrix

| Dimension | Shown (Directly Inspected) | Reported (Human / Agent Relayed) | Not Shown (Unverified / Unknown) |
| :--- | :--- | :--- | :--- |
| **Pushed Checkpoints** | Remote commits, diffs, CI logs, GitHub records. | File freshness and local worktree state. | Arbitrary machine-failure recovery; bare-repo recovery without clean base. |
| **Same-Vendor Recovery** | Pushed trial commits reconciled after conversation reset. | Retained local worktrees enabled recovery; deviations occurred. | Independent verification without local worktree files. |
| **Cross-Vendor Recovery** | Pushed commits contained stale `Next:` trailer and Section 2 conflict. | Recognized stale trailer; online tool returned 403; human-relayed; start timing missing. | Automated failover; unassisted platform writes; token efficiency. |
| **Policy Governance** | Written contracts and scope boundaries in public threads. | Cooperative compliance observed; deviations occurred and corrected. | Hardware/OS sandboxing; technical non-bypassable enforcement. |
| **Windows Assisted Onboarding** | Assisted manual-starter adoption and single-file documentation task verified by static diff inspection and published GitHub Issue comments ([Issue #3](https://github.com/Tiflit/Agent-Workflow/issues/3#issuecomment-6103291947)). | Local toy commits, clean working tree status, file digest pairs, and agent-reported latency. | Unassisted clone-and-start onboarding; independent timing / session duration measurement; technical enforcement or sandboxing; token or efficiency improvements. |

## 2. Empirical Reference Findings

Reference trials established critical empirical limits:
- **Posting & Memory Gaps**: Online Claude got HTTP 403 with memory caveats; Antigravity Claude lacked write tools. Relayed findings left acquisition timing unrecorded.
- **Distinct Deviations**: Antigravity local-listing check deviated from instructions, distinct from the UI fixture background launch.
- **Windows Assisted Usability Trial ([Issue #3](https://github.com/Tiflit/Agent-Workflow/issues/3#issuecomment-6103291947))**: A fresh Gemini agent adopted the manual starter and corrected a single documentation discrepancy on Windows PowerShell with coordinator assistance. Friction identified: inline shell argument passing corrupted published Markdown with ASCII control characters (U+000B), requiring literal file publication (`--body-file`); pre-flight inspection included an unnecessary parent-directory listing; execution timing was agent-reported and unverified by the coordinator. No claim of unassisted usability, technical enforcement, timing precision, or token efficiency. See [`WINDOWS-FIRST-RUN.md`](WINDOWS-FIRST-RUN.md).
- **No Blanket Compliance**: Written rules do not guarantee compliance; deviations occurred across runs.
- **Withheld Claims**: No general claim of cross-vendor parity, automated recovery, or token efficiency.

## 3. Standard Operational Metrics

Track metrics prospectively without retroactive reconstruction:
- **Dispatch Count**: Activation messages directing an agent's turn.
- **Human Interventions**: Manual actions (*link relay*, *approval*, *clarification*, *manual repair*).
- **Task-Level Latency**: Elapsed time from acknowledged acquisition to accepted reconstruction (including pauses). Unrecorded timestamps remain **Unknown**.
