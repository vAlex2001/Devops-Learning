#!/bin/bash

# Check if directory exists.

DIRNAME="testfolder"

if [ -d "$DIRNAME" ]; then
    echo "Directory $DIRNAME already exists"
else
    echo "Directory $DIRNAME does not exist, creating it..."
    mkdir $DIRNAME
    echo "Done. Directory created."
fi