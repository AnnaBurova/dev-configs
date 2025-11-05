# 🐍 NewtCode Python Code Style Guide

This document defines the official Python code style, structure, and behavioral conventions used across all NewtCode projects.

Following these standards ensures consistent, reliable, and maintainable code across the entire codebase.

***

## Environment Context

- **Operating system:** Windows 11
- **Editors:** Visual Studio Code, Sublime Text 3
- **Python version:** 3.13 (Anaconda environment)
  - Interpreter path: `C:/ProgramData/anaconda3/python.exe`

## General Rules

- Follow PEP 8 for code style and PEP 484 for type annotations.
- Use native Python type hints and avoid importing collection types from `typing`.
  - *Use `list[str]`, `dict[str, int]`, not `List[str]` or `Dict[str, int]`.*
- All comments and docstrings must be written in English.
- Use Google-style docstrings for all modules, functions, and classes.

## File Header Format

Each Python source file must start with the following header block:

```python
"""
Updated on YYYY-MM
Created on YYYY-MM

@author: NewtCode Anna Burova
"""
```

## Input Validation Rules

- Every input parameter must be explicitly type-checked.
- If the input is invalid:
  - Log an error using:
    ```python
    import newtutils.console as NewtCons

    NewtCons.error_msg(
        "description of the problem",
        location=__file__,
        stop=False
    )
    ```
  - Stop further execution if data integrity cannot be guaranteed.
- If the input is valid:
  - Process all data without loss or unnecessary filtering.
  - The function must return the most correct and complete result possible, even in the presence of recoverable errors.

## Sorting and Collections

When sorting collections or dictionaries:

- Elements with missing keys must be moved to the end of the list.
- Type comparison errors must not interrupt execution.
- Mixed data types must be handled consistently and safely.

## Design Principles

- Functions must be as pure, predictable, and side-effect-free as reasonably possible.
- Prioritize clarity, safety, and reliability over micro-optimizations.
- Normalize all newlines to `\n`.
- Always declare an explicit return type annotation for functions and methods.
- Code must behave identically on both Windows and Linux.

***

By following these standards, all NewtCode Python modules remain stable, maintainable, and consistent across different environments.
