#!/bin/sh

set -e

echo "Flake8 error count:"
flake8 strivelogger tests --count --show-source --statistics
echo "iSort results:"
isort --check strivelogger --profile black
echo "ok" # won't get here if the previous step fails
isort --check tests
echo "MyPy results:"
mypy strivelogger