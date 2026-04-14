"""
Updated on YYYY-MM
Created on YYYY-MM

@author: NewtCode Anna Burova

Copyright (c) YYYY Anna Burova
All Rights Reserved
"""

from __future__ import annotations

import sys
import os

import newtutils.console as NewtCons
import newtutils.utility as NewtUtil
import newtutils.files as NewtFiles
import newtutils.sql as NewtSQL
import newtutils.network as NewtNet

DIR_PROJECT = os.path.dirname(os.path.realpath(__file__))
# print(DIR_PROJECT)

DIR_GLOBAL = os.path.dirname(os.path.dirname(os.path.dirname(DIR_PROJECT)))
# print(DIR_GLOBAL)

# Add the project root directory to sys.path
sys.path.append(DIR_GLOBAL)

# TODO: change the path as needed
MUST_LOCATION = os.path.join("D:\\", "VS_Code")


# TODO: add your functions here
# Examples in docstring.py
# code-style-python.md can be used as references for structure, style, and documentation.


if __name__ == "__main__":
    NewtCons.check_location(DIR_GLOBAL, MUST_LOCATION)
    # TODO: add your function calls here

    print("=== END ===")
