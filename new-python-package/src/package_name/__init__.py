"""
Author: NewtCode Anna Burova
Created: 2026-10
"""

# ===== Imports from modules ========================================== =======

# ----- docstring ----------------------------------------------------- ------- ------------------- --------------------
# Re-export the most useful functions so callers can import them directly:
from .docstring import count_words, docstring_example

# ----- module -------------------------------------------------------- ------- ------------------- --------------------
from .module import (
    greet,
)

# Example:
# from package_name import greet, count_words

# ===== Metadata ====================================================== =======

# Names listed here define the package's intended public API.
__all__ = [
    # ----- docstring ------------------------------------------------- ------- ------------------- --------------------
    "count_words",
    "docstring_example",

    # ----- module ---------------------------------------------------- ------- ------------------- --------------------
    "greet",
]

# ===== Project ======================================================= =======

# Update this value when the project version in pyproject.toml changes.
__version__ = "0.1.0"
__author__ = "Anna Burova"
__email__ = "burova.anna+git@gmail.com"
__description__ = "Development configuration utilities"
__license__ = "MIT"
__url__ = "https://github.com/AnnaBurova/dev-configs/tree/main/new-python-package"
