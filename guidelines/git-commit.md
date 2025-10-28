# 🐍 NewtCode Commit Message Guide

This document defines how to write clear, consistent, and meaningful commit messages  
following the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.  
Using these rules helps maintain clean history and improves code traceability.

## Commit Message Structure

Each commit message follows this format:

```
<type>(<scope>): <short summary>
<BLANK LINE>
<optional longer description>
```

## Commit Types

| Type | Purpose |
| ------ | ---------- |
| **feat** | Add new feature |
| **fix** | Fix a bug |
| **refactor** | Code restructure without behavior change |
| **docs** | Documentation changes only |
| **test** | New or updated tests |
| **chore** | Maintenance, tooling, configs, CI updates |
| **style** | Formatting, naming, whitespace, no logic change |

## Scope Examples

Use a short, lowercase identifier describing the affected area:

```
core, api, readme, git, sublime, vscode, parser
```

## Summary Rules

- Use **imperative mood** — «Add», «Fix», «Update», not «Added» or «Fixes».
- Capitalize the first word.
- Do **not** end the summary with a period.
- Keep the summary around **50 characters**.
- Add an optional body to explain *what* and *why*, not *how*.

## 🧰 Examples

```
feat(api): add pagination support
fix(core): handle missing keys during merge
refactor(parser): simplify token validation logic
docs(readme): update setup instructions
chore(git): update .gitignore for build artifacts
style(vscode): adjust indentation in settings
test(utility): add sorting validation test cases
```

## 💡 Notes

- All commit messages must be written in **English**.
- Avoid vague messages like «fix bug» — be specific about the change.
  when generating commits automatically through AI tools.
