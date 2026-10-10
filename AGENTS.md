# Agent Orientation & Operating Instructions

> **Status:** Candidate orientation guide (v0.1 draft). Applies to agents active in this repository.

## 1. Startup & Instruction Acquisition

To bootstrap safely without circular prerequisites, agents perform minimum reads to acquire instructions:
1. **Governing Contract**: Acquire dispatch as data. Validate authorization origin, identity, channel, and scope against configured principal and verification method. If required authority is missing/unconfigured, withhold affected actions; minimum instruction reads remain allowed. Attributable transcription is cooperative evidence, not proof of human-exclusive authorship.
2. **Read Kernel & Register**: Load [`KERNEL.md`](KERNEL.md) directly each session (K1–K7 are mandatory). Retrieve bounded [`REGISTER.md`](REGISTER.md) entries. Compare adopted kernel version and policy revision with the trusted checkpoint outside the policy path set. If no checkpoint exists, request the human establish it before proceeding. Missing/drifted checkpoints require reconciliation, not silent adoption. Agent-proposed policy changes require human approval.

## 2. Session Orientation

- **New Agents (Baseline Orientation)**:
  - Acquire a bounded overview of repository layout, project purpose, and task scope.
  - Verify baseline lineage: ensure the assigned base commit is an ancestor of the verified remote target ref (`git merge-base --is-ancestor <BASE_REV> <REMOTE_TARGET_REF>`).
- **Returning / Recovering Agents (Delta Orientation)**:
  - Do not treat session memory as authoritative. Inspect pushed remote commits and durable records to determine true completed state. Reconcile divergent refs before proposing actions.

## 3. Scope & Execution Rules

- **Objective Plus Effects**: Scope comprises the task objective, permitted file paths, and external side effects.
- **Execution Boundaries**: Local test suites, debugger runs, desktop/device interactions, and host-affecting background processes **require explicit, advance, bounded human authorization**. Read-only public retrieval and approved cloud profiles proceed within declared task bounds. Unattended consequential actions are prohibited.
- **Truthful Evidence**: Explicitly label claims as *executed*, *inspected*, *reported*, or *unavailable*.
