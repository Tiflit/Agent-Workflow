# Deployment Enforcement Register — Manual Preset

> **Status:** Candidate starter deployment register (v0.1 draft). Deployment adaptation and enforcement declarations under [`KERNEL.md`](KERNEL.md).

## 1. Governance & Policy Identity

| Parameter | Configuration / Derivation | Description |
| :--- | :--- | :--- |
| **Candidate Kernel Version** | `v0.4` | Invariant normative rules from `KERNEL.md`. |
| **Owner Adoption Status** | `Candidate (Unadopted)` | Explicit human adoption state; unadopted templates do not override project rules. |
| **Applicable Policy Revision** | `git log -1 --format=%H <ACQUIRED_REV> -- README.md KERNEL.md REGISTER.md AGENTS.md SECURITY.md docs/RECORDS.md docs/PROFILES.md docs/CLAIMS.md` | Latest commit touching all eight policy/guidance files at acquired revision, compared against trusted checkpoint; external permission drift tracked separately. |
| **Human Principal** | `<HUMAN_OWNER_ID>` | Authorized human owner retaining ultimate approval and merge authority. |
| **Authorized Control Channel** | `<PRIMARY_CONTROL_CHANNEL>` | Official medium for task dispatch (e.g., repository Issue thread, terminal). |
| **Control Authorship Verification** | `<CONTROL_AUTHORSHIP_VERIFICATION_METHOD>` | Method for verifying authorization origin, identity, and scope. |
| **Credential Relationship** | `<CREDENTIAL_RELATIONSHIP>` | Declared identity relation (e.g., shared developer token vs. distinct agent bot). |
| **Session / Cost Ceiling** | `<SESSION_COST_OR_TOKEN_LIMIT>` | Developer-configured resource ceiling (or 'Unmetered/Unavailable'). |

## 2. Environment Profiles & Approved Destinations

- **Execution Profiles**:
  - *Host Execution Profile (`<HOST_PROFILE>`)*: Manual-cooperative. Local tests, debugger runs, desktop/device access, and background processes require advance, bounded human authorization. Unattended consequential actions are prohibited.
  - *Cloud Execution Profile (`<CLOUD_PROFILE>`)*: Bounded CI or container runs executing declared workflows.
- **Approved Processing Destinations & Purposes**:
  - Version Control: Remote repository origin (`<APPROVED_ORIGIN_URL>`) for approved branch pushes.
  - Model Inference: Approved LLM provider APIs (`<APPROVED_AI_PROVIDER>`) for authorized task analysis.
  - Unauthorized Destinations: External pastebins, unapproved cloud storage buckets, and public web endpoints are prohibited.

## 3. Kernel Guarantee Realization & Disclosures (K1–K7)

Starter defaults are labeled cooperative; technical controls remain unvalidated unless verified locally or in hosted environments.

| Guarantee | Declared Mechanism | Technical Status | Disclosed Gaps / Limitations |
| :--- | :--- | :--- | :--- |
| **K1 (Scope & Execution)** | Contract limits & human review | Cooperative (Unvalidated) | Filesystem isolation is unvalidated; worktrees do not establish process isolation; compliance is cooperative. |
| **K2 (Sensitive Information)** | Privacy patterns & destination rules | Cooperative (Unvalidated) | Egress monitoring and network filtering are unvalidated; outbound data protection relies on agent discipline. |
| **K3 (Truthful Evidence)** | Explicit evidence labeling (executed / inspected / reported / unavailable) | Cooperative | Uninspected claims are blocked by review; no automatic truth-enforcement probe exists. |
| **K4 (History Preservation)** | Non-destructive git commits & worktrees | Cooperative | Unpushed local commits remain vulnerable to disk loss; durability requires remote push. |
| **K5 (Untrusted Content)** | External inputs treated as data | Cooperative | Indirect prompt injection defense is prompt-level; parser does not cryptographically isolate text. |
| **K6 (Holds & Resume)** | Human-only resume; halt at safe boundaries | Cooperative | Holds stop active work at the next safe boundary; instant process kill is not guaranteed. |
| **K7 (Authority & Policy)** | Human-administered policy files | Cooperative | Shared human/agent credentials do not enforce independent human authorization technically. |

## 4. Stop Triggers & Safe Checkpointing

Agents halt work at the nearest safe boundary and checkpoint state upon:
1. Ambiguity in task contract, conflicting scope instructions, or missing base refs.
2. Detection of potential secrets, personal identifiers, or unapproved destination requests.
3. Authenticated human hold ("Hold", "Stop", "Pause") on the control channel.
4. Exhaustion of developer-configured cost/session ceilings or rate-limit warnings.
