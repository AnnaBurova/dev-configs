# 💡 NewtCode Style Guide

**Environment**

- **OS:** Windows 11
- **Editors:** VS Code / Sublime Text 3
- **Python:** 3.13 (Anaconda: `C:/ProgramData/anaconda3/python.exe`)

---

### General Rules

- Follow **PEP 8** and **PEP 484** (type hints required).
- Avoid all imports from `typing` - use native type hints (`list[str]`, `dict[str, int]`, etc.).
- All comments and docstrings must be written **in English**.
- Use **Google-style docstrings** for all functions, classes, and modules.
- Each file begins with a standard header:

```python
"""
Created on 202Y-MM

@author: NewtCode Anna Burova
"""
```

---

### Input Validation

- All input must be type-checked using explicit validation.
- If argument types or structures are invalid, call `Newt.error_msg()`  
  to display the error **without stopping the program**.

```python
Newt.error_msg("description of the problem",
    location=__file__,
    stop=False)
```

- Data is **never lost** - even on failure, the function must return the most valid possible result.

---

### Sorting Behavior

- When sorting collections:

  - Missing keys always push the item to the **end** of the list.
  - Sorting errors **must not** interrupt program execution.
  - Mixed types (e.g., `str` and `int`) are handled safely and deterministically.

---

### Additional Guidelines

- Functions should be **pure and predictable** - avoid global state or side effects.
- Always prefer readability and reliability over micro-optimization.
- Use consistent newline normalization (`\n`).
- Always include return type annotations.
