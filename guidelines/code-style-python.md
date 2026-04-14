# NewtCode Python Code Style Guide

This document defines the Python code style conventions, structure, documentation, error handling, and cross-platform behavior used across NewtCode projects.

Following these standards helps keep the codebase consistent, reliable, and maintainable.

---

## Development Environment

- `newtutils` is a must-have utility for working with projects
- **Python versions**: 3.14

---

## General Rules to PEP 8 and PEP 484

PEP 8 - Style Guide for Python Code

PEP 484 - Type Hints

- Use 4 spaces per indentation level.
- Soft limit lines is 80 characters.
- Hard limit lines is 120 characters.
- Set rulers to [80, 100, 120] in editor.
- Write all comments and docstrings in English.
- Use `utf-8` encoding for all files.
- Normalize all newlines to `\n` and `LF`.
- For code examples:
  - `docstring.py` is a reference for Google-style docstrings.
  - `script.py` is a reference for general code style and structure.

### Import statements examples:

Imports should be grouped in the following order:

- Standard library imports.
- Related third party imports.
- Local application/library specific imports.

Check `new-repo/LICENSE` for the best order list of **standard library modules** used in NewtCode projects.

### Type annotations examples:

```python
from __future__ import annotations
data: int | str | None = None  # can be int, str, or None
data: list[int | str] = [1, "two", 3]  # list of int or str elements
data: set[int | str] = {1, "two", 3}  # set of int or str elements
data: tuple[int, str] = (1, "two")  # first element must be int, second must be str
data: dict[str, int] = {"a": 1, "b": 2}  # keys must be str, values must be int
```

### Bracket placement examples:

```python
my_list = [
    "item1",
    "item2",
    "item3",
]
```

```python
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
```

### If-Else Statements examples:

```python
if var1 > var2:
    do_something_1()
elif var1 == var2:
    do_something_2()
else:
    do_something_3()
```

```python
variable = value_if_true if condition else value_if_false

do_something_1() if var1 > var2 else do_something_2()

do_something_1() if var1 > var2 else do_something_2() if var1 == var2 else do_something_3()
```

```python
if var1 > var2 and var3 > var4:
    do_something_1()
if var1 > var2 or var3 > var4:
    do_something_2()
if not var1 > var2:
    do_something_3()
if foo is not None:
    do_something_4()
```

```python
if (
    var1 > var2
    and var3 > var4
):
    do_something_1()
elif (
    var1 > var2
    or var3 > var4
):
    do_something_2()
else:
    do_something_3()
```

### Backslash usage examples:

```python
with open('/path/to/some/file/with/very/long/path/to/read') as file_1, \
     open('/path/to/some/file/with/very/long/path/to/write', 'w') as file_2:
    file_2.write(file_1.read())
```

---

## Input Validation

- Explicitly type-check every input parameter before processing.
- If an input is invalid, log the issue using `newtutils.console.error_msg()`.
- Use `stop=True` only when execution cannot continue safely.

Example:

```python
import newtutils.console as NewtCons

NewtCons.error_msg(
    "description of the problem",
    location=__file__,
    stop=False
)
```

---

## Global Rules

- For valid input, process all data fully and avoid unnecessary filtering or truncation.
- Raise exceptions for unrecoverable issues.
- Return the most correct and complete result possible, including in recoverable-error cases.
- Stop execution only when data integrity or correctness cannot be guaranteed.
- Do not hide failures silently. Keep errors actionable and easy to trace.

---

## Summary

By following these standards, all NewtCode Python code should be consistent, well-documented, type-safe, and predictable across different environments.
