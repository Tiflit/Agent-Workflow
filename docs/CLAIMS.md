# Evidentiary Claims Boundaries & Empirical Limits

> **Status:** Candidate claims register (v0.1 draft). Defines demonstrated vs. unverified workflow properties under [`KERNEL.md`](../KERNEL.md).

## 1. Evidentiary Boundary Matrix

| Capability Dimension | Shown (Directly Evidenced) | Reported (Human / Agent Reported) | Not Shown (Unverified / Unknown) |
| :--- | :--- | :--- | :--- |
| **Same-Vendor Session Recovery** | Local artifact inspection succeeded after conversation reset. | Procedure deviations occurred; retained local worktrees enabled reconstruction. | Recovery without local artifacts; general crash/loss recovery. |
| **Cross-Vendor Recovery Trial** | Fresh agent correctly identified stale `Next:` trailer from remote commits. | Agent GitHub write failed; analysis was manually relayed by human operator. | Unassisted remote posting; automated multi-vendor failover; token efficiency. |
| **Safety & Policy Enforcement** | Agents halted upon written scope limits and explicit human holds. | Cooperative compliance observed across multiple structured tasks. | Operating-system technical sandboxing; non-bypassable policy enforcement. |

## 2. Empirical Trial Caveats

Recent trials in reference deployments demonstrated important boundary limits:
- **Same-Vendor Recovery**: Depended heavily on retained local files and worktree artifacts; did not prove bare-repository recovery.
- **Cross-Vendor Reconstruction**: Fresh cross-vendor agent correctly spotted stale trailers and material uncertainties, but lacked automated platform posting privileges; report timing was unrecorded.
- **General Claims Withheld**: We make **no general claim** of vendor neutrality, arbitrary machine-failure recovery, token efficiency, or technical policy enforcement.

## 3. Standard Operational Metrics

To maintain truthful measurement, track metrics prospectively:
- **Dispatch Count**: Distinct activation messages directing an agent's next action.
- **Human Interventions**: Count of manual operator actions (classified as: link relay, approval, clarification, or manual fix).
- **Task-Level Time**: Elapsed time from initial task acquisition to verified completion.

Metrics not captured contemporaneously remain explicitly labeled as **Unknown**.
