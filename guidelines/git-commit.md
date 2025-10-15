# Commit Guidelines

This document explains how to write clear and consistent commit messages
following the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
Using these guidelines will make your repository easier to read, understand, and maintain.

## Commit Message Structure

A commit message should have the following structure:

```
<type>(<scope>): <short summary>
<BLANK LINE>
<optional longer description>
```

## Commit Types (Conventional Commits)

feat(scope): Add new feature
fix(scope): Fix a bug
chore(scope): Routine task, config update, maintenance
docs(scope): Documentation change
style(scope): Formatting, styling, indentation rules

## Scope examples (optional)

vscode, sublime, git, readme, api

## Summary rules

- Use imperative mood: Add, Fix, Update, Remove
- Capitalize first word
- No period at the end
- Keep it short (~50 chars)

## Examples

feat(vscode): Add settings for auto-format on save
fix(sublime): Correct tab size configuration
chore(git): Update .gitignore for node projects
docs(readme): Add commit message guidelines
style(vscode): Adjust spacing in settings.json
