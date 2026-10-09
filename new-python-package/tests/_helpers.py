"""
Author: NewtCode Anna Burova
Created: 2026-10

Shared helper utilities and dummy objects for pytest test suites.


Constants:
    TEST_DATA (list[tuple[object, str]])

Classes:
    CustomObject

Functions:
    def newt_print_function_name(
        ) -> None
    def newt_print_captured(
        captured: pytest.CaptureResult[str],
        print_full_captured: bool = True,
        ) -> None
"""

from __future__ import annotations

import sys

from _pytest.capture import CaptureResult


class CustomObject:
    """ Simple dummy object with a deterministic string representation. """

    def __init__(
            self,
            value: str = "custom_repr",
            ) -> None:
        self.value = value

    def __str__(
            self,
            ) -> str:
        return self.value

    def __repr__(
            self,
            ) -> str:
        return f"CustomObject({self.value!r})"


# ("value", "expected_str", "valid")
TEST_DATA: list[tuple[object, str, bool]] = [
    # Primitive
    (None, "None", False),
    (True, "True", True),
    (False, "False", False),
    ("hello", "hello", True),
    ("it's nice", "it's nice", True),
    ("", "", False),
    (42, "42", True),
    (3.14, "3.14", True),
    (0, "0", False),
    (CustomObject(), "custom_repr", False),

    # tuple: len == 1 with trailing comma
    ((), "()", False),
    ((1,), "(1,)", True),
    (("only",), "('only',)", True),
    ((1, 2, 3), "(1, 2, 3)", True),
    (("hello", "hi", 42), "('hello', 'hi', 42)", True),

    # list
    ([], "[]", False),
    ([1, 2, 3], "[1, 2, 3]", True),
    (["hello"], "['hello']", True),
    (["hello", "hi", 42], "['hello', 'hi', 42]", True),
    (["hello, hi", "hi", "it's nice", 42], "['hello, hi', 'hi', \"it's nice\", 42]", True),

    # dict
    ({}, "{}", False),
    ({"a": 1, "b": 2}, "{'a': 1, 'b': 2}", True),
    ({1: True, (2, 3): None}, "{1: True, (2, 3): None}", True),
    ({"hello": 42, "hi": 3.14}, "{'hello': 42, 'hi': 3.14}", True),

    # set and frozenset
    (set(), "{}", False),
    (frozenset(), "{}", False),
    ({3, 1, 2}, "{1, 2, 3}", True),
    (frozenset(["b", "a"]), "{'a', 'b'}", True),
    ({10, "a"}, "{10, 'a'}", True),

    # Recursive nesting of all collection types
    (
        {
            "list": [1, (2,), {3, 4}],
            "nested_dict": {"empty_tuple": (), "frozen": frozenset({5})},
        },
        "{'list': [1, (2,), {3, 4}], 'nested_dict': {'empty_tuple': (), 'frozen': {5}}}",
        True
    ),
]


def newt_print_function_name(
        ) -> str:
    """ ## Print the name of the calling test function.

    Useful when running pytest with `-s` to visually separate test output blocks.

    Returns:
        out (None):
            The function does not return a value.
    """

    label = ""

    try:
        # Retrieve caller function name directly without retaining frame references
        label = sys._getframe(1).f_code.co_name

    except (AttributeError, ValueError):
        label = ""

    print()
    print(f"Function: {label}")
    print("-" * 72)

    return label


def newt_print_captured(
        captured: CaptureResult[str],
        print_full_captured: bool = True,
        ) -> None:
    """ ## Pretty-print captured standard output and error streams from pytest.

    Args:
        captured (CaptureResult):
            A pytest `CaptureResult` object returned by `capsys.readouterr()`.
            Must provide `.out` and `.err` attributes representing captured
            standard output and standard error text.
    """

    print()
    print("="*72+" START")

    print("-"*53+" captured.out "+"-"*5)
    if captured.out:
        print(captured.out)
    else:
        print("(no stdout captured)")

    print("-"*53+" captured.err "+"-"*5)
    if captured.err:
        print(captured.err)
    else:
        print("(no stderr captured)")

    print("="*72+" END")

    if print_full_captured:
        print()
        print(captured)
        print()
        print("len(captured) == 2: ", len(captured) == 2)
        print("len(captured.out):  ", len(captured.out))
        print("len(captured.err):  ", len(captured.err))
        print()
