"""
Author: NewtCode Anna Burova
Created: 2026-10

Comprehensive unit tests
Module: module
Functions:
- greet
"""

from __future__ import annotations

import pytest

import package_name.module as NewtCode

from ._helpers import (
    TEST_DATA,
    newt_print_captured,
    newt_print_function_name,
)


class TestGreet:
    """ Tests for greet function. """


    @pytest.mark.parametrize(("value", "expected_str", "valid"), TEST_DATA)
    def test_greet(
            self,
            value: object,
            expected_str: str,
            valid: bool,
            capsys: pytest.CaptureFixture[str],
            ) -> None:
        """ Ensure NewtCode.greet() formats all supported data types correctly. """

        func_name = newt_print_function_name()

        assert NewtCode.greet(value) == f"Hello, {expected_str}!"

        captured = capsys.readouterr()
        newt_print_captured(captured, False)

        min_captured_out_len = len(
            "\n"
            f"Function: {func_name}\n"
            f"{'-' * 72}"
            "\n"
        )

        assert len(captured.out) == min_captured_out_len
        assert len(captured.err) == 0

        assert captured.out.count("::: ERROR :::") == 0
        assert captured.err.count("::: ERROR :::") == 0
