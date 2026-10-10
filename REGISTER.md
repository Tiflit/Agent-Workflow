# Deployment Enforcement Register — Manual Preset

> **Status:** Candidate starter deployment register (v0.1 draft). Specifies concrete environment boundaries, human authorities, and enforcement status under [`KERNEL.md`](KERNEL.md).

## 1. Governance & Authority Configuration

| Setting | Value / Placeholder | Description |
| :--- | :--- | :--- |
| **Adopted Kernel Version** | `v0.4` | Invariant normative rules from `KERNEL.md`. |
| **Applicable Policy Revision** | `git rev-parse HEAD:REGISTER.md` | Policy revision derived from applicable policy files at the acquired commit, not every unreviewed HEAD change. External permission changes remain tracked separately. |
| **Human Principal** | `<HUMAN_OWNER_ID>` | Authorized human owner retaining ultimate approval and merge authority. |
| **Authorized Control Channels** | `<PRIMARY_CONTROL_CHANNEL>` | Official medium for task activation (e.g., repository Issue thread, direct terminal). |
| **Agent Identities** | `<AGENT_ROLE_ID>` | Logical identity assigned to the executing agent. |
| **Operational Preset** | `Manual-Cooperative` | Strictly human-mediated operation; unattended autonomous execution is prohibited. |

## 2. Environment & Processing Destinations

- **Local Execution Bounds**:
  - Task execution is confined to isolated task worktrees (e.g., `<TASK_WORKTREE_PATH>`).
  - Access to personal user folders, unrelated repositories, system credentials, and browser session caches is prohibited.
- **Approved Remote Destinations**:
  - Version Control: Remote repository origin (`<GIT_REMOTE_ORIGIN>`).
  - Model Inference: Approved LLM provider APIs (`<APPROVED_AI_PROVIDER>`). Data sent by the human is documented; onward agent transmission requires human awareness.
- **Unauthorized Destinations**: Arbitrary public pastebins, external third-party web endpoints, and unapproved cloud storage buckets are prohibited.

## 3. Enforcement Status & Technical Boundaries

In accordance with Kernel K1 and K7, technical enforcement mechanisms are distinguished from cooperative adherence. Unknown capabilities must be declared as unknown rather than assumed to be enforced.

| Boundary | Enforcement Level | Realized Mechanism | Gap Disclosure |
| :--- | :--- | :--- | :--- |
| **Scope Limitation** | Cooperative | Agent prompt constraints & pre-commit diff review | No operating system sandbox isolates file access; cooperative compliance only. |
| **Test & Execution Hold** | Cooperative | Manual approval request in chat / Issue thread | No automatic execution interceptor; agent halts cooperatively before executing tests. |
| **Credential Separation** | Gapped / Cooperative | Shared account tokens (e.g., local developer Git/CLI token) | Agent operates under shared developer credentials; attribution trailers do not provide technical non-repudiation. |
| **Network Boundaries** | Unknown / Unrestricted | Standard host network interface | Outbound network calls are not restricted by local proxy filters. |

## 4. Operational Boundaries & Stop Triggers

- **Test Authorization Requirement**: Local test runs, debugger sessions, or runtime application executions require explicit, advance, bounded authorization defining exact commands, targets, and expected duration.
- **Cost & Quota Budgets**: Bounded to single-task requests. If context length exceeds 80% or rate limits approach exhaustion, agents must checkpoint and yield.
- **Immediate Stop Triggers**:
  1. Ambiguity in task contract or conflicting scope instructions.
  2. Potential leakage or detection of sensitive credentials or personal data.
  3. Receipt of a human hold ("Hold", "Stop", "Pause") on the control channel.
  4. Detection of unexpected git branch collisions or unstaged modifications.

When stopped, agents preserve all working state in the task worktree and yield for human instruction.
