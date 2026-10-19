"""A tiny command-line greeting program."""

import sys


def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"


def main() -> None:
    """Print a greeting for the first command-line argument."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))


def test_greet() -> None:
    """Check the expected greeting."""
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    main()
