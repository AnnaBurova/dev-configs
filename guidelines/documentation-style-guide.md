# 🐍 NewtCode Documentation Style Guide

This guide defines the conventions for writing and maintaining **module headers** and **function docstrings** in all Python files within the NewtCode project.

All rules are based on the standards defined in:

- `code-style-python.md` — general code and behavior rules
- `docstring.py` — internal template that demonstrates a valid Google-style docstring structure

## File Header Format

Each Python source file must begin with the standard module header:

```python
"""
Updated on YYYY-MM
Created on YYYY-MM

@author: NewtCode Anna Burova
"""
```

### Rules

- `Updated on` is always listed **above** `Created on`.
- The header must appear at the very top of the file, before any imports or code.
- Use the same author line format across all modules.

## Optional Module Documentation Sections

If a module-level documentation block is required (for example, in public or shared modules), list exported constants and functions using the following structure:

```python
"""
Constants:
    CONSTANT_NAME (type)

Functions:
    def function_name(
        param1: type,
        param2: type
        ) -> return_type
"""
```

### Rules

- List all constants and functions defined in the module so that the full contents of the module are visible at a glance.
- Function signatures in this documentation block must **exactly match** the actual code (names, parameters, and return type).
- If constants exist, include them under the `Constants:` section; otherwise, omit the section entirely.

## Function Docstring Format

Each function must use the **Google-style** docstring pattern, as illustrated in `docstring.py`.

Treat `docstring.py` as the canonical template: copy its structure and adapt names, descriptions, and types to the specific function.

## Writing Rules

- Use **English only** in all docstrings and headers.
- Be **precise and technical** — avoid conversational tone.
- Each docstring must describe:
  - the purpose of the function,
  - all parameters and their types,
  - the return value and its type,
  - raised exceptions (if any).
- Use `out` as the placeholder name in the `Returns:` section, unless a specific return variable name is important for users of the module.
- Maintain **4-space indentation** and **1 blank line** between docstring sections (`Args`, `Returns`, `Raises`).
- Include a `Raises:` section only if:
  - the function explicitly raises an exception, or
  - the function calls `NewtCons.error_msg(stop=True)`.

## Consistency Rules

- All modules must share consistent formatting, indentation, and capitalization, in line with `code-style-python.md`.
- Reuse terminology across the codebase (for example, use the same phrases for «input data» and «output result» in all related modules).
- Keep docstrings concise — focus on **what** the function does and **why**, not on low-level implementation details.
- Always verify that documented arguments, default values, and return types match the actual code.

## References

- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide — Comments and Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Internal templates:
  - `dev-configs/guidelines/docstring.py`

***

By following this guide, all NewtCode Python modules will maintain clear, professional, and unified documentation standards.
