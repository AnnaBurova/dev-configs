# 🧭 Git Daily Workflow Mini-Guide

## 📦 Basic Commands

```bash
# Add specific file to staging
git add <filename>

# Add all modified files to staging
git add .

# Commit with a message
git commit -m "Message"

# View unstaged changes
git diff

# Summary of changed files only
git diff --summary
```

```bash
# Unstage all files (remove from staging area)
git reset
```

✅  **Tip**: Useful when you accidentally staged too many files.

---

## 🕒 Commit Date Management

```bash
# Set a custom date for the commit
git commit --date="2025-04-10 14:00:00" -m "Message"
```

---

## ✏️ Amending the Last Commit

```bash
git commit --amend --no-edit --date="2025-05-24T00:39:50"
```

* `--amend` — rewrite the **last commit**
* `--no-edit` — keep the same commit message
* `--date` — manually set commit date and author timestamp

### Date Format

```
YYYY-MM-DDTHH:MM:SS
# The letter 'T' is required between date and time
```

---

## 🪶 Empty Commits

```bash
git commit --allow-empty -m "Message" --date="2025-04-10T18:35:09"
```

* `--allow-empty` — allows committing **without any file changes**

✅  Useful for **triggering CI/CD pipelines** or **adding historical notes**

### Date Format

```
YYYY-MM-DDTHH:MM:SS
# The letter 'T' is required between date and time
```

---

## 📜 Log & History

```bash
# Compact log view
git log --oneline

# Export log summary to a file
git log --oneline > history.txt

# Detailed custom log format
git log --pretty=format:"%h %ad | %an | %s" --date=short > history.txt
```

---

## 🔄 File Normalization

```bash
# Re-apply .gitattributes rules to specific file
git add --renormalize <filename>
# Re-apply .gitattributes rules to all files
git add --renormalize .
```

✅  Keeps line endings and binary file handling consistent across systems.

---

## 🌿 Branching

```bash
# Create and switch to a new branch
git checkout -b feature/new-ui

# Switch to an existing branch
git checkout main

# Merge a branch into the current one
git merge feature/new-ui

# Delete a branch (after merge)
git branch -d feature/new-ui
```

### Recommended Branch Prefixes

| Type          | Prefix   | Example              |
| ------------- | -------- | -------------------- |
| Feature       | `feat/`  | `feat/add-login`     |
| Bug fix       | `fix/`   | `fix/api-timeout`    |
| Documentation | `docs/`  | `docs/update-readme` |
| Maintenance   | `chore/` | `chore/update-deps`  |
| Tests         | `test/`  | `test/unit-helpers`  |

---

## 🌍 Remote Management

```bash
# Clone a remote repository
git clone https://github.com/user/repo.git

# Show remotes
git remote -v

# Add a new remote
git remote add origin https://github.com/user/repo.git

# Rename remote
git remote rename origin upstream
```

### Fetching and Pulling

```bash
# Fetch new branches and updates (no merge)
git fetch

# Fetch and rebase (recommended for teams)
git pull --rebase

# Merge changes directly (less clean history)
git pull
```

### Pushing Changes

```bash
# Push the current branch
git push

# Push a specific branch
git push origin feature/new-ui

# Force push (use with care)
git push --force-with-lease
```

✅ Use `--force-with-lease` instead of `--force` — it’s safer and won’t overwrite teammates’ work.
* When you push with `--force`, Git replaces the branch on the remote server with your local branch — no matter what’s there.
* When you push with `--force-with-lease`, Git first checks whether the remote branch still points to the same commit you last fetched (the one your local copy is based on).
  * If no one else has pushed, your push proceeds (safe).
  * If someone else pushed new commits, Git refuses to push and warns you.

---

## 🔧 Rebasing & History Cleanup

```bash
# Rebase your branch with main (update history cleanly)
git fetch origin
git rebase origin/main

# Interactive rebase for cleanup
git rebase -i HEAD~5
```

* Combine, edit, or delete commits before merging
* Keep your history clean and readable

---

## 🧩 Tags and Releases

```bash
# Create a lightweight tag
git tag v1.0.0

# Annotated tag (recommended)
git tag -a v1.0.0 -m "First release"

# Push all tags to remote
git push --tags
```

---

## ⚙️ Useful Tips

* Run `git status` often — it’s your best friend for tracking changes.
* Commit small and often — one logical change per commit
* Use rebasing for local cleanup, merging for published branches
* Keep main (or master) always stable and deployable
* Write clear, conventional commit messages
* Always pull before pushing:

```bash
git pull --rebase
git push
```
