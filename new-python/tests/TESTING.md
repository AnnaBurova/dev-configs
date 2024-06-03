# Testing

This directory contains comprehensive unit tests for the **XXX** package.

## Test Files

- test_docstring.py
- test_module.py

## Requirements

- pytest
- pytest-cov

```bash
# Install packages:
$ pip install pytest
$ pip install pytest-cov
```

## Test Coverage

### What is coverage?

**Code coverage** measures how much of your source code is executed by tests.
It shows:

- Which lines of code were run during tests
- Which functions were called
- Which branches (if/else) were tested
- Overall percentage of code covered

### Usage

```bash
# Navigate to the project directory:
$ cd dev-library/

# Run all tests with code coverage analysis:
$ pytest tests/ --cov=library --cov-report=html
# OR Run a specific test file with code coverage analysis:
$ pytest tests/test_console.py --cov=library --cov-report=html
```

This generates an `htmlcov/` folder containing the coverage report.
Open `htmlcov/index.html` in your browser to see a detailed coverage report
with highlighted lines (green = covered, red = not covered).

```bash
$ start htmlcov/index.html
```

## Running Tests Using PyTest

```bash
# Navigate to the project directory:
$ cd dev-library/

# Run all tests:
$ pytest tests/
# OR Run a specific test file:
$ pytest tests/test_console.py
```

OR

```bash
# Navigate to the tests directory:
$ cd dev-library/tests/
# Run all tests:
$ pytest .
# OR Run a specific test file:
$ pytest ./test_console.py
```

Run with verbose output:

```bash
$ pytest tests/
$ pytest tests/ -v
$ pytest tests/ -s
$ pytest tests/ -s -v
$ pytest tests/ -s -v > test_results.txt 2>&1
```

## Notes

- All tests are designed to be independent and can run in any order.
- File tests use temporary files and directories.
- SQL tests create temporary databases that are cleaned up after tests.
- Network tests use mocked HTTP requests to avoid actual network calls.
