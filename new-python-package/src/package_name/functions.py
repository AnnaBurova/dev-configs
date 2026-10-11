# Copyright (c) 2026 Anna Burova
"""Example module demonstrating function structure and docstrings.

Author: NewtCode Anna Burova
Created: 2026-10

Functions:
    def greet(
        name: str,
        ) -> str
    def count_words(
        text: str,
        ) -> int
"""


def greet(
        name: str,
        ) -> str:
    """## Return a greeting for the supplied name.

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
        message = "<name> must not be empty"
        raise ValueError(message)

    return f"Hello, {normalized_name}!"


def count_words(
        text: str,
        ) -> int:
    """## Count whitespace-separated words in a string.

    This small example demonstrates a type-annotated function and a docstring.
    More advanced parsing rules can be added when needed.

    Args:
        text (str):
            Text to count.<br>
            An empty string contains zero words.

    Returns:
        out (int):
            The number of whitespace-separated words.

    """
    return len(text.split())
