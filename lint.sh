#!/bin/sh

set -e

echo "Lint check..."
ruff check strivelogger --show-source --output-format=github
echo "✅"

echo "Format check..."
black strivelogger --check

echo "Type check..."
pyright strivelogger
