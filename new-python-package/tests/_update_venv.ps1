#!/usr/bin/env pwsh

<#
Author: NewtCode Anna Burova
Created: 2026-10

Run:
& 'D:\VS_Code\dev-configs\new-python-package\tests\_update_venv.ps1'

Install the project in editable mode with test dependencies in each virtual environment.
#>

# ===================================================================== ======= ===================

# Directory containing virtual environments
$WorkspaceDirectory = "D:\VS_Code"

$Environments = @(
    "venv311"
    "venv312"
    "venv313"
    "venv314"
    "venv315"
)

# --------------------------------------------------------------------- ------- ------------------- --------------------

# Directory containing this script and one level above the tests/ directory.
$ProjectDirectory = Split-Path -Path $PSScriptRoot -Parent
# D:\VS_Code\dev-configs\new-python-package

Set-Location -LiteralPath $ProjectDirectory

Write-Host ""

# --------------------------------------------------------------------- ------- ------------------- --------------------

if (Get-Command deactivate -ErrorAction SilentlyContinue) {

    Write-Host "Deactivating virtual environment..."

    deactivate

    Write-Host ""
}

# --------------------------------------------------------------------- ------- ------------------- --------------------

foreach ($Environment in $Environments) {

    $PythonPath = Join-Path `
        -Path $WorkspaceDirectory `
        -ChildPath ".$Environment\Scripts\python.exe"

    if (-not (Test-Path -LiteralPath $PythonPath -PathType Leaf)) {
        Write-Host "`nSkipping $Environment : python not found"
        continue
    }

    Write-Host "`nInstalling project and test dependencies in $Environment..."

    & $PythonPath -m pip install -e ".[test]"

    if ($LASTEXITCODE -ne 0) {
        throw "Failed to install project in $Environment. Exit code: $LASTEXITCODE"
    }
}

# --------------------------------------------------------------------- ------- ------------------- --------------------

Set-Location -LiteralPath $WorkspaceDirectory

Write-Host ""

# ===================================================================== ======= ===================
