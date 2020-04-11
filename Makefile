SHELL :=/bin/bash
CWD := $(PWD)
TMP_PATH := $(CWD)/.tmp
VENV_PATH := $(CWD)/.venv

.PHONY: test clean

clean:
	@rm -rf $(TMP_PATH) __pycache__ .pytest_cache
	@find . -name '*.pyc' -delete

setup:
	@pip install -U -e .[dev]
	@npm install -g pyright

venv_test:
	@pytest -vvv

format:
	@black .

check:
	@black --check --diff .
	@pyright
