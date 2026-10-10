# Record Formats & Checkpoint Standards

> **Status:** Candidate record schema (v0.1 draft). Defines standard structured records for contracts, checkpoints, dispatches, and review observations under [`KERNEL.md`](../KERNEL.md).

## 1. Task Contract Record (Issue Body / Specification)
Word budget: `<= 350 words`.
- **Primary Task Reference**: `#<ISSUE_NUMBER>`
- **Objective**: Functional task goal, acceptance criteria, and operational bounds.
- **Assigned Owner & Branch**: Assigned agent role (`<AGENT_ROLE>`) and target branch (`<TARGET_BRANCH>`).
- **Human Approval Evidence**: Attributable human approval record or direct thread link.
- **Base Revision**: Full commit SHA of the starting baseline.
- **Authoritative Activation Pointer**: Link to the currently active dispatch comment.
- **Allowed Scope & Resources**:
  - Tracked Paths: Explicit list of allowed files and directories.
  - Permitted Environment & Effects: Permitted host/cloud profiles, tools, and side effects.
  - Prohibitions First: Specific forbidden actions (e.g., no tests, no push to main).
- **Required Acceptance Evidence**: Observable criteria and required evidence type (inspected or executed).

## 2. Dispatch Activation Format (Comment)
Word budget: `<= 150 words`.
- **Prohibitions First**: Explicitly list all forbidden actions before operational instructions.
- **Authoritative Link**: Direct URL to governing task contract and approval record.
- **Assigned Agent**: Identifier of the assigned agent.
- **Target Branch / Base**: Active branch name and starting commit SHA.
- **Bounded Objective**: Specific deliverable authorized for this turn.

## 3. Git Checkpoint Trailers (Commit Message)
Trailers record operational context in commit messages. Trailers are informative records, never self-granted permissions.

```text
Task-Contract: #<ISSUE_NUMBER>
Base-Revision: <BASE_COMMIT_SHA>
Done: <Summary of completed steps in this commit>
Next: <Specific concrete next step, or omitted if awaiting direction>
Unresolved: <Known blockers, material uncertainties, or pending decisions>
Verified-Revision: <COMMIT_SHA | 'Unverified'>
Evidence-Type: <Executed | Inspected | Unavailable>
Evidence-Outcome: <Pass | Fail | AttentionRequired | None>
```

- **Verified Revision & Evidence**: `Verified-Revision` records only a verified commit SHA or `Unverified`. The associated `Evidence-Type` (executed vs. inspected) and `Evidence-Outcome` record verification nature and result (e.g., executed tests or inspected document links/budgets).
- **Local vs. Pushed Durability**: Local commits survive conversation loss on intact storage; pushing adds remote durability. Neither guarantees recovery from arbitrary hardware loss.
- **Natural Checkpoint Boundaries**: Commit and checkpoint at logical unit completions or upon approaching context limits.

## 4. Review & Observation Format (Review Comment)
Word budget: `<= 250 words`.
- **Reviewed Target**: Commit SHA and branch.
- **Reviewer Identity & Relationship**: State identity and disclose reviewer relationship honestly (e.g., "Self-Review by Author", "Peer Agent Review", or "Human Review"). Never present self-review as independent validation.
- **Findings & Triage**:
  - In-scope defects: Document exact findings; in-scope repairs may be performed within task bounds.
  - Out-of-scope observations: Document for human or peer triage before promoting to new tasks; agents MUST NOT self-authorize expanding scope.
- **Explicit Ownership Transfer**: State explicit handover to the next owner (e.g., "Yielding ownership to <NEXT_OWNER>"). Ownership transfers only by explicit authorized reassignment; automatic timeout takeovers are prohibited.
