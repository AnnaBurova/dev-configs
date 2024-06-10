```text
Author: NewtCode Anna Burova
Created: 2024-06
Updated: 2026-11
```

# Installing the NewtCode Package

## Project Structure Overview

```text
new-python/                       # Root repository
│
├── src/
│   └── package_name/             # Main Python package
│       ├── __init__.py           # Defines the package's public import interface
│       ├── __main__.py           # Optional entry point for `python -m package_name`
│       ├── docstring.py          # Example module with a documented function
│       ├── module.py             # Example module with a public function
│       └── (other modules)
│
├── tests/                        # Manual and automated test scripts
│   ├── output/                   # Test output logs
│   │   ├── venv_test_module_1.txt
│   │   ├── venv_test_module_2.txt
│   │   ├── venv_test_module_3.txt
│   │   ├── venv_test_module_4.txt
│   │   └── (other test logs)
│   │
│   ├── README_TESTING.md         # Instructions for running tests across Python versions
│   ├── _run_tests.sh             # (Optional) Test runner script
│   ├── _update_venv.ps1          # (Optional) Updates packages in virtual environments
│   ├── __init__.py               # Marks the tests directory as a package
│   ├── helpers.py                # Helper functions for tests
│   ├── test_module.py            # Tests for the example module
│   ├── test_module_function.py   # Tests for the example function
│   └── (other tests)
│
├── .gitignore                    # Excludes local environments, caches, and build output
├── LICENSE                       # Terms for using and distributing the package
├── CHANGELOG.md                  # Optional record of changes between releases
├── CONTRIBUTING.md               # Optional baseline for project contributions
├── INSTALLATION.md               # Local setup instructions
├── pyproject.toml                # Build configuration and package metadata
├── requirements.txt              # Runtime dependencies for using the package
└── README.md                     # Project overview and first-use instructions
```

## Requirements

NewtCode supports the following Python versions:

- Python 3.15
- Python 3.14
- Python 3.13
- Python 3.12
- Python 3.11

Other dependencies are listed in `requirements.txt`.

**Note:** For distribution as a package, dependencies should also be specified in
`pyproject.toml` under `[project] dependencies`.
The `requirements.txt` file is kept here for local development convenience.

## Installation Mode: Local Installation (No PyPI)

The **NewtCode** project is a local development package and is not published on PyPI.
Installation should be performed directly from the project folder.

---

### Regular Local Installation (Static Copy)

Installs a copy of the package into the active virtual environment.
Recommended when the project is only intended to be used
and its source code does not need to be edited.

```sh
# Activate Virtual Environment

# Navigate to the project directory:
cd ./dev-configs/new-python/

# Install dependencies first (if requirements.txt exists)
python -m pip install -r requirements.txt

# Install the NewtCode package
python -m pip install .
```

---

### Editable Local Installation (Recommended for Development)

To update all configured development virtual environments
and install the optional `test` dependencies defined in `pyproject.toml`,
use the PowerShell helper script:

```pwsh
& '.\dev-configs\new-python\tests\_update_venv.ps1'
```

Recommended when the project is intended to be used and tested.

---

ALTERNATIVELY, install the package in editable mode MANUALLY.

This links the project source folder directly to the Python environment.
Changes made in `src/package_name/` take effect immediately.
No reinstallation is required after each edit.

- `--editable` or `-e` creates a link to the local project
instead of copying its files into the environment.

```sh
# Activate Virtual Environment

# Navigate to the project directory:
cd ./dev-configs/new-python/

# Install dependencies first (if requirements.txt exists)
python -m pip install -r requirements.txt

# Install the NewtCode package in editable mode, including test dependencies
python -m pip install -e ".[test]"
```

---

### Temporary Local Usage (Without Installation)

To run or test functions directly from the downloaded source.
This approach does not install anything globally;
it only extends the Python path for the current session.

```python
# Import required modules
import sys
from pathlib import Path

# Adjust this path to the actual project location
proj_root = Path("D:/") / "VS_Code" / "dev-configs" / "new-python" / "src"

if str(proj_root) not in sys.path:
    sys.path.append(str(proj_root))

import package_name as NewtCode
```

---

### VS Code Settings

To make VS Code recognize the local package:

1. Create or open `.vscode/settings.json` in the VS Code workspace root.

2. Add or extend the following:
    ```jsonc
    {
        "python.analysis.extraPaths": [
            "./dev-configs/new-python/src",
        ],
    }
    ```

    - Adjust the path so that it points to the `src` directory of the project.
    - The path must be relative to the VS Code workspace root.
    - Do not include `package_name` at the end of the path.

3. Reload VS Code (`Ctrl + Shift + P` -> "Developer: Reload Window").

## Uninstalling

To remove the package from the active virtual environment:

```sh
# Check whether the package is installed
python -m pip show package_name

# Uninstall the package
python -m pip uninstall package_name
```

## Usage Examples

After installation, the **NewtCode** package can be imported from anywhere:

```python
# Import the package
import package_name as NewtCode

# Usage examples:
NewtCode.docstring_example(1, "Test")
```
