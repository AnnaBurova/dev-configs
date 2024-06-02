"""
Updated on YYYY-MM
Created on YYYY-MM

@author: NewtCode Anna Burova

Constants:
    CONSTANT_NAME (type)

Functions:
    def function_name(
        param1: type,
        param2: type = "default",
        ) -> return_type
    def docstring_example(
        param1: int,
        param2: str = "default",
        ) -> None
        ) -> bool
        ) -> int
        ) -> str
        ) -> tuple[int, str]
"""


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
            Always exits with code 1.
        ValueError:
            If `param1` is less than zero or `param2` is empty.
    """

    # TODO: Implement the function logic here

    # return None
    # return True
    # return False
    # return param1
    # return param2
    return param1, param2
