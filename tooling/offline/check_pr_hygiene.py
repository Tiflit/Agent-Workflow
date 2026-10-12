"""Pure hygiene helper checking pull request description metadata against template headings and primary issue contract."""

from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import re
from dataclasses import dataclass
from typing import List, Optional

try:
    from .parse_contract import ContractParseError, extract_primary_issue
except ImportError:
    from parse_contract import ContractParseError, extract_primary_issue


REQUIRED_HEADINGS = [
    "Summary",
    "Scope",
    "Verification",
    "Documentation",
]


@dataclass
class HygieneResult:
    is_valid: bool
    missing_sections: List[str]
    primary_issue: Optional[int]
    diagnostics: List[str]


def verify_pr_body(body: str) -> HygieneResult:
    """Verifies that the PR body contains required sections and an unambiguous primary issue reference."""
    missing: List[str] = []
    diagnostics: List[str] = []

    if not body or not body.strip():
        return HygieneResult(
            is_valid=False,
            missing_sections=REQUIRED_HEADINGS + ["Primary Issue"],
            primary_issue=None,
            diagnostics=["PR body is empty."],
        )

    # Check for required section headings
    for heading in REQUIRED_HEADINGS:
        pattern = rf"^##\s+{re.escape(heading)}\s*$"
        if not re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
            missing.append(heading)
            diagnostics.append(f"Missing required section heading '## {heading}'.")

    # Check for primary issue reference
    primary_issue: Optional[int] = None
    try:
        primary_issue = extract_primary_issue(body)
    except ContractParseError as e:
        missing.append("Primary Issue")
        diagnostics.append(f"Primary issue error: {e}")

    return HygieneResult(
        is_valid=(len(missing) == 0),
        missing_sections=missing,
        primary_issue=primary_issue,
        diagnostics=diagnostics,
    )
