# Copyright (c) 2026 Anna Burova
"""Comprehensive unit tests for the functions module.

Author: NewtCode Anna Burova
Created: 2026-10

Module: functions
Functions:
- greet
"""

from __future__ import annotations

import pytest

from ._helpers import (
    TEST_DATA,
    newt_print_function_name,
    newt_print_captured,
)

import package_name.functions as NewtCode


class TestGreet:
    """Tests for the greet() function."""

    @pytest.mark.parametrize(("given_value", "expected_str", "is_valid"), TEST_DATA)
    def test_greet(
            self,
            given_value: str,
            expected_str: str,
            is_valid: bool,
            capsys: pytest.CaptureFixture[str],
            ) -> None:
        """Ensure NewtCode.greet() formats valid names and rejects empty input."""
        func_name = newt_print_function_name()

        assert NewtCode.greet(given_value) == f"Hello, {expected_str}!"

        captured = capsys.readouterr()
        newt_print_captured(captured, verbose=False)

        min_captured_out_str = (
            "\n"
            f"Function: {func_name}\n"
            f"{'-' * 72}"
            "\n"
        )
        min_captured_out_len = len(min_captured_out_str)

        assert len(captured.out) == min_captured_out_len
        assert len(captured.err) == 0

        assert captured.out.count("::: ERROR :::") == 0
        assert captured.err.count("::: ERROR :::") == 0
