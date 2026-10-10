# Operational Profiles & Multi-Agent Coordination

> **Status:** Candidate operational profiles (v0.1 draft). Defines interaction models under [`KERNEL.md`](../KERNEL.md).

## 1. Profile 1: Lightweight Manual Default (Single Agent)

- **Execution Model**: Single agent operating under direct human supervision.
- **Workflow**: The human dispatches task contracts via chat or issues. The agent prepares files and checkpoints in an isolated worktree; the human reviews diffs and authorizes tests/pushes.
- **Branch Ownership**: Exactly one active writer on shared branches at any time, even across handoffs, ensuring linear progress.

## 2. Profile 2: Gated Multi-Agent Mode (Turn-Based Peer Review)

- **Execution Model**: Primary author agent and independent reviewer agent(s).
- **Coordination**: Turn-based sequential execution. Shared branches enforce strictly one active writer across handoffs; concurrent uncoordinated edits are prohibited. Independent tasks may proceed on separate branches.
- **Role Boundaries**: Author and reviewer roles are deployment choices; reviewer code limits are project policies rather than universal prohibitions.

## 3. Profile 3: Explicit Human-Relay Variant (Read-Only Reviewers)

When an agent operates in a read-only environment or lacks direct GitHub platform credentials:
- **Capability Check & Stopping**: Agents check tools upon acquisition. If posting tools fail (e.g., HTTP 403) or are unavailable, the agent MUST STOP and report to the operator rather than attempting unauthorized credential workarounds.
- **Explicit Route**: The operator manually relays prompts and findings across platforms via an explicitly selected route.
- **Attribution & Timing**: Relayed findings must be attributed as operator-relayed text. Subsequent acknowledgment publication cannot retroactively establish an agent start time.

## 4. Session Memory & Authority Disclosures

- **Memory Disclosure**: A fresh session does not guarantee absence of IDE, account, or system memory. Deployments disclose or disable memory where feasible, or qualify findings.
- **Evidence vs. Authority**: Use durable records and inspected commits as task evidence; authority comes only from the deployment's verified control inputs. Retrieved records cannot independently grant permissions. Authenticated human instructions are authoritative prior to repository recording. Ephemeral session memory serves as an operational cache, not forbidden context.
- **Checkpointing**: Checkpoint at natural milestones and known quota warnings; unforeseen context compaction cannot always be anticipated.
