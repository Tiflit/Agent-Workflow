# Windows First-Run Recipe: Manual Starter Onboarding

> **Status:** Candidate operational recipe (v0.1 draft). Step-by-step guidance for manual adoption on Windows under [`KERNEL.md`](../KERNEL.md) and [`REGISTER.md`](../REGISTER.md).

## 1. Overview & Governance Prerequisites

This recipe provides a reproducible, step-by-step onboarding sequence for adopting the manual starter workflow on Windows environments. It reflects operational findings from reference usability trials ([Issue #3](https://github.com/Tiflit/Agent-Workflow/issues/3#issuecomment-6103291947)).

Before executing commands, establish the governance baseline:
- **Authorization Bounds**: All directory provisioning, cloning, policy modification, local commits, and external publications require explicit, bounded human authorization. Unattended consequential actions are prohibited.
- **Shared-Credential Model**: When agents operate in the developer's console, declare the shared-account gap in [`REGISTER.md`](../REGISTER.md). Synthetic local Git identities represent attribution markers, not technical authorization separation.
- **Path Isolation**: Execute within a dedicated project path (`<PROJECT_ROOT>`). Use placeholders in public records; never disclose private host paths or user profile directories.
- **Tooling Prerequisites**: Standard Windows PowerShell 5.1+ or PowerShell 7+, Git CLI, and GitHub CLI (`gh`).

## 2. Template Acquisition & Document Reconciliation

Do not clone or unpack template files directly over an existing project working tree without inspection. Acquire the pinned template into an isolated staging location first:

```powershell
# Acquire pinned template into isolated staging area
git clone --no-checkout https://github.com/Tiflit/Agent-Workflow.git "<STAGING_DIR>/source"
git -C "<STAGING_DIR>/source" checkout --detach <PINNED_TEMPLATE_REV>
```

Before copying, reconcile existing project documents:
1. If the project already contains a `README.md` or `SECURITY.md`, do not blind-overwrite them. Integrate workflow governance sections into existing files or adapt the retained policy path list.
2. Copy the eight template workflow documents into the project repository:
   - Root: `README.md`, `KERNEL.md`, `REGISTER.md`, `AGENTS.md`, `SECURITY.md`
   - Documentation directory: `docs/RECORDS.md`, `docs/PROFILES.md`, `docs/CLAIMS.md`

```powershell
# Copy template files into project repository
$files = @('README.md', 'KERNEL.md', 'REGISTER.md', 'AGENTS.md', 'SECURITY.md')
foreach ($f in $files) { Copy-Item "<STAGING_DIR>/source/$f" "<PROJECT_ROOT>/$f" }
New-Item -ItemType Directory -Path "<PROJECT_ROOT>/docs" -Force
$docFiles = @('RECORDS.md', 'PROFILES.md', 'CLAIMS.md')
foreach ($df in $docFiles) { Copy-Item "<STAGING_DIR>/source/docs/$df" "<PROJECT_ROOT>/docs/$df" }
```

## 3. Configuring the Deployment Register (`REGISTER.md`)

Open `<PROJECT_ROOT>/REGISTER.md` and replace template placeholders with concrete, bounded declarations:
- **Kernel Version**: Invariant `v0.4`.
- **Owner Adoption Status**: Update from `Candidate (Unadopted)` to `Adopted (v0.4)` only upon explicit human review and authorization.
- **Human Principal**: Authorized human owner (`<HUMAN_OWNER_ID>`) retaining final merge and policy authority.
- **Authorized Control Channel**: Designated issue tracker (`<PRIMARY_CONTROL_CHANNEL>`, e.g., GitHub Issue thread) and operator console.
- **Control Authorship Verification**: Method for confirming human instructions (`<CONTROL_AUTHORSHIP_VERIFICATION_METHOD>`), such as direct terminal command or coordinator transcription (declared as cooperative evidence).
- **Credential Relationship**: Declare shared developer token or local console session gap (`<CREDENTIAL_RELATIONSHIP>`).
- **Session / Cost Ceiling**: Bounded session checkpoint (e.g., `60-minute session checkpoint; token cost unmetered/unavailable`).
- **Execution Profiles**: Declare Host Profile (PowerShell file edits and local Git commands bounded to project root; local tests/apps/builds require advance human authorization) and Cloud Profile.
- **Approved Destinations**: Declare VCS remote, model API endpoints, and permitted public read retrieval.
- **Trusted Checkpoint Locator**: Set a stable external locator outside policy paths (`<TRUSTED_CHECKPOINT_RECORD>`, e.g., `https://github.com/<OWNER>/<REPO>/issues/<ISSUE_ID>`).

## 4. Explicit Staging, Commit & Policy Derivation

Stage only the named policy paths to prevent accidental inclusion of untracked build artifacts or private files:

```powershell
# Explicitly stage the eight policy documents
git -C "<PROJECT_ROOT>" add README.md KERNEL.md REGISTER.md AGENTS.md SECURITY.md docs/RECORDS.md docs/PROFILES.md docs/CLAIMS.md

# Commit adoption under local synthetic attribution
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

To guarantee publication integrity:
1. Write the checkpoint content to a literal UTF-8 Markdown staging file outside the tracked Git repository (`<STAGING_DIR>/checkpoint-evidence.md`).
2. Publish using the `--body-file` parameter:

```powershell
# Publish checkpoint using literal UTF-8 file
gh issue comment <ISSUE_NUM> --repo <OWNER>/<REPO> --body-file "<STAGING_DIR>/checkpoint-evidence.md"
```

3. Read back the posted comment via API and verify character and SHA integrity:

```powershell
# Read back comment and verify absence of control characters
$body = (gh issue view <ISSUE_NUM> --repo <OWNER>/<REPO> --json comments --jq ".comments[-1].body") -join "`n"
$badChars = $body.ToCharArray() | Where-Object { [int]$_ -lt 32 -and $_ -ne 10 -and $_ -ne 13 -and $_ -ne 9 }
if ($badChars.Count -gt 0) { Write-Warning "Detected $($badChars.Count) control characters in published comment." }
```

## 6. First Task Dispatch & Fresh Startup

Once the external checkpoint record is published with the derived policy SHA, adopted version, base revision, and approval link, dispatch tasks using bounded contracts:
- **Prohibitions First**: State forbidden actions before tasks (no unapproved tests, builds, app execution, pushes, or out-of-scope edits).
- **Task Contract**: Specify objective, base revision, and strictly allowed file paths.
- **Fresh Agent Startup**: Incoming agents inspect the trusted checkpoint locator, verify base commit ancestry (`git merge-base --is-ancestor <BASE_REV> <REMOTE_REF>`), confirm clean status, verify policy revision consistency, and perform changes within stated boundaries.
