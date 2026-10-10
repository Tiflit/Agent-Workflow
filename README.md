# Agent-Workflow: Lightweight Manual Starter Template

> **Status:** Candidate starter template (v0.1 draft). Merging this candidate does not adopt it into external deployments. Developer-governed, agent-neutral, stack-independent workflow.

## Overview

Agent-Workflow provides a lightweight, human-governed operational framework for collaborative development with AI agents. It prioritizes cooperative safety, truthful evidence tracking, and strict scope control without heavyweight automation frameworks or proprietary tooling.

By default, the workflow operates with **one active agent** under explicit human direction. The developer chooses tools, models, local directories, and cloud resources.

## Core Principles

1. **Human Governance First**: Agents prepare changes, inspect artifacts, and propose bounded actions. Consequential actions (git pushes, PR merges, deployment) require human authorization. Unattended consequential actions are prohibited under the manual preset.
2. **Advance Host Execution Authorization**: Local test suites, runtime application launches, debugger sessions, or host-affecting background processes **always require explicit, advance, bounded human authorization**. Read-only public-source retrieval and approved cloud profiles proceed within declared task bounds.
3. **Approval vs. Reporting**: Policy approval is strictly separated from reporting cadence. Passing checks or progress notes never confer self-granted permissions.
4. **Truthful Evidence**: Explicitly distinguish evidence types: *executed*, *inspected*, *reported*, and *unavailable*.

## Quickstart: First-Run Adoption in 4 Steps

1. **Copy All Eight Template Documents**:
   Copy the complete template set (`README.md`, `KERNEL.md`, `REGISTER.md`, `AGENTS.md`, `SECURITY.md`, and `docs/{RECORDS,PROFILES,CLAIMS}.md`) into your repository, or explicitly adapt the policy-derivation command to the subset retained.
2. **Configure Register & Credentials**:
   In `REGISTER.md`, configure placeholders for human principal (`<HUMAN_OWNER_ID>`), control channel (`<PRIMARY_CONTROL_CHANNEL>`), verification method (`<CONTROL_AUTHORSHIP_VERIFICATION_METHOD>`), credential relationship / shared-account gaps, approved destinations, and execution profiles.
3. **Commit & Establish Trusted Checkpoint**:
   Commit configuration changes to version control. Derive the policy revision hash over the applicable policy files. Record this initial hash, adopted kernel version, approval source, and acquired base revision in a trusted control record (e.g., an attributable human-approved Issue comment) **outside the policy path set**. Do not embed the computed SHA inside policy files.
4. **Dispatch First Task**:
   Dispatch a bounded task contract referencing the trusted checkpoint, base revision, objective, allowed paths, and prohibitions first. If no checkpoint exists, the agent halts and requests its creation before proceeding.

## Candidate Limitations

- Provides documentation templates only; contains no automated CI enforcement or autonomous supervisor scripts.
- Multi-agent peer review is optional; read-only reviewers may use an explicit human-relay variant (see [`docs/PROFILES.md`](docs/PROFILES.md)).
- Usability on arbitrary external projects is untested; users must adapt paths and checklists.

## Document Index

- [`KERNEL.md`](KERNEL.md): Invariant normative guarantees (v0.4).
- [`REGISTER.md`](REGISTER.md): Deployment settings, identities, and boundaries.
- [`AGENTS.md`](AGENTS.md): Operational orientation and dispatch protocols.
- [`docs/RECORDS.md`](docs/RECORDS.md): Schemas for contracts, checkpoints, and reviews.
- [`docs/CLAIMS.md`](docs/CLAIMS.md): Evidentiary claims boundaries and reference limits.
- [`docs/PROFILES.md`](docs/PROFILES.md): Operational modes (Manual Default vs. Multi-Agent Relay).
- [`SECURITY.md`](SECURITY.md): Privacy and vulnerability reporting practices.
