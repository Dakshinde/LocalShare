#!/bin/bash
# This is the Mac/Linux launcher for LocalShare

# Check if a folder path was provided as an argument
if [ -n "$1" ]; then
    # If argument provided, set the environment variable
    echo "Setting folder from argument: $1"
    export FOLDER_TO_SHARE="$1"
else
    # If no argument, ensure variable is unset (Python script will ask)
    echo "No folder argument, will prompt for path..."
    unset FOLDER_TO_SHARE
fi

echo "========================================="
echo "         Starting LocalShare..."
echo "========================================="
echo ""

# Run the Python server (it will now ask if FOLDER_TO_SHARE is not set)
python3 backend.py