# -*- coding: utf-8 -*-
"""
Created on 2025-10

@author: NewtCode Anna Burova
"""

import sys
import os
import shutil

dir_ = os.path.dirname(os.path.realpath(__file__))

# Add the project root directory to sys.path
sys.path.append(dir_)

# TODO CHECK BEFORE START: put file in location with your repos
# # D:\VS_Code
# print(dir_)
# sys.exit()


def copy_file_to_folders(file_paths, destination_folders):
    missing_folders = []
    failed_folders = []

    for folder in destination_folders:
        if not os.path.exists(folder):
            missing_folders.append(folder)
            continue

        for file in file_paths:
            try:
                shutil.copy(file, folder)
                print(f"Copied {os.path.basename(file)} to {folder}")
            except Exception as e:
                print(f"Failed to copy {os.path.basename(file)} to {folder}: {e}")
                if folder not in failed_folders:
                    failed_folders.append(folder)

    if missing_folders:
        print("\nFolders that did not exist before running the script:")
        for f in missing_folders:
            print(f" - {f}")

    if failed_folders:
        print("\nFolders where copying failed:")
        for f in failed_folders:
            print(f" - {f}")


file_paths = [
    os.path.join(dir_, "dev-configs", ".gitignore"),
    os.path.join(dir_, "dev-configs", ".gitattributes"),
    os.path.join(dir_, "dev-configs", "new-repo", "AUTHORS"),
    os.path.join(dir_, "dev-configs", "new-repo", "CHANGELOG"),
    os.path.join(dir_, "dev-configs", "new-repo", "CONTRIBUTING"),
    os.path.join(dir_, "dev-configs", "new-repo", "COPYRIGHT"),
    os.path.join(dir_, "dev-configs", "new-repo", "INSTALL.md"),
    os.path.join(dir_, "dev-configs", "new-repo", "LICENSE"),
    os.path.join(dir_, "dev-configs", "new-repo", "README.md"),
    os.path.join(dir_, "dev-configs", "new-repo", "TODO"),
    ]
destination_folders = [
    os.path.join(dir_, "dev-newtutils"),
    os.path.join(dir_, "dev-tools"),
    ]

copy_file_to_folders(file_paths, destination_folders)
