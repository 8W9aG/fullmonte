#!/bin/sh

set -e

echo "Formatting..."
echo "--- Ruff ---"
ruff format fullmonte
echo "--- isort ---"
isort fullmonte

echo "Checking..."
echo "--- Flake8 ---"
flake8 fullmonte
echo "--- pylint ---"
pylint fullmonte
echo "--- mypy ---"
mypy fullmonte
echo "--- Ruff ---"
ruff check fullmonte
echo "--- pyright ---"
pyright fullmonte
