```bash
# Helpful software
PS C:\WINDOWS\system32> WinGet install --id Ghisler.TotalCommander
PS C:\WINDOWS\system32> WinGet install --id SublimeHQ.SublimeText.4
PS C:\WINDOWS\system32> WinGet install --id Microsoft.VisualStudioCode
PS C:\WINDOWS\system32> WinGet install --id GitHub.GitHubDesktop
PS C:\WINDOWS\system32> WinGet install --id Git.Git

# Python Manager
PS C:\WINDOWS\system32> WinGet install --id Python.PythonInstallManager

# Updates manager if new version and List of all possible python versions online
PS C:\WINDOWS\system32> py list --online
Python install manager was successfully updated to 26.1.

# Install latest python version
PS C:\WINDOWS\system32> python
Installing Python 3.14.4.
PS C:\WINDOWS\system32> python --version
Python 3.14.4

# Check its location if needed
PS C:\WINDOWS\system32> py -0p
-V:3.14[-64] *   C:\Users\UserName\AppData\Local\Python\pythoncore-3.14-64\python.exe

# Installation of other needed versions
PS C:\WINDOWS\system32> py install 3.13
Installing Python 3.13.13.
PS C:\WINDOWS\system32> py install 3.12
Installing Python 3.12.10.
PS C:\WINDOWS\system32> py install 3.11
Installing Python 3.11.9.
PS C:\WINDOWS\system32> py install 3.10
Installing Python 3.10.11.

# List of all local installed python versions
PS C:\WINDOWS\system32> py list
Tag           Name            Managed By  Version  Alias
3.14[-64]  *  Python 3.14.4   PythonCore  3.14.4   python3[-64].exe, python3.14[-64].exe
3.13[-64]     Python 3.13.13  PythonCore  3.13.13  python3.13[-64].exe
3.12[-64]     Python 3.12.10  PythonCore  3.12.10  python3.12[-64].exe
3.11[-64]     Python 3.11.9   PythonCore  3.11.9   python3.11[-64].exe
3.10[-64]     Python 3.10.11  PythonCore  3.10.11  python3.10.exe

# This shows setting in PATH
PS C:\WINDOWS\system32> where python
PS C:\WINDOWS\system32> where py
# I have it empty

# All other versions not listed here are modifications, tests and in development
PS C:\WINDOWS\system32> py list --online
Tag                            Name                                     Managed By   Version   Alias
3.14[-64]                      Python 3.14.4                            PythonCore   3.14.4    python3.14-64.exe
3.13[-64]                      Python 3.13.13                           PythonCore   3.13.13   python3.13-64.exe
3.12[-64]                      Python 3.12.10                           PythonCore   3.12.10   python3.12-64.exe
3.11[-64]                      Python 3.11.9                            PythonCore   3.11.9    python3.11-64.exe
3.10[-64]                      Python 3.10.11                           PythonCore   3.10.11   python3.10.exe
3.9[-64]                       Python 3.9.13                            PythonCore   3.9.13    python3.9.exe
3.8[-64]                       Python 3.8.10                            PythonCore   3.8.10    python3.8.exe
3.7[-64]                       Python 3.7.9                             PythonCore   3.7.9     python3.7.exe
3.6[-64]                       Python 3.6.8                             PythonCore   3.6.8     python3.6.exe
3.5[-64]                       Python 3.5.4                             PythonCore   3.5.4     python3.5.exe
2.7-32                         Python 2.7.18                            PythonCore   2.7.18    python2.7.exe, python2.exe
2.7[-64]                       Python 2.7.18                            PythonCore   2.7.18

# How to check versions
PS C:\WINDOWS\system32> python --version
Python 3.14.4
PS C:\WINDOWS\system32> py -3.13 --version
Python 3.13.13
PS C:\WINDOWS\system32> py -3.12 --version
Python 3.12.10
PS C:\WINDOWS\system32> py -3.11 --version
Python 3.11.9
PS C:\WINDOWS\system32> py -3.10 --version
Python 3.10.11

# Prepare environments
PS D:\VS_Code> py -3.14 -m venv .venv314
PS D:\VS_Code> py -3.13 -m venv .venv313
PS D:\VS_Code> py -3.12 -m venv .venv312
PS D:\VS_Code> py -3.11 -m venv .venv311
PS D:\VS_Code> py -3.10 -m venv .venv310

# Install packages in each environment
PS D:\VS_Code> python -m pip install requests
PS D:\VS_Code> py -3.13 -m pip install requests
PS D:\VS_Code> py -3.12 -m pip install requests
```
