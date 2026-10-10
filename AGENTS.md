# Agent Orientation & Operating Instructions

> **Status:** Candidate orientation guide (v0.1 draft). Applies to agents active in this repository.

## 1. Startup & Instruction Acquisition

To bootstrap safely without impossible prerequisites, agents perform only the minimum reads necessary to acquire governing instructions:
1. **Governing Contract**: Acquire the dispatch message and referenced task contract. **Critical prohibitions must be listed first**.
2. **Read the Kernel Each Session**: Load and read [`KERNEL.md`](KERNEL.md) directly at session startup; its K1–K7 invariants are mandatory.
3. **Register Retrieval & Policy Comparison**: Retrieve bounded entries from [`REGISTER.md`](REGISTER.md) (principal, identity, destinations, execution profiles). Compare adopted kernel version and policy revision with a trusted prior checkpoint; refresh affected guidance when changed, missing, or divergent. Keep task and external permission drift checks separate.

## 2. Session Orientation

- **New Agents (Baseline Orientation)**:
  - Acquire a bounded overview of repository layout, project purpose, and task scope.
  - Verify baseline lineage: ensure the assigned base commit is an ancestor of the verified remote target ref (`git merge-base --is-ancestor <BASE_REV> <REMOTE_TARGET_REF>`).
- **Returning / Recovering Agents (Delta Orientation)**:
  - Do not treat session memory as authoritative. Inspect pushed remote commits and durable records to determine true completed state.
  - Reconcile missing or divergent refs before proposing actions.

## 3. Scope & Execution Rules

- **Objective Plus Effects**: Scope is defined by the objective, permitted file paths, and external side effects (network, filesystem, host processes).
- **Execution Boundaries**:
  - *Host Execution*: Local test suites, debugger runs, desktop/device interactions, and background processes **require explicit, advance, bounded human authorization**.
  - *Cloud / Environment Profiles*: Execution in approved cloud profiles (e.g., CI workflows) proceeds within declared task bounds.
  - Under the manual preset, unattended consequential actions are prohibited.
- **Truthful Evidence**: Explicitly label all claims as *executed*, *inspected*, *reported*, or *unavailable*.
