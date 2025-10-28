# 🐍 NewtCode Documentation Style Guide

This guide defines how to write and maintain consistent **module headers** and **function docstrings**  
for all Python files in the NewtCode project.

All rules are based on the standards defined in:
- `code-style-python.md` — general code and behavior rules
- `docstring.py` — template example of a valid Google-style docstring

## File Header Format

Each Python source file must begin with:

```python
"""
Updated on YYYY-MM
Created on YYYY-MM

@author: NewtCode Anna Burova

Functions:
    def function_name(
        params...
        ) -> return_type
"""
```

### Rules

- `Updated on` is always listed **above** `Created on`.
- All function signatures in the header must **exactly match** the code.
- If constants exist, include them under a `Constants:` section:
  ```python
  Constants:
      CONSTANT_NAME (type):
          Short description.
  ```

## Function Docstring Format

Each function must use the **Google-style** docstring pattern.

Take example from `docstring.py`

## Writing Rules

- Use **English only**.
- Be **precise and technical** — avoid conversational tone.
- Each docstring must describe:
  - the purpose of the function,
  - all parameters and their types,
  - the return value,
  - raised exceptions (if any).
- Use `out` as the return variable placeholder — unless a specific variable name is returned.
- Maintain **4-space indentation** and **1 blank line** between `Args`, `Returns`, and `Raises`.
- Include `Raises:` only if:
  - the function explicitly raises an exception, or
  - calls `NewtCons.error_msg(stop=True)`.

## Consistency Rules

- All modules must share consistent formatting, indentation, and capitalization.
- Reuse terminology across the codebase (e.g., «input data», «output result»).
- Keep docstrings concise — focus on **what** and **why**, not **how**.
- Always verify that the documented arguments and return types match the actual code.

## References

- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide (Docstrings)](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Internal templates:
  - `dev-configs/guidelines/docstring.py`

---

By following this guide, all NewtCode Python modules will maintain clear, professional, and unified documentation standards.
