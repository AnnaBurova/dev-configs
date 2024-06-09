# This optional module makes the package runnable with
# python -m package_name
# Remove it if the package does not need a command-line entry point.

from . import greet


def main(
        ) -> None:
    """Run a small example to demonstrate the package."""

    print(greet("Python"))


if __name__ == "__main__":

    main()
