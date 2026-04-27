```bash
# Helpful software
$ WinGet install --id Ghisler.TotalCommander
$ WinGet install --id SublimeHQ.SublimeText.4
$ WinGet install --id Microsoft.VisualStudioCode
$ WinGet install --id GitHub.GitHubDesktop
$ WinGet install --id Git.Git

# Python Manager
$ WinGet install --id Python.PythonInstallManager

# Updates manager if new version and List of all possible python versions online
$ py list --online
Python install manager was successfully updated to 26.1.

# Install latest python version
$ python
Installing Python 3.14.4.

$ python --version
Python 3.14.4

# Check its location if needed
$ py -0p
-V:3.14[-64]  *  C:\Users\UserName\AppData\Local\Python\pythoncore-3.14-64\python.exe

# Installation of other needed versions
$ py install 3.13
Installing Python 3.13.13.

$ py install 3.12
Installing Python 3.12.10.

$ py install 3.11
Installing Python 3.11.9.

$ py install 3.10
Installing Python 3.10.11.

# List of all local installed python versions
$ py list
Tag           Name            Managed By  Version  Alias
3.14[-64]  *  Python 3.14.4   PythonCore  3.14.4   python3[-64].exe, python3.14[-64].exe
3.13[-64]     Python 3.13.13  PythonCore  3.13.13  python3.13[-64].exe
3.12[-64]     Python 3.12.10  PythonCore  3.12.10  python3.12[-64].exe
3.11[-64]     Python 3.11.9   PythonCore  3.11.9   python3.11[-64].exe
3.10[-64]     Python 3.10.11  PythonCore  3.10.11  python3.10.exe

# This shows setting in PATH
$ where python
$ where py
# I have it empty

# All other versions not listed here are modifications, tests and in development
$ py list --online
Tag         Name             Managed By   Version   Alias
3.14[-64]   Python 3.14.4    PythonCore   3.14.4    python3.14-64.exe
3.13[-64]   Python 3.13.13   PythonCore   3.13.13   python3.13-64.exe
3.12[-64]   Python 3.12.10   PythonCore   3.12.10   python3.12-64.exe
3.11[-64]   Python 3.11.9    PythonCore   3.11.9    python3.11-64.exe
3.10[-64]   Python 3.10.11   PythonCore   3.10.11   python3.10.exe
3.9[-64]    Python 3.9.13    PythonCore   3.9.13    python3.9.exe
3.8[-64]    Python 3.8.10    PythonCore   3.8.10    python3.8.exe
3.7[-64]    Python 3.7.9     PythonCore   3.7.9     python3.7.exe
3.6[-64]    Python 3.6.8     PythonCore   3.6.8     python3.6.exe
3.5[-64]    Python 3.5.4     PythonCore   3.5.4     python3.5.exe
2.7-32      Python 2.7.18    PythonCore   2.7.18    python2.7.exe, python2.exe
2.7[-64]    Python 2.7.18    PythonCore   2.7.18

# How to check versions
$ python --version
Python 3.14.4

$ py -3.13 --version
Python 3.13.13

$ py -3.12 --version
Python 3.12.10

$ py -3.11 --version
Python 3.11.9

$ py -3.10 --version
Python 3.10.11

# Prepare environments
$ py -3.14 -m venv .venv314
$ py -3.13 -m venv .venv313
$ py -3.12 -m venv .venv312
$ py -3.11 -m venv .venv311
$ py -3.10 -m venv .venv310

# Install packages in each environment
$ python -m pip install requests
$ py -3.13 -m pip install requests
$ py -3.12 -m pip install requests


# Uninstalling all packages from an environment
$ pip list

Package Version
------- -------
pip     26.0.1

$ pip freeze > to_delete.txt

# (Optional but Recommended): Open to_delete.txt and remove core packages like pip, setuptools, or wheel to avoid breaking your environment.
$ pip uninstall -y -r to_delete.txt


# Build project with hatchling
$ cd dev-project
$ pip install build hatchling twine
$ python -m build
Successfully built project-0.1.0.tar.gz and project-0.1.0-py3-none-any.whl

# Look inside files to check content
$ tar -tzf dist/project-0.1.0.tar.gz
$ python -c "import zipfile; z=zipfile.ZipFile('dist/project-0.1.0-py3-none-any.whl'); print('\n'.join(z.namelist()))"
```
