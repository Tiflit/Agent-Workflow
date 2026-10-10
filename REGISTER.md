# Deployment Enforcement Register — Manual Preset

> **Status:** Candidate starter deployment register (v0.1 draft). Deployment declarations under [`KERNEL.md`](KERNEL.md). Candidate merge does not adopt into external deployments.

## 1. Governance & Policy Identity

| Parameter | Configuration / Derivation | Description |
| :--- | :--- | :--- |
| **Candidate Kernel Version** | `v0.4` | Invariant normative rules from `KERNEL.md`. |
| **Owner Adoption Status** | `Candidate (Unadopted)` | Explicit human adoption state; unadopted templates do not override project rules. |
| **Applicable Policy Derivation** | `git log -1 --format=%H <ACQUIRED_REV> -- README.md KERNEL.md REGISTER.md AGENTS.md SECURITY.md docs/RECORDS.md docs/PROFILES.md docs/CLAIMS.md` | Derives latest commit touching policy files at acquired revision. SHA is recorded in a trusted record outside this path set. |
| **Human Principal** | `<HUMAN_OWNER_ID>` | Authorized human owner retaining ultimate approval and merge authority. |
| **Authorized Control Channel** | `<PRIMARY_CONTROL_CHANNEL>` | Official medium for task dispatch (e.g., repository Issue thread, terminal). |
| **Control Authorship Verification** | `<CONTROL_AUTHORSHIP_VERIFICATION_METHOD>` | Verifies authorization origin, identity, and scope. Coordinator transcription is cooperative evidence, not proof of human-exclusive authorship. |
| **Credential Relationship** | `<CREDENTIAL_RELATIONSHIP>` | Declared identity relation and shared-account gap (e.g., shared developer token vs. distinct bot identity). |
| **Session / Cost Ceiling** | `<SESSION_COST_OR_TOKEN_LIMIT>` | Developer-configured resource ceiling (or 'Unmetered/Unavailable'). |

## 2. Environment Profiles & Approved Destinations

- **Execution Profiles**:
  - *Host Profile (`<HOST_PROFILE>`)*: Local tests, debuggers, devices, and host background processes require advance, bounded human authorization; unattended actions prohibited.
  - *Cloud Profile (`<CLOUD_PROFILE>`)*: Bounded CI/container runs under declared workflows.
- **Approved Processing Destinations & Purposes**:
  - VCS Origin (`<APPROVED_ORIGIN_URL>`), Model APIs (`<APPROVED_AI_PROVIDER>`). Public read-only retrieval permitted; sensitive data transmission to unapproved destinations prohibited.

## 3. Kernel Guarantee Realization & Disclosures (K1–K7)

Defaults are labeled cooperative; technical controls remain unvalidated unless verified locally or in hosted environments.

| Guarantee | Declared Mechanism | Technical Status | Disclosed Gaps / Limitations |
| :--- | :--- | :--- | :--- |
| **K1 (Scope & Execution)** | Contract limits & human review | Cooperative (Unvalidated) | Filesystem isolation unvalidated; worktrees do not isolate processes; compliance is cooperative. |
| **K2 (Sensitive Information)** | Privacy patterns & destination rules | Cooperative (Unvalidated) | Egress filtering unvalidated; outbound data protection relies on agent discipline. |
| **K3 (Truthful Evidence)** | Explicit labeling (executed / inspected / reported / unavailable) | Cooperative | Uninspected claims blocked by review; no automatic truth-enforcement probe exists. |
| **K4 (History Preservation)** | Non-destructive git commits & worktrees | Cooperative | Unpushed local commits vulnerable to disk loss; durability requires remote push. |
| **K5 (Untrusted Content)** | External inputs treated as data | Cooperative | Indirect injection defense is prompt-level; parser does not cryptographically isolate text. |
| **K6 (Holds & Resume)** | Human-only resume; halt at safe boundaries | Cooperative | Holds stop active work at next safe boundary; instant kill not guaranteed. |
| **K7 (Authority & Policy)** | Human-administered policy files | Cooperative | Shared credentials do not enforce human authorization. Agent-proposed policy changes require human approval. |

## 4. First-Run Bootstrap & Stop Triggers

- **First-Run Bootstrap**: If no trusted checkpoint exists, agents perform bounded instruction acquisition only and request the human establish it before executing tasks. Missing/drifted checkpoints require reconciliation, not silent adoption.
- **Stop Triggers**: Agents halt at the nearest safe boundary upon:
  1. Unconfigured authority, ambiguous contracts, or missing base refs.
  2. Secrets, personal identifiers, or unapproved destinations.
  3. Authenticated human hold ("Hold", "Stop") on the control channel.
  4. Exhausted cost/session ceilings or rate limits.
