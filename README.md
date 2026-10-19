# greet-ci

A small Python greeting program with GitHub Actions CI.

## Requirements

- Python 3.11 or later
- [uv](https://docs.astral.sh/uv/)

## Run

From the repository root:

```sh
uv run --locked python greet.py Hee
uv run --locked python greet.py
```

The first command prints `Hello, Hee!`; the second prints `Hello, world!`.

## Check and build

```sh
uv run --locked pytest -q greet.py
uv run --locked black --check greet.py
uv run --locked flake8 greet.py
uv run --locked mypy greet.py
uv build
```
