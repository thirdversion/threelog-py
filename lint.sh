#!/bin/sh

set -e

echo "Lint check..."
ruff check threelog --output-format=github
echo "✅"

echo "Format check..."
ruff format threelog --check

echo "Type check..."
pyright threelog
