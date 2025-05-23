#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
PROJECT_ROOT=$(dirname "$SCRIPT_DIR")
cd "$PROJECT_ROOT"
echo "Running all unit tests in $PROJECT_ROOT ..."
python -m unittest discover -s tests
