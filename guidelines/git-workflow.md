# 🧭 Git Commands Mini-Guide

## 📦 Basic Commands

```bash
git add <filename>       # Add specific file to staging
git add .                # Add all modified files to staging
git commit -m "Message"  # Commit with a message
git diff                 # View unstaged changes
git diff --summary       # Summary of changed files only
git reset                # Unstage all files (remove from staging area)
```

## 🕒 Commit Date Management

```bash
git commit --date="2025-04-10 14:00:00" -m "Message"                # Set a custom date for the commit
git commit --allow-empty -m "Message" --date="2025-04-10T18:35:09"  # Empty Commits
git commit --amend --no-edit --date="2025-05-24T00:39:50"           # Amending the Last Commit

GIT_AUTHOR_DATE="2025-10-22T00:36:00" \
GIT_COMMITTER_DATE="2025-10-22T00:36:00" \
git commit --amend --no-edit --date="2025-10-22T00:36:00"
```

- `--amend` - rewrite the **last commit**
- `--no-edit` - keep the same commit message
- `--date` - manually set commit date and author timestamp
- `"YYYY-MM-DDTHH:MM:SS"` - The letter 'T' is required between date and time
- `--allow-empty` - allows committing **without any file changes**

## 📜 Log & History

```bash
git log --oneline                                                       # Compact log view
git log --oneline > history.txt                                         # Export log summary to a file
git log --pretty=format:"%h %ad | %an | %s" --date=short > history.txt  # Detailed custom log format

git log --pretty=format:"%h%nAuthor: %an%nDate: %ad%nMessage: %s%n" --date=iso
# 332902e
# Author: Anna Burova
# Date: 2025-10-21 12:40:13 +0300
# Message: chore(version): bump project version to 0.1.4

git log --pretty=format:"%h %s%n  Author date: %ad%n  Commit date: %cd" --date=iso
# 160dab8 Initial commit
#   Author date: 2025-10-15 11:48:35 +0300
#   Commit date: 2025-10-15 11:48:35 +0300
```

## 🔄 File Normalization

```bash
git add --renormalize <filename>  # Re-apply .gitattributes rules to specific file
git add --renormalize .           # Re-apply .gitattributes rules to all files
```

## 🌿 Branching

```bash
git checkout -b feature/new-ui  # Create and switch to a new branch
git checkout master             # Switch to an existing branch
git merge feature/new-ui        # Merge a branch into the current one
git branch -d feature/new-ui    # Delete a branch (after merge)
```

### Recommended Branch Prefixes

| Type          | Prefix   | Example              |
| ------------- | -------- | -------------------- |
| Feature       | `feat/`  | `feat/add-login`     |
| Bug fix       | `fix/`   | `fix/api-timeout`    |
| Documentation | `docs/`  | `docs/update-readme` |
| Maintenance   | `chore/` | `chore/update-deps`  |
| Tests         | `test/`  | `test/unit-helpers`  |

## 🌍 Remote Management

```bash
git clone https://github.com/user/repo.git              # Clone a remote repository
git remote -v                                           # Show remotes
git remote add origin https://github.com/user/repo.git  # Add a new remote
git remote rename origin upstream                       # Rename remote
```

### Fetching and Pulling

```bash
git fetch          # Fetch new branches and updates (no merge)
git pull --rebase  # Fetch and rebase (recommended for teams)
git pull           # Merge changes directly (less clean history)
```

### Pushing Changes

```bash
git push                        # Push the current branch
git push origin feature/new-ui  # Push a specific branch
git push --force-with-lease     # Force push (wont overwrite teammates work)
git push --force               # Force push (overwrite teammates work)
```

- When you push with `--force`,
  Git replaces the branch on the remote server with your local branch — no matter what’s there.
- When you push with `--force-with-lease`,
  Git first checks whether the remote branch still points to the same commit you last fetched
  (the one your local copy is based on).
  - If no one else has pushed, your push proceeds (safe).
  - If someone else pushed new commits, Git refuses to push and warns you.

## 🔧 Rebasing & History Cleanup

```bash
# Rebase your branch with main (update history cleanly)
git fetch origin
git rebase origin/main

# Interactive rebase for cleanup
git rebase -i HEAD~5
```

- Combine, edit, or delete commits before merging
- Keep your history clean and readable

## 🧩 Tags and Releases

```bash
git tag                               # List all local tags
git tag -n                            # List all local tags with annotation
git ls-remote --tags origin           # List all remote tags

git tag v1.0.0                        # Create lightweight tag
git tag -a v1.0.0 -m "First release"  # Create annotated tag (recommended)
git tag -a v1.0.0 332902e -m "v1.0.0 — First release"  # Tag specific commit

git tag -d v1.0.0                     # Delete local tag
git show v1.0.0                       # Show tag details
git push --tags                       # Push all tags to remote
git push origin --force --tags
git fetch --tags                      # Fetch all tags from remote
git checkout v1.0.0                   # Checkout to tagged version
```
