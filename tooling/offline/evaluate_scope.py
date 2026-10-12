"""Pure evaluation helper for checking changed files against allowed paths contracts."""

from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

try:
    from .parse_contract import AllowedPaths, ContractParseError, parse_allowed_paths
except ImportError:
    from parse_contract import AllowedPaths, ContractParseError, parse_allowed_paths


def normalize_allowed_paths_section(text: str) -> str:
    """Normalizes Issue body so subsequent markdown headings (# or ##) act as section delimiters for parse_allowed_paths."""
    if not text:
        return text
    pattern = r"(^###\s+Allowed paths\s*[\r\n]+[\s\S]*?)(?=^#{1,2}\s+)"
    return re.sub(pattern, r"\1\n### Section Boundary\n", text, count=1, flags=re.MULTILINE | re.IGNORECASE)


@dataclass
class ScopeResult:
    is_valid: bool
    violations: List[str]
    allowed_patterns: List[str]
    is_unconstrained: bool = False


def matches_pattern(file_path: str, pattern: str) -> bool:
    """Matches a normalized repository path against an allowed pattern."""
    norm_file = file_path.replace("\\", "/").strip("/")
    norm_pattern = pattern.replace("\\", "/").strip()

    if norm_pattern.endswith("/**"):
        prefix = norm_pattern[:-3]
        if not prefix.endswith("/"):
            prefix += "/"
        return norm_file.startswith(prefix)

    if norm_pattern.endswith("/"):
        return norm_file.startswith(norm_pattern)

    # Exact match
    return norm_file == norm_pattern.strip("/")


def check_files(
    files: List[Dict[str, Any]],
    patterns: List[str],
    is_unconstrained: bool = False,
) -> ScopeResult:
    """
    Checks changed files against allowed patterns.

    Renamed files check BOTH previous_filename and filename.
    """
    if is_unconstrained:
        return ScopeResult(is_valid=True, violations=[], allowed_patterns=[], is_unconstrained=True)

    violations: List[str] = []

    for file_info in files:
        filename = file_info.get("filename", "")
        previous_filename = file_info.get("previous_filename")

        # Check target filename
        if filename:
            if not any(matches_pattern(filename, p) for p in patterns):
                violations.append(filename)

        # Check previous filename for renames
        if previous_filename:
            if not any(matches_pattern(previous_filename, p) for p in patterns):
                rename_viol = f"{previous_filename} (renamed to {filename})"
                if rename_viol not in violations and previous_filename not in violations:
                    violations.append(rename_viol)

    return ScopeResult(
        is_valid=(len(violations) == 0),
        violations=violations,
        allowed_patterns=patterns,
        is_unconstrained=False,
    )
