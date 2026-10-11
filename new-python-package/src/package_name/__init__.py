# Copyright (c) 2026 Anna Burova
"""Package public API and metadata.

Author: NewtCode Anna Burova
Created: 2026-10
"""

# ===== Imports from modules ========================================== =======

# Re-export the most useful functions so callers can import them directly

from .docstring import docstring_example
from .functions import (
    count_words,
    greet,
)

# Usage: from package_name import greet, count_words, docstring_example

# ===== Metadata ====================================================== =======

# Names listed here define the package's intended public API.
__all__ = [
    "count_words",  # ----- functions
    "docstring_example",  # ----- docstring
    "greet",  # ----- functions
]

# ===== Project ======================================================= =======

# Update this value when the project version in pyproject.toml changes.
__version__ = "0.1.0"
__author__ = "Anna Burova"
__email__ = "burova.anna+git@gmail.com"
__description__ = "Development configuration utilities"
__license__ = "MIT"
__url__ = "https://github.com/AnnaBurova/dev-configs/tree/main/new-python-package"
