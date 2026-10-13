# Agent-Workflow: Lightweight Manual Starter Template

> **Status:** Candidate starter template (v0.1 draft). Merging this candidate does not adopt it into external deployments. Developer-governed, agent-neutral, stack-independent workflow.

## Overview

Agent-Workflow provides a lightweight, human-governed operational framework for collaborative development with AI agents. It prioritizes cooperative safety, truthful evidence tracking, and strict scope control without heavyweight automation frameworks or proprietary tooling.

By default, the workflow operates with **one active agent** under explicit human direction. The developer chooses tools, models, local directories, and cloud resources. The repository provides manual starter templates alongside an optional offline preflight and role-preview toolkit ([`tooling/offline/README.md`](tooling/offline/README.md)); using the toolkit is strictly opt-in and does not alter the core eight-document adoption path.

## Core Principles

1. **Human Governance First**: Agents prepare changes, inspect artifacts, and propose bounded actions. Consequential actions (git pushes, PR merges, deployment) require human authorization. Unattended consequential actions are prohibited under the manual preset.
2. **Advance Host Execution Authorization**: Local test suites, runtime application launches, debugger sessions, or host-affecting background processes **always require explicit, advance, bounded human authorization**. Read-only public-source retrieval and approved cloud profiles proceed within declared task bounds.
3. **Approval vs. Reporting**: Policy approval is strictly separated from reporting cadence. Passing checks or progress notes never confer self-granted permissions.
4. **Truthful Evidence**: Explicitly distinguish evidence types: *executed*, *inspected*, *reported*, and *unavailable*.

## Quickstart: First-Run Adoption in 4 Steps

For a detailed step-by-step guide on Windows PowerShell, see [`docs/WINDOWS-FIRST-RUN.md`](docs/WINDOWS-FIRST-RUN.md).

1. **Copy All Eight Template Documents**:
   Copy the complete template set (`README.md`, `KERNEL.md`, `REGISTER.md`, `AGENTS.md`, `SECURITY.md`, and `docs/{RECORDS,PROFILES,CLAIMS}.md`) into your repository, or adapt the policy-derivation command to the subset retained.
2. **Configure Register, Review & Adopt v0.4**:
   In `REGISTER.md`:
   - Review and adopt v0.4, updating `Owner Adoption Status` from candidate to adopted before committing policy (this template repository ships unadopted).
   - Configure placeholders for human principal (`<HUMAN_OWNER_ID>`), control channel (`<PRIMARY_CONTROL_CHANNEL>`), verification method (`<CONTROL_AUTHORSHIP_VERIFICATION_METHOD>`), credential relationship / shared-account gaps, destinations, execution profiles, and a stable `<TRUSTED_CHECKPOINT_RECORD>` locator (e.g., Issue #1 or governance thread outside policy paths).
3. **Commit Configured Policy & Complete External Record**:
   Commit configured policy files to version control before task execution. Derive the policy revision hash over the applicable policy files. In the configured external checkpoint record, record this derived SHA, adopted kernel version, approval source, and base revision. Do not edit covered policy files to insert the computed SHA.
4. **Dispatch First Task**:
   Dispatch a bounded task contract referencing the trusted checkpoint record, base revision, objective, allowed paths, and prohibitions first. If no checkpoint exists, agents halt and request its establishment before proceeding.

## Candidate Limitations

- Provides a manual starter template with an optional offline preflight and role-preview toolkit ([`tooling/offline/README.md`](tooling/offline/README.md)); contains no autonomous supervisor, dispatch automation, agent synchronization, or validated execution sandboxes. Repository cloud CI exercises offline toolkit fixtures only, distinguishing fixture verification from enforced task, merge, or authority gates.
- Multi-agent peer review is optional; read-only reviewers may use an explicit human-relay variant (see [`docs/PROFILES.md`](docs/PROFILES.md)).
- Usability on arbitrary external projects is largely untested; users must adapt paths and checklists. Assisted onboarding was demonstrated in [Issue #3](https://github.com/Tiflit/Agent-Workflow/issues/3#issuecomment-6103291947) (see [`docs/WINDOWS-FIRST-RUN.md`](docs/WINDOWS-FIRST-RUN.md)). Clean copied-project layout and CLI portability were demonstrated across 7 bootstrap tests in [`docs/CLEAN-BOOTSTRAP-TRIAL.md`](docs/CLEAN-BOOTSTRAP-TRIAL.md) ([PR #11](https://github.com/Tiflit/Agent-Workflow/pull/11#issuecomment-6136015866)), and fresh-session read-only navigation was demonstrated as human-relayed and source-adjudicated without blocking navigation defects in [Issue #12](https://github.com/Tiflit/Agent-Workflow/issues/12#issuecomment-6136188844) (without independent agent context-isolation proof). Manual human relay remains the operating mode; autonomous dispatch, unassisted full adoption, automated enforcement, and adopted upstream sync remain unshown and untested.

## Document Index

- [`KERNEL.md`](KERNEL.md): Invariant normative guarantees (v0.4).
- [`REGISTER.md`](REGISTER.md): Deployment settings, identities, and boundaries.
- [`AGENTS.md`](AGENTS.md): Operational orientation and dispatch protocols.
- [`docs/WINDOWS-FIRST-RUN.md`](docs/WINDOWS-FIRST-RUN.md): Step-by-step Windows onboarding recipe and publication practices.
- [`docs/CLEAN-BOOTSTRAP-TRIAL.md`](docs/CLEAN-BOOTSTRAP-TRIAL.md): Clean-project bootstrap trial and offline toolkit portability evidence.
- [`docs/RECORDS.md`](docs/RECORDS.md): Schemas for contracts, checkpoints, and reviews.
- [`docs/CLAIMS.md`](docs/CLAIMS.md): Evidentiary claims boundaries and reference limits.
- [`docs/PROFILES.md`](docs/PROFILES.md): Operational modes (Manual Default vs. Multi-Agent Relay).
- [`SECURITY.md`](SECURITY.md): Privacy and vulnerability reporting practices.
- [`tooling/offline/README.md`](tooling/offline/README.md): Optional offline preflight and role-preview toolkit documentation.
