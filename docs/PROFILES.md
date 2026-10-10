# Operational Profiles & Multi-Agent Coordination

> **Status:** Candidate operational profiles (v0.1 draft). Defines interaction models under [`KERNEL.md`](../KERNEL.md).

## 1. Profile 1: Lightweight Manual Default (Single Agent)

- **Execution Model**: Single agent operating under direct human supervision.
- **Workflow**: The human issues discrete task contracts via chat or issues. The agent prepares files and checkpoints in an isolated worktree. The human reviews diffs and executes or authorizes tests and git pushes.
- **Branch Ownership**: Single-writer branch ownership ensures linear, predictable progress.

## 2. Profile 2: Gated Multi-Agent Mode (Turn-Based Peer Review)

- **Execution Model**: Primary author agent and independent reviewer agent(s).
- **Coordination**: Turn-based sequential execution. Independent concurrent tasks may proceed on separate feature branches; shared branches require explicit handoffs.
- **Role Boundaries**: Author and reviewer roles are deployment choices; reviewer code-writing limits are project-defined policies rather than universal prohibitions.

## 3. Profile 3: Explicit Human-Relay Variant (Read-Only Reviewers)

When an agent operates in a read-only environment or lacks direct GitHub platform credentials:
- **Capability Check & Stopping**: Agents check tool capabilities upon acquisition. If platform posting tools fail or are unavailable, the agent MUST STOP and output its report to the operator rather than attempting unauthorized credential workarounds.
- **Explicit Route**: The human operator manually copies prompts and relays review findings across platforms via an explicitly selected route.
- **Attribution & Timing**: Relayed findings must be attributed as operator-relayed text. Subsequent acknowledgment publication cannot retroactively establish an agent start time.

## 4. Session Memory & Context Disclosures

- **Memory Disclosure**: A fresh conversation does not guarantee the complete absence of IDE, account, or persistent system memory. Deployments must disclose or disable memory where feasible, or qualify findings accordingly.
- **Cache vs. Authority**: Durable repository records and remote commits remain the sole authoritative source of truth. Ephemeral session memory serves as an operational cache, not forbidden context.
- **Checkpointing**: Checkpoint at natural milestones and known quota warnings; unforeseen context compaction or abrupt session termination cannot always be anticipated.
