"""
Author: NewtCode Anna Burova
Created: 2024-06
Updated: 2026-11

Functions:
    def greet(
        name: str,
        ) -> str
"""

from __future__ import annotations


def greet(
        name: str,
        ) -> str:
    """ ## Return a greeting for the supplied name.

    Args:
        name (str):
            Name to include in the greeting.

    Returns:
        out (str):
            A greeting with surrounding whitespace removed from the name.

    Raises:
        ValueError:
            If the name is empty or contains only whitespace.
    """

    normalized_name = name.strip()
    if not normalized_name:
        raise ValueError("name must not be empty")

    return f"Hello, {normalized_name}!"
