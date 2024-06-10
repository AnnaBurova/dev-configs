"""
Author: NewtCode Anna Burova
Created: 2024-06
Updated: 2026-11

Constants:
    CONSTANT_NAME (type)

Functions:
    def function_name(
        param1: type,
        param2: type = "default",
        ) -> return_type

Functions:
    def count_words(
        text: str,
        ) -> int
    def docstring_example(
        param1: int,
        param2: str = "default",
        # ) -> None
        # ) -> bool
        # ) -> int
        # ) -> str
        ) -> tuple[int, str]
"""

from __future__ import annotations


def count_words(
        text: str,
        ) -> int:
    """ ## Count whitespace-separated words in a string.

    This intentionally small example demonstrates a type-annotated function and a docstring.
    More advanced parsing rules can be added when needed.

    Args:
        text (str):
            Text to count.
            An empty string contains zero words.

    Returns:
        out (int):
            The number of whitespace-separated words.
    """

    return len(text.split())


def docstring_example(
        param1: int,
        param2: str = "default",
        # ) -> None:  # return None
        # ) -> bool:  # return True | False
        # ) -> int:  # return param1
        # ) -> str:  # return param2
        ) -> tuple[int, str]:  # return param1, param2
    """ ## Short description of what the function does.

    An optional longer description of what the function does on multiple lines.
    An optional longer description of what the function does on multiple lines.
    An optional longer description of what the function does on multiple lines.

    Args:
        param1 (int):
            Description of the first parameter.<br>
            Code:
            if else True False
            def function_call() -> None:
                return None
            function_call()
        param2 (str):
            Description of the second parameter.<br>
            Defaults to empty string.
            Defaults to 0 (the first element).
            Defaults to 5.
            Defaults to None.
            Defaults to True.
            Defaults to False.
            Defaults to "Unknown".
        *args (tuple):
            Variable length positional arguments.
        **kwargs (dict):
            Variable length keyword arguments.

    Returns:
        out (None):
            The function does not return a value.
    Returns:
        out (bool):
            True if the operation succeeds,<br>
            otherwise False.
    Returns:
        out (int):
            The result based on `param1`.
    Returns:
        out (str):
            A message generated using `param2`.
    Returns:
        out (tuple):
            A tuple containing multiple results.

    Raises:
        SystemExit:
            If user presses Ctrl+C (`KeyboardInterrupt`).
            If user enters `x` to exit.
            If no valid selection is made after 5 attempts.
            If directories do not match.
            If an error occurs and `stop=True`.
            Terminates with code 1.
        ValueError:
            If `param1` is less than zero or `param2` is empty.

    Examples:
        ```python
        Newt.function({3, 1, 2})
        # Output: '{1, 2, 3}'

        Newt.function(["hello"])
        # Output: '["hello"]'

        Newt.function(42)
        # Output: '42'
        ```
    """

    # TODO: Implement the function logic here

    # return None
    # return True
    # return False
    # return param1
    # return param2
    return param1, param2
