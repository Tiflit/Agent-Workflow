# Windows First-Run Recipe: Manual Starter Onboarding

> **Status:** Candidate operational recipe (v0.1 draft). Step-by-step guidance for manual adoption on Windows under [`KERNEL.md`](../KERNEL.md) and [`REGISTER.md`](../REGISTER.md).

## 1. Overview & Governance Prerequisites

This recipe provides a reproducible onboarding sequence for adopting the manual starter workflow on Windows environments, reflecting operational findings from reference usability trials ([Issue #3](https://github.com/Tiflit/Agent-Workflow/issues/3#issuecomment-6103291947)).

Before executing commands, establish the governance baseline:
- **Authorization Bounds**: All directory provisioning, cloning, policy modification, local commits, and external publications require explicit, bounded human authorization. Unattended consequential actions are prohibited.
- **Shared Credentials & Attribution**: When agents operate in the developer's console, declare the shared-account gap in [`REGISTER.md`](../REGISTER.md). Local Git identity configurations are optional attribution markers; they do not establish technical identity separation or authorization.
- **Workspace Scope & Process Isolation**: Confine file operations and Git commands to the designated task workspace (`<PROJECT_ROOT>`). Use generic placeholders in public records; never disclose private host paths or user profiles. Working in a designated folder does not establish technical process, network, or OS isolation; compliance is cooperative.
- **Tooling Prerequisites**: Standard Windows PowerShell 5.1+ or PowerShell 7+, Git CLI, and GitHub CLI (`gh`).

## 2. Template Acquisition & Document Reconciliation

Do not clone or unpack template files directly over an existing project working tree. Acquire the pinned template into an isolated staging location first:

```powershell
# Acquire pinned template into isolated staging area
git clone --no-checkout https://github.com/Tiflit/Agent-Workflow.git "<STAGING_DIR>/source"
git -C "<STAGING_DIR>/source" checkout --detach <PINNED_TEMPLATE_REV>
```

Before copying, verify destination paths. If any of the eight workflow documents already exist in the target project, halt copying immediately; existing-project integration requires deliberate, human-reviewed reconciliation:

```powershell
# Stop before copying if any destination file already exists
$destFiles = @(
    'README.md', 'KERNEL.md', 'REGISTER.md', 'AGENTS.md', 'SECURITY.md',
    'docs/RECORDS.md', 'docs/PROFILES.md', 'docs/CLAIMS.md'
)
$collisions = $destFiles | Where-Object { Test-Path "<PROJECT_ROOT>/$_" }
if ($collisions) {
    Write-Error "Destination collisions detected: $($collisions -join ', '). Stop: existing files require deliberate human reconciliation."
    return
}

# Copy eight template documents into project repository
New-Item -ItemType Directory -Path "<PROJECT_ROOT>/docs" -Force
foreach ($f in $destFiles) {
    Copy-Item "<STAGING_DIR>/source/$f" "<PROJECT_ROOT>/$f"
}
```

## 3. Configuring the Deployment Register (`REGISTER.md`)

Open `<PROJECT_ROOT>/REGISTER.md` and replace template placeholders with concrete, bounded declarations:
- **Kernel Version**: Invariant `v0.4`.
- **Owner Adoption Status**: Update from `Candidate (Unadopted)` to `Adopted (v0.4)` only upon explicit human review and authorization.
- **Human Principal**: Authorized human owner (`<HUMAN_OWNER_ID>`) retaining final merge and policy authority.
- **Authorized Control Channel**: Designated issue tracker (`<PRIMARY_CONTROL_CHANNEL>`, e.g., GitHub Issue thread) and operator console.
- **Control Authorship Verification**: Method for confirming human instructions (`<CONTROL_AUTHORSHIP_VERIFICATION_METHOD>`), such as direct terminal command or coordinator transcription (declared as cooperative evidence).
- **Credential Relationship**: Declare shared developer token or local console session gap (`<CREDENTIAL_RELATIONSHIP>`).
- **Session / Cost Ceiling**: Mandatory stopping limit (e.g., `60-minute session stopping limit; token cost unmetered/unavailable`).
- **Execution Profiles**: Declare Host Profile (PowerShell file edits and local Git commands bounded to project root; local tests/apps/builds require advance human authorization) and Cloud Profile.
- **Approved Destinations**: Declare VCS remote, model API endpoints, and permitted public read retrieval.
- **Trusted Checkpoint Locator**: Stable external locator outside policy paths (`<TRUSTED_CHECKPOINT_RECORD>`, e.g., `https://github.com/<OWNER>/<REPO>/issues/<ISSUE_ID>`).

## 4. Explicit Staging, Commit & Policy Derivation

Stage only the named policy paths to prevent accidental inclusion of untracked build artifacts or private files:

```powershell
# Explicitly stage the eight policy documents
git -C "<PROJECT_ROOT>" add README.md KERNEL.md REGISTER.md AGENTS.md SECURITY.md docs/RECORDS.md docs/PROFILES.md docs/CLAIMS.md

# Commit adoption under designated attribution
git -C "<PROJECT_ROOT>" commit -m "docs: adopt agent-workflow v0.4 manual starter"
```

Derive the policy revision hash across all applicable policy paths:

```powershell
# Derive policy SHA over applicable policy paths
$policySha = git -C "<PROJECT_ROOT>" log -1 --format=%H HEAD -- README.md KERNEL.md REGISTER.md AGENTS.md SECURITY.md docs/RECORDS.md docs/PROFILES.md docs/CLAIMS.md
```

**Critical Invariant**: Never edit policy files after committing to insert `$policySha`. The policy SHA must be recorded exclusively in the external checkpoint record to avoid circular hash invalidation.

## 5. Publishing Checkpoints Without Shell Quoting Corruption

In Windows PowerShell, inlining multi-line Markdown into CLI arguments (`gh issue comment --body "..."`) risks string interpolation errors, escape-backslash leakage, and ASCII control character insertion (e.g., U+000B vertical tabs).

To avoid string-escaping corruption:
1. Write the checkpoint content to a literal UTF-8 Markdown staging file outside the tracked Git repository (`<STAGING_DIR>/checkpoint-evidence.md`).
2. Include concrete adoption parameters in the draft:

```powershell
# Write literal UTF-8 checkpoint draft without BOM (PowerShell 5.1 and 7+ compatible)
$draftContent = @"
## Checkpoint — v0.4 Adoption Record
- **Adopted Kernel**: v0.4
- **Policy SHA**: <POLICY_SHA>
- **Base Revision**: <BASE_REV>
- **Approval Pointer**: <APPROVAL_RECORD_URL>
- **Attribution**: <HUMAN_OWNER_ID> (human) / shared-credential gap declared.
"@
# Replace placeholders before writing
[System.IO.File]::WriteAllText("<STAGING_DIR>/checkpoint-evidence.md", $draftContent, [System.Text.UTF8Encoding]::new($false))
```

3. Publish using the `--body-file` parameter:

```powershell
# Publish checkpoint using literal UTF-8 file and capture URL
$commentUrl = gh issue comment <ISSUE_NUM> --repo <OWNER>/<REPO> --body-file "<STAGING_DIR>/checkpoint-evidence.md"
```

4. Read back the specific posted comment by its ID and compare the fetched text to the draft:

```powershell
# Extract comment ID from URL and fetch the exact comment body
$commentId = $commentUrl.Trim().Split('/')[-1].Replace('#issuecomment-', '')
$fetchedBody = (gh api "repos/<OWNER>/<REPO>/issues/comments/$commentId" --jq ".body") -join "`n"
$draftText = [System.IO.File]::ReadAllText("<STAGING_DIR>/checkpoint-evidence.md", [System.Text.Encoding]::UTF8)

# Verify exact match; preserve any discrepancy in evidence records rather than rewriting history
if ($fetchedBody -ne $draftText) {
    Write-Warning "Publication discrepancy detected: fetched comment does not match local draft."
}
```

## 6. First Task Dispatch & Fresh Startup

Once the external checkpoint record is published with the derived policy SHA, adopted version, base revision, and approval link, dispatch tasks using bounded contracts:
- **Prohibitions First**: State forbidden actions before tasks (no unapproved tests, builds, app execution, pushes, or out-of-scope edits).
- **Task Contract**: Specify objective, base revision, and strictly allowed file paths.
- **Fresh Agent Startup**: Incoming agents MUST read [`KERNEL.md`](../KERNEL.md) and [`REGISTER.md`](../REGISTER.md) at startup, and validate dispatch origin, channel, identity, and scope against configured authority before execution. If the trusted checkpoint is missing or drifted, agents must halt and request human reconciliation. Reaching the configured session ceiling is a mandatory stop trigger.
