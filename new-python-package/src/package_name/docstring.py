# Copyright (c) 2026 Anna Burova
"""Docstring style guide and templates.

Author: NewtCode Anna Burova
Created: 2026-10

Functions:
    def docstring_example(
        param1: int,
        param2: str = "Unknown",
        *args: object,
        **kwargs: object,
        ) -> tuple[int, str]
"""

from __future__ import annotations

"""Reference examples of Python function return type annotations.

    ) -> return_type:

    # return None
    ) -> None:

    # return True | False
    ) -> bool:

    # return param1
    ) -> int:

    # return param2
    ) -> str:

    # return param1, param2
    ) -> tuple[int, str]:
"""

"""Reference examples of Google-style Args sections.

    Args:
        param1 (int):
            Description of the first parameter.<br>
            Optional multi-line explanation or inline snippet.<br>
            Code:
            if else True False
            def function_call() -> None:
                return None
            function_call()

        param2 (str):
            Description of the second parameter.<br>
            Defaults to an empty string.
            Defaults to 0 (the first element).
            Defaults to 5.
            Defaults to None.
            Defaults to True.
            Defaults to False.
            Defaults to "Unknown".

        *args (object):
            Variable-length positional arguments.

        **kwargs (object):
            Variable-length keyword arguments.
"""

"""Reference examples of Google-style Returns sections.

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
        out (tuple[int, str]):
            A tuple containing multiple results.
"""

"""Reference examples of Google-style Raises sections.

    Raises:
        SystemExit:
            If the user presses Ctrl+C (`KeyboardInterrupt`).<br>
            If the user enters `x` to exit.<br>
            If no valid selection is made after 5 attempts.<br>
            If directories do not match.<br>
            If an error occurs and `stop=True`.<br>

            Terminates with code 1.

        ValueError:
            If `param1` is less than zero or `param2` is empty.
            If the name is empty or contains only whitespace.
"""


def docstring_example(
        param1: int,
        param2: str = "Unknown",
        *args: object,
        **kwargs: object,
        ) -> tuple[int, str]:
    """## Short description of what the function does.

    An optional longer description explaining behavior, edge cases,
    and design nuances across multiple lines.

    Args:
        param1 (int):
            Description of the first parameter.<br>
            Optional multi-line explanation or inline snippet.<br>
            Code:
            if else True False
            def function_call() -> None:
                return None
            function_call()

        param2 (str):
            Description of the second parameter.<br>
            Defaults to "Unknown".

        *args (object):
            Variable-length positional arguments.

        **kwargs (object):
            Variable-length keyword arguments.

    Returns:
        out (tuple[int, str]):
            A tuple containing multiple results.

    Raises:
        SystemExit:
            Terminates with code 1.

    Examples:
        ```python
        Newt.docstring_example(42, "hello")
        # Output: (42, 'hello')

        Newt.docstring_example(1)
        # Output: (1, 'Unknown')
        ```

    """
    # TODO: Implement the function logic here

    for msg in args:
        print(msg)

    for key, val in kwargs.items():
        print(f"{key}={val}")

    return param1, param2
