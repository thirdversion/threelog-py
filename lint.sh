#!/bin/sh

set -e

echo "Flake8 error count:"
flake8 app tests --count --show-source --statistics
echo "iSort results:"
isort --check app --profile black
echo "ok" # won't get here if the previous step fails
isort --check tests
echo "MyPy results:"
mypy app