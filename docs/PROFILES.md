# Operational Profiles & Multi-Agent Coordination

> **Status:** Candidate operational profiles (v0.1 draft). Defines interaction models under [`KERNEL.md`](../KERNEL.md).

## 1. Profile 1: Lightweight Manual Default (Single Agent)

- **Execution Model**: One agent, one human developer.
- **Workflow**: The human issues discrete task contracts via chat or issues. The agent prepares files and checkpoints in an isolated worktree. The human reviews diffs and executes or authorizes tests and git pushes.
- **Best For**: Daily feature development, refactoring, and single-developer workflows.

## 2. Profile 2: Gated Multi-Agent Mode (Turn-Based Peer Review)

- **Execution Model**: Primary author agent and independent reviewer agent(s).
- **Coordination**: Strictly sequential and turn-based; concurrent uncoordinated edits on shared branches are prohibited.
- **Authority**: Reviewer agents inspect diffs and provide feedback; they do not author code or self-approve integration.

## 3. Profile 3: Explicit Human-Relay Variant (Read-Only Reviewers)

When an agent operates in a read-only environment or lacks direct GitHub platform credentials:
- **Capability Check at Acquisition**: Agents must verify available tools upon startup. If external posting tools are missing or fail, the agent MUST STOP and output its report to the operator rather than attempting unauthorized credential workarounds.
- **Human-Relayed Evidence**: The human operator manually copies and relays prompts and review findings between platforms.
- **Attribution & Timing**: Relayed findings must be explicitly attributed as operator-relayed text. Late acknowledgment publication after manual relay does not retroactively adjust task start or elapsed timing.

## 4. Context & Memory Boundary Disclosures

- **Fresh Session Amnesia**: Fresh agent sessions start with clean conversation contexts and lack internal memory of prior interactions.
- **Durable Pointers**: Agents must rely exclusively on committed git history, remote issues, and structured records rather than ephemeral chat memory.
- **Compaction & Truncation**: When agent contexts exceed model limits, history is lossy; all decisions and progress must be saved to durable repository records before truncation occurs.
