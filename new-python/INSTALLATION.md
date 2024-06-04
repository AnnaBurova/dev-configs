# Installing *XXX* Module (NewtCode)

## Project Structure

```
dev-library/              # Root repository
│
├── src/
│   └── library/          # Main Python package (module source)
│       ├── __init__.py
│       ├── docstring.py
│       ├── module.py
│       └── (other files)
│
├── tests/                # Manual and automated test scripts
│   ├── output/           # Test output logs
│   │   ├── venv_test_module_1.txt
│   │   ├── venv_test_module_2.txt
│   │   ├── venv_test_module_3.txt
│   │   ├── venv_test_module_4.txt
│   │   └── (other test logs)
│   │
│   ├── TESTING.md        # Test documentation and instructions
│   ├── _update_venv.ps1  # (Optional) Updates packages in virtual environments
│   ├── _run_tests.sh     # (Optional) Test runner batch script
│   ├── __init__.py       # Marks tests as a package
│   ├── helpers.py        # Helper functions for tests
│   ├── test_docstring.py
│   ├── test_module.py
│   ├── test_*.py      # Pytest test scripts for modules
│   ├── test_*_*.py    # Pytest test scripts for functions
│   └── (other test scripts)
│
├── CHANGELOG.md          # Version history and release notes
├── CONTRIBUTING.md       # Guidelines for contributors
├── INSTALLATION.md       # Installation and development setup guide (current file)
├── LICENSE               # License file
├── pyproject.toml        # Build system configuration and project metadata
├── requirements.txt      # Project dependencies
└── README.md             # Project overview and usage instructions
```

## Requirements

XXX supports the following Python versions:

- Python 3.14
- Python 3.13
- Python 3.12
- Python 3.11
- Python 3.10

Other dependencies are listed in `requirements.txt`.

**Note:** For library distribution, dependencies should also be specified in
`pyproject.toml` under `[project] dependencies`.
The `requirements.txt` file is kept here for local development convenience.

## Installation Mode: Local Installation (No PyPI)

Project **XXX** is a local development library and is not published on PyPI.
Installation should be done directly from the project folder.

### Regular Local Installation (Static Copy)

Install a copy of the package.
Recommended when you only want to use the project, not actively edit its source code.
Safe for non-admin users.

- `--user` installs into the user's personal environment.

```bash
# Navigate to the project directory
$ cd dev-library/

# Install dependencies first (if requirements.txt exists)
$ python -m pip install --user -r requirements.txt

# Install the package for the current user
$ python -m pip install --user .
# OR in a virtual environment (venv)
$ python -m pip install .
```

### Editable Local Installation (Recommended for Development)

To update all configured development virtual environments
and install the test dependencies from the test group,
use the PowerShell helper script:

```bash
$ ./dev-library/tests/_update_venv.ps1
```

Recommended when you want to use and test the project.

Alternatively, install the package in editable mode manually.

This links the project source folder directly to the Python environment.
Changes made in `dev-library/src/library/` take effect immediately.
No reinstallation is required after each edit.

- `--editable` or `-e` creates a link to the local project
instead of copying its files into the environment.

```bash
# Navigate to the project directory
$ cd dev-library/

# Install dependencies first (if requirements.txt exists)
$ python -m pip install --user -r requirements.txt

# Install the package in editable mode for the current user
$ python -m pip install --user -e .
# OR in a virtual environment (venv)
$ python -m pip install -e .
```

### Temporary Local Usage (Without Installation)

To run or test functions directly from the downloaded source.
This approach doesn't install anything globally;
it only extends the Python path for the current session.

```python
# Import required modules
import sys
import os
from pathlib import Path

# Adjust this path to the actual project location
proj_root = os.path.join("D:\\", "VS_Code", "dev-library", "src")
# Or use one of these formats:
proj_root = Path("D:/") / "VS_Code" / "dev-library" / "src"
proj_root = "D:/VS_Code/dev-library/src"
proj_root = r"D:\VS_Code\dev-library\src"

if str(proj_root) not in sys.path:
    sys.path.append(str(proj_root))

import library as Lib
```

### VS Code Settings

To make VS Code recognize the local package:

1. Create or open `.vscode/settings.json`.

2. Add or extend the following:
    ```json
    {
        "python.analysis.extraPaths": [
            "./dev-library/src",
        ]
    }
    ```

    - Adjust the path above to match the actual project location.

3. Reload VS Code (`Ctrl + Shift + P` -> "Developer: Reload Window").

## Uninstalling

To remove the package completely:

```bash
# Check if the package is installed and see its location
# Note: On Windows, `findstr` requires Command Prompt
$ python -m pip list | findstr library
# On PowerShell, use:
$ python -m pip list | Select-String library

# Uninstall the package
# admin rights required only if installed system-wide without --user
$ python -m pip uninstall library
```

## Usage Examples

After installation, **XXX** can be imported from anywhere:

```python
# Import the package
import library as Lib

# Usage examples:
Lib.docstring_example(1, "Test")
```
