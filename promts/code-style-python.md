# NewtCode Developer Prompt

This prompt defines the **style, conventions, and behavioral rules** for all source code, documentation, and responses produced in the **NewtCode** project.

---

## Environment Context

* **Operating System:** Windows 11
* **Editors:** Visual Studio Code, Sublime Text 3
* **Python version:** 3.13 (Anaconda environment)
  * Interpreter path: `C:/ProgramData/anaconda3/python.exe`

---

## General Coding Rules

* Follow **PEP 8** for style and **PEP 484** for type annotations.
* Avoid all imports from the `typing` module — use **native type hints** instead (`list[str]`, `dict[str, int]`, etc.).
* All **comments** and **docstrings** must be written in **English**.
* Use **Google-style docstrings** for all functions, classes, and modules.
* Every source file begins with a header block:

```python
"""
Created on 202Y-MM

@author: NewtCode Anna Burova
"""
```

---

## Input Validation

* Every input parameter must be **explicitly type-checked**.
* When invalid data or arguments are detected, the function must **not raise an exception** directly.
  Instead, call:

```python
Newt.error_msg(
    "description of the problem",
    location=__file__,
    stop=False)
```

* The function must attempt to return the **most valid possible result** even in the presence of errors — **no data loss** under any circumstances.

---

## Sorting and Collection Behavior

When sorting collections or dictionaries:

* Missing keys must always move the item to the **end** of the result list.
* Type comparison errors **must not interrupt execution**.
* Mixed types (e.g., `str` vs. `int`) must be handled deterministically and consistently.

---

## Additional Design Principles

* Functions should be **pure and predictable** — avoid hidden state and global side effects.
* Prioritize **clarity, reliability, and determinism** over micro-optimization.
* Normalize newlines across all outputs as `\n`.
* Every function must explicitly declare a **return type annotation**.
* Ensure all code and tests behave **consistently across platforms** (especially Windows and Linux).
