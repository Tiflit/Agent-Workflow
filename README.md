# Agent-Workflow: Lightweight Manual Starter Template

> **Status:** Candidate starter template (v0.1 draft). Not adopted by external projects. Developer-governed, agent-neutral, stack-independent workflow.

## Overview

Agent-Workflow provides a lightweight, human-governed operational framework for collaborative software development with AI agents. It prioritizes cooperative safety, truthful evidence tracking, and strict scope control without requiring heavyweight automation frameworks or proprietary tooling.

By default, the workflow operates with **one active agent** under explicit human direction. The developer chooses which agent tools, models, local directories, and cloud resources to allocate.

## Core Principles

1. **Human Governance First**: Agents prepare changes, inspect artifacts, and propose bounded actions. Consequential changes (git pushes, PR merges, test execution) require human authorization.
2. **Advance Test Authorization**: Local test suites, runtime application launches, or desktop/hardware interactions **always require explicit, advance human authorization** defining allowed commands, targets, and disruption bounds. Tests are never run implicitly or unattended.
3. **Approval vs. Reporting**: Policy approval (what actions are permitted) is strictly separated from reporting cadence (how frequently status is communicated). Passing checks or progress notes never confer self-granted permissions.
4. **Truthful Evidence**: Only distinguish directly observed evidence from reported claims. Unexecuted tests or unavailable data remain explicitly labeled as unverified or unavailable.

## Quickstart: Manual Startup in 4 Steps

1. **Clone & Initialize**:
   Clone this repository into your project or copy its workflow documents (`KERNEL.md`, `REGISTER.md`, `AGENTS.md`, and `docs/`).
2. **Configure Register (`REGISTER.md`)**:
   Fill in placeholders for the human owner (`<OWNER_HANDLE>`), authorized control channels (e.g., GitHub Issues), approved processing destinations, and scope bounds.
3. **Dispatch First Task**:
   Create a bounded task (e.g., in an Issue or task contract) with:
   - Prohibitions stated first.
   - Authoritative task contract link and base commit SHA.
   - Objective, allowed file paths, and stopping criteria.
4. **Review & Iterate**:
   Review agent-submitted diffs, verify trails against [`docs/RECORDS.md`](docs/RECORDS.md), and conduct human verification before approving integration.

## Prerequisites & Candidate Limitations

- **Adoption Prerequisites**:
  - A configured version control repository (Git).
  - Explicit assignment of human owner and agent roles.
  - Review of privacy disclosures regarding model providers.
- **Candidate Limitations**:
  - This repository provides documentation templates only; it contains no automated CI enforcement or autonomous supervisor scripts.
  - Multi-agent coordination requires strict turn-taking and explicit human relays (see [`docs/PROFILES.md`](docs/PROFILES.md)).
  - Usability on arbitrary external projects is untested; users must adapt paths and checklists to their specific toolchain.

## Document Index

- [`KERNEL.md`](KERNEL.md): Invariant normative guarantees (v0.4).
- [`REGISTER.md`](REGISTER.md): Deployment-specific settings, identities, and boundaries.
- [`AGENTS.md`](AGENTS.md): Operational orientation and dispatch protocols for agents.
- [`docs/RECORDS.md`](docs/RECORDS.md): Schema for task contracts, checkpoints, and reviews.
- [`docs/CLAIMS.md`](docs/CLAIMS.md): Evidentiary claims boundaries and empirical trial findings.
- [`docs/PROFILES.md`](docs/PROFILES.md): Operational modes (Manual Default vs. Multi-Agent Relay).
- [`SECURITY.md`](SECURITY.md): Privacy and vulnerability reporting practices.
