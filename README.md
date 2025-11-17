# 🦎 Dev-Config — Chocolate Box by `NewtCode`

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

A collection of configuration files, templates, and scripts for maintaining consistent
Git repository structure, formatting, and behavior across all projects.

---

## 📖 Overview

This repository contains my preferred settings and tools for working with Git and project files.
It provides a unified baseline for code style, text normalization, and automation of common checks,
making repositories clean, predictable, and easy to maintain.

---

## 🧩 Features

| File | Purpose |
|------|----------|
| `.gitignore` | Specifies files and directories that should not be tracked by Git. |
| `.gitattributes` | Ensures consistent text normalization (LF endings), defines diff rules, and marks binary files. |
| `scripts/check_gitattributes.sh` | Bash script that verifies `.gitattributes` consistency across all tracked files. |
| `scripts/copy_files.py` | Python script to copy predefined files to multiple project folders and report missing or failed destinations. |
| `settings/.editorconfig` | Defines indentation, line endings, and encoding rules for all file types to maintain consistent formatting in editors. |
| `settings/Sublime_Text/Preferences.sublime-settings` | Sublime Text editor preferences, e.g., tabs vs spaces, font size, line endings, and other editor behaviors. |
| `settings/VS_Code/settings.json` | VS Code editor settings, such as formatting rules, extensions configuration, and editor behavior. |

---

## ⚙️ Requirements

- **Python 3.10+** (tested with Python 3.10, 3.11, 3.12, 3.13)
- Full type hint support with `from __future__ import annotations`

## 📦 Dependencies

All other modules rely only on the Python Standard Library.

---

## 🚀 Getting Started

- [Installation Guide](INSTALL.md) — setup instructions and configuration details.

---

## 📋 Development Notes

- [TODO list](TODO) — Planned improvements
- [CHANGELOG](CHANGELOG.md) — Version history
- [CONTRIBUTING](CONTRIBUTING.md) — Style and contribution rules

---

## 🪪 License

- [COPYRIGHT](COPYRIGHT) — Copyright information for original and included materials.
- [LICENSE](LICENSE) — The license governing the use of this repository (MIT).
- [AUTHORS](AUTHORS) — List of contributors and credits for external resources.
