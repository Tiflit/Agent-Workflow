# Agent Orientation & Operating Instructions

> **Status:** Candidate orientation guide (v0.1 draft). Applies to all AI agents active in this repository.

## 1. Mandatory Startup Rules

Before reading project files or taking any tool action:
1. **Kernel Invariants**: Read [`KERNEL.md`](KERNEL.md). Its 7 guarantees are non-negotiable.
2. **Deployment Register**: Read [`REGISTER.md`](REGISTER.md). Identify the human principal, approved channels, and disclosed enforcement gaps.
3. **Dispatch Contract**: Work only from an active dispatch message that explicitly names the authoritative task contract, human approval link, and base commit. **Critical prohibitions must be listed first**.

## 2. Session Orientation

- **New Agents (Initial Task Orientation)**:
  - Verify git clean state and confirm the base commit is an ancestor of the remote target branch (`git merge-base --is-ancestor <BASE> HEAD`).
  - Read only the assigned task files and context explicitly permitted by the dispatch contract.
- **Returning / Recovering Agents (Delta Orientation)**:
  - Do not assume prior session memory or local files remain authoritative.
  - Re-verify git lineage against the pushed remote head.
  - If baseline or task state is missing, divergent, or unpushed, broaden review to reconcile discrepancies before proceeding.

## 3. Scope & Execution Protocols

- **Objective Plus Effects**: Scope is defined by the task objective, permitted file paths, and external side effects (network, filesystem, shell). Bounded file paths alone do not authorize unpermitted side effects.
- **Advance Test Permission**: Never run test suites, build tools, or background processes unless explicitly authorized in the dispatch.
- **Checkpointing**: Record progress via structured checkpoint trailers (see [`docs/RECORDS.md`](docs/RECORDS.md)). Stop at natural boundaries and relinquish ownership.
