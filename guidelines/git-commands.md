```bash
# Basic Commands
git status               # Show working tree status
git add <filename>       # Add specific file to staging
git add .                # Add all modified files to staging
git commit -m "Message"  # Commit with a message
git diff                 # View unstaged changes
git diff --summary       # Summary of changed files only
git diff --staged        # View staged changes
git diff --staged > changes.patch  # Compare staged changes and save to patch file
git diff v1.0.0 v1.1.1 > changes.patch  # Compare two tags and save to patch file


# Stash Workflow
# Use stash when you need to temporarily save unfinished work.
git stash                    # Stash unstaged changes (keep untracked files)
git stash -u                 # Stash all changes including untracked files
git stash push -m "Message"  # Stash with a message for easier identification
git stash list               # List all stashed changes
git stash show -p            # Show details of the most recent stash
git stash pop                # Apply the most recent stash and remove it from the stash list
git stash apply              # Apply the most recent stash without removing it from the stash list
git stash drop               # Remove the most recent stash without applying it
git stash clear              # Remove all stashes


# Reset and Restore
git reset                       # Unstage all files (remove from staging area)
git reset <filename>            # Unstage a file (keep changes in working directory)
git reset --soft HEAD~1         # Undo last commit, keep staged changes
git reset --mixed HEAD~1        # Undo last commit, keep changes unstaged
git reset --hard HEAD~1         # Undo last commit and discard changes
# Use  git reset --hard  only when you are sure you want to lose local changes.
git restore                     # Discard changes in working directory
git restore <filename>          # Discard local changes in a file
git restore --staged <filename> # Unstage a file (keep changes in working directory)


# Date Management
git commit --date="2026-01-30 14:00:00" -m "Message"                # Set a custom date for the commit
git commit --allow-empty -m "Message" --date="2026-01-30T14:00:00"  # Empty Commits
git commit --amend --no-edit --date="2026-01-30T14:00:00"           # Amending the Last Commit

GIT_AUTHOR_DATE="2026-01-30T14:00:00" \
GIT_COMMITTER_DATE="2026-01-30T14:00:00" \
git commit --amend --no-edit --date="2026-01-30T14:00:00"

# GIT_AUTHOR_DATE and GIT_COMMITTER_DATE set the actual timestamps
# --amend                # rewrite the last commit
# --no-edit              # keep the same commit message
# --date                 # manually set commit date and author timestamp
# "YYYY-MM-DDTHH:MM:SS"  # The letter 'T' is required between date and time
# --allow-empty          # allows committing without any file changes


# Log and History
git log --oneline                           # Compact log view
git log --oneline > history.txt             # Export log summary to a file
git log --graph --oneline --decorate --all  # Visualize branch structure and commits

git log --pretty=format:"%h %ad | %an | %s" --date=short > history.txt  # Detailed custom log format

git log --pretty=format:"%h%nAuthor: %an%nDate: %ad%nMessage: %s%n" --date=iso
# 332902e
# Author: Anna Burova
# Date: 2026-01-30 14:00:00 +0300
# Message: chore(version): bump project version to 0.1.4

git log --pretty=format:"%h %s%n  Author date: %ad%n  Commit date: %cd" --date=iso
# 160dab8 Initial commit
#   Author date: 2026-01-30 14:00:00 +0300
#   Commit date: 2026-01-30 14:00:00 +0300

git show <commit>  # Show details of a specific commit
git blame <file>   # Show line-by-line history of a file


# File Normalization
# Use this after changing .gitattributes or line-ending rules.
git add --renormalize <filename>  # Re-apply .gitattributes rules to specific file
git add --renormalize .           # Re-apply .gitattributes rules to all files


# Branching
git branch                      # List local branches
git branch -a                   # List all branches
git switch -c feature/new-ui    # Create and switch to a branch
git switch main                 # Switch to main branch
git checkout -b feature/new-ui  # Create and switch to a new branch
git checkout main               # Switch to an existing branch
git merge feature/new-ui        # Merge a branch into the current one
git merge origin/main           # Merge the latest changes from main into the current branch
git branch -d feature/new-ui    # Delete a branch (after merge)
git branch -D feature/new-ui    # Force delete branch


# Remote Management
git clone https://github.com/user/repo.git              # Clone a remote repository
git remote -v                                           # Show remotes
git remote add origin https://github.com/user/repo.git  # Add a new remote
git remote rename origin upstream                       # Rename remote


# Fetching and Pulling
git fetch          # Fetch new branches and updates (no merge)
git pull --rebase  # Fetch and rebase (recommended for teams)
git pull           # Merge changes directly (less clean history)


# Pushing Changes
git push                        # Push the current branch
git push origin feature/new-ui  # Push a specific branch
git push --force-with-lease     # Force push (wont overwrite teammates work)
git push --force                # Force push (overwrite teammates work)

# If push with --force,
#   Git replaces the branch on the remote server with local branch — no matter what's there.
# If push with --force-with-lease,
#   Git first checks whether the remote branch still points to the same commit last local fetched.
#   If no one else has pushed, this push proceeds (safe).
#   If someone else pushed new commits, Git refuses to push and gives warning.


# Rebasing and History Cleanup
# Combine, edit, or delete commits before merging

# Rebase your branch with main (update history cleanly)
git fetch origin
git rebase origin/main

# Interactive rebase for cleanup
git rebase -i HEAD~5   # Edit last 5 commits
git rebase --continue  # Continue after resolving conflicts
git rebase --abort     # Abort rebase and return to original state


# Tags and Releases

git tag                               # List all local tags
git tag -n                            # List all local tags with annotation
git ls-remote --tags origin           # List all remote tags

git tag --sort=v:refname -n           # List tags sorted by version number with annotation
git config --global tag.sort version:refname  # Set default tag sorting to version number (once per repository or globally)

git tag v1.0.0                        # Create lightweight tag
git tag -a v1.0.0 -m "First release"  # Create annotated tag (recommended)
git tag -a v1.0.0 332902e -m "v1.0.0 — First release"  # Tag specific commit
git tag -d v1.0.0                     # Delete local tag

git show v1.0.0                       # Show tag details
git push --tags                       # Push all tags to remote
git push origin --force --tags        # Force push tags (use with caution)
git push origin v1.0.0                # Push specific tag to remote
git fetch --tags                      # Fetch all tags from remote
git checkout v1.0.0                   # Checkout to tagged version
```
