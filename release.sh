#!/bin/bash

if [ "$1" == "" ]; then
    echo "Password is required"
    exit 1
fi

pip install twine
python -m twine upload -u __token__ -p $1 dist/*