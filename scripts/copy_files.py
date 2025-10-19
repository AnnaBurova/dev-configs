"""
Created on 2025-10

@author: NewtCode Anna Burova
"""

import sys
import os
import shutil
from typing import List

dir_ = os.path.dirname(os.path.realpath(__file__))

# Add the project root directory to sys.path
sys.path.append(dir_)

# TODO CHECK BEFORE START: put file in location with your repos
# D:\VS_Code
print(dir_)
sys.exit()


def copy_file_to_folders(
        file_paths: List[str],
        destination_folders: List[str]
        ) -> None:
    """
    Copy a list of files into multiple destination folders.

    Args:
        file_paths (List[str]): A list of file paths to copy.
        destination_folders (List[str]): A list of destination folders.

    This function attempts to copy each file from `file_paths`
    into every folder in `destination_folders`. It reports:
      - folders that were missing,
      - folders where copying failed.
    """

    missing_folders = []
    failed_folders = []

    for folder_ in destination_folders:
        if not os.path.exists(folder_):
            missing_folders.append(folder_)
            continue

        for file_ in file_paths:
            try:
                shutil.copy(file_, folder_)

                print(f"Copied {os.path.basename(file_)} → {folder_}")

            except Exception as e_:
                print(f"Failed to copy {os.path.basename(file_)} → {folder_}: {e_}")

                if folder_ not in failed_folders:
                    failed_folders.append(folder_)

    if missing_folders:
        print("\nFolders that did not exist before running the script:")

        for folder_ in missing_folders:
            print(f" - {folder_}")

    if failed_folders:
        print("\nFolders where copying failed:")

        for folder_ in failed_folders:
            print(f" - {folder_}")


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
