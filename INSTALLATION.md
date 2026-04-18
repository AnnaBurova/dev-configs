# How to use some Tools

## `./scripts/check_gitattributes.sh`

To check if all files have a corresponding rule in .gitattributes, this script can be used in **bash**:

```sh
missing_attributes=$(git ls-files | git check-attr -a --stdin | grep 'text: auto' || printf '\n')

if [ -n "$missing_attributes" ]; then
  printf '%s\n%s\n' '.gitattributes rule missing for the following files:' "$missing_attributes"
else
  printf '%s\n' 'All files have a corresponding rule in .gitattributes'
fi
```

You can also use the checked-in script which has more features.

```bash
./scripts/check_gitattributes.sh
```
OR
```bash
../dev-configs/scripts/check_gitattributes.sh
```

Run with `--help` for the available options.

Requires Git and Bash.

🔄 **File Normalization**:

```bash
# Re-apply .gitattributes rules to specific file
git add --renormalize <filename>
# Re-apply .gitattributes rules to all files
git add --renormalize .
```

---

## `./scripts/copy_files.py` - Copy Files to Multiple Folders

### Overview

This script is designed to **copy a predefined set of files** to multiple destination folders. It also **reports folders that do not exist** and **folders where copying failed**.

The script is useful for **distributing configuration files or templates** across multiple project directories in a consistent way.

### Requirements

* Standard libraries only: `os`, `sys`, `shutil`

### How It Works

1. **Set the project root directory**:

```python
dir_ = os.path.dirname(os.path.realpath(__file__))
```

The script uses this as a base path for file and folder locations.

2. **Add the root directory to `sys.path`** (optional):

```python
sys.path.append(dir_)
```

This ensures that the script can access modules in the project root if needed.

3. **Define file paths** (`file_paths`):

  * A list of files to copy.
  * Paths are relative to the script directory.

4. **Define destination folders** (`destination_folders`):

  * A list of folders where the files should be copied.
  * If a folder does not exist, it is reported as missing.

5. **Copy files function**: `copy_file_to_folders(file_paths, destination_folders)`

  * Loops through each destination folder.
  * Skips folders that do not exist and logs them.
  * Copies each file to the folder using `shutil.copy()`.
  * Reports folders where copying fails.
  * Prints informative messages including **file names only**, not full paths.

## Notes

* The script **does not create missing folders**; it only reports them.
* File names are displayed without their full paths for clarity.
* Make sure the script is placed in the correct directory relative to your projects before running.
