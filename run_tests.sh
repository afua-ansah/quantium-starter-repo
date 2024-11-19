#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the virtual environment path
VENV_PATH="./quantium" 

# Activate the project virtual environment
if [ -d "$VENV_PATH" ]; then
    echo "Activating virtual environment..."
    source "$VENV_PATH/bin/activate"
else
    echo "Virtual environment not found at $VENV_PATH"
    exit 1
fi

# Run the test suite with pytest
echo "Running test suite..."
pytest

# Capture the exit status of pytest
TEST_EXIT_CODE=$?

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

# Exit with the appropriate status
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
