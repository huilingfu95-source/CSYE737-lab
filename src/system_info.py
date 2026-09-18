"""Student-facing system information module for Lab 01.

Students should complete the missing implementations below.
"""

from __future__ import annotations

import platform
import sys

def main() -> None:
    """Run a small demonstration of the environment report workflow."""
    try:
        report = build_environment_report("Student User")
    except NotImplementedError:
        print("Complete the TODO implementations in src/system_info.py before running this demo.")
        return

    print("Environment report:")
    for key in ("name", "python_version", "platform"):
        print(f"- {key}: {report[key]}")


def get_python_version() -> str:
    """Return the running Python version."""
    return platform.python_version()


def get_platform_name() -> str:
    """Return the operating-system/platform name."""
    return platform.system()


def normalize_name(name: str) -> str:
    """Return a normalized name suitable for display."""
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    normalized = name.strip()
    if not normalized:
        raise ValueError("name cannot be empty after stripping whitespace")
    return normalized


def build_environment_report(name: str) -> dict:
    """
    Return a dictionary describing the execution environment.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    normalized = normalize_name(name)
    return {
        "name": normalized,
        "python_version": get_python_version(),
        "platform": get_platform_name(),
    }


if __name__ == "__main__":
    main()
