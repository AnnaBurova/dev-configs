#!/usr/bin/env pwsh

<#
Author: NewtCode Anna Burova
Created: 2026-10

Run:
& 'D:\VS_Code\dev-configs\new-python-package\tests\_run_tests.ps1'

Run selected test modules in configured virtual environments across four pytest modes.
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

$Modules = @(
    "module"
)

# --------------------------------------------------------------------- ------- ------------------- --------------------

Set-Location -LiteralPath $PSScriptRoot
# D:\VS_Code\dev-configs\new-python-package\tests

# Ensure output directory exists
$OutputDirectory = Join-Path -Path $PSScriptRoot -ChildPath "output"
if (-not (Test-Path -LiteralPath $OutputDirectory -PathType Container)) {
    New-Item -ItemType Directory -Path $OutputDirectory | Out-Null
}

# UTF-8 encoding without BOM (for consistent LF output files)
$Utf8NoBom = [System.Text.UTF8Encoding]::new($false)

# Ensure PowerShell reads external process output and Python writes it in UTF-8
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONUTF8 = "1"

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

    $PytestPath = Join-Path `
        -Path $WorkspaceDirectory `
        -ChildPath ".$Environment\Scripts\pytest.exe"

    # Skip environment if pytest executable is not found
    if (-not (Test-Path -LiteralPath $PytestPath -PathType Leaf)) {
        Write-Host "`nSkipping $Environment : pytest not found"
        continue
    }

    # ----------------------------------------------------------------- ------- ------------------- --------------------

    foreach ($Module in $Modules) {

        $TestFile = "test_${Module}.py"

        foreach ($Mode in 1..4) {

            Write-Host "tests/${TestFile}: mode $Mode, environment $Environment"

            $PytestArgs = switch ($Mode) {
                1 { @("-m", "pytest", $TestFile) }
                2 { @("-m", "pytest", "-vv", $TestFile) }
                3 { @("-m", "pytest", "-s", $TestFile) }
                4 { @("-m", "pytest", "-s", "-vv", $TestFile) }
            }

            # Run pytest and capture both stdout and stderr
            $RawLines = & $PythonPath $PytestArgs 2>&1 | ForEach-Object { $_.ToString() }

            # Strip execution time from summary line
            $ProcessedLines = $RawLines | ForEach-Object {
                $_ -replace '(passed|ran) in [0-9.]+s( ={10,})$', '$1$2'
            }

            # Join with LF (`n) and write as UTF-8 without BOM (equivalent to dos2unix)
            $Content = ($ProcessedLines -join "`n") + "`n"
            $OutputFile = Join-Path -Path $OutputDirectory -ChildPath "test_${Mode}_${Module}_${Environment}.txt"
            [System.IO.File]::WriteAllText($OutputFile, $Content, $Utf8NoBom)
        }
    }
}

# --------------------------------------------------------------------- ------- ------------------- --------------------

Set-Location -LiteralPath $WorkspaceDirectory

Write-Host ""

# ===================================================================== ======= ===================
