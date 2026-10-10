# Record Formats & Checkpoint Standards

> **Status:** Candidate record schema (v0.1 draft). Defines standard structured records for contracts, checkpoints, dispatches, and review observations under [`KERNEL.md`](../KERNEL.md).

## 1. Task Contract Record (Issue Body / Specification)
Word budget: `<= 350 words`.
- **Primary Task Reference**: `#<ISSUE_NUMBER>`
- **Human Approval Evidence**: Attributable human approval record / link.
- **Base Revision**: Full commit SHA of target baseline.
- **Allowed Scope**:
  - Tracked Paths: Explicit list of allowed files/directories.
  - Objective: Functional criteria and bounds.
  - Prohibitions: Forbidden operations (e.g., no tests, no push to main).
- **Stopping Criteria**: Observable milestone marking task completion.

## 2. Dispatch Activation Format (Comment)
Word budget: `<= 150 words`.
- **Prohibitions First**: Explicitly list all forbidden actions before instructions.
- **Authoritative Link**: Direct URL to governing task contract and approval record.
- **Assigned Agent**: Identifier of the assigned agent.
- **Target Branch / Base**: Active branch name and starting commit SHA.
- **Bounded Objective**: Specific deliverable authorized for this execution turn.

## 3. Git Checkpoint Trailers (Commit Message)
Trailers record operational context in commit messages. Trailers are informative records, never self-granted permissions.

```text
Task-Contract: #<ISSUE_NUMBER>
Base-Revision: <BASE_COMMIT_SHA>
Done: <Summary of completed steps in this commit>
Next: <Specific concrete next step, or omitted if awaiting direction>
Unresolved: <Known blockers, material uncertainties, or pending decisions>
Verified-Revision: <SHA of last revision verified by tests, or 'Unverified'>
```

- **Checkpoint vs. Verified Revision**: `Base-Revision` is the starting point; `Verified-Revision` records only revisions where test evidence was executed and established.
- **Local vs. Pushed Durability**: Local commits are unpushed working state; durable recovery requires pushing to the remote branch.
- **Natural Boundaries**: Commit and checkpoint at logical unit completions or when context length/token budget approaches limits.

## 4. Review & Observation Format (Review Comment)
Word budget: `<= 250 words`.
- **Reviewed Target**: Commit SHA and branch.
- **Reviewer Identity & Relationship**: State identity and disclose reviewer relationship honestly (e.g., "Self-Review by Author", "Peer Agent Review", or "Human Review"). Never present self-review as independent validation.
- **Inspection Scope**: Evaluated files and diffs.
- **Findings & Disposition**:
  - In-scope defects: Document exact findings; in-scope repairs may be proposed or executed within assigned task limits.
  - Out-of-scope findings: Record as advisory notes; agents MUST NOT self-authorize expanding scope to address them.
- **Ownership Transfer**: State explicit handover to the next owner (e.g., "Yielding ownership to <OWNER>"). Ownership transfers only by explicit message; automatic timeout takeovers are prohibited.
