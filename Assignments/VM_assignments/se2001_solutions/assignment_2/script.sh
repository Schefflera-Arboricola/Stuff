#!/bin/bash

if ! command -v curl &>/dev/null; then
    echo "Error: curl is not installed. Please install it before running this script."
    exit 1
fi

roll_number="21f2000232"

# URL for the upload
upload_url="http://local.server/upload/${roll_number}.txt"

file_to_upload="${HOME}/se2001/assignment_2/${roll_number}.txt"

# Check if the file exists
if [ ! -f "$file_to_upload" ]; then
    echo "Error: File ${roll_number}.txt not found in ~/se2001/assignment_2."
    exit 1
fi

# Perform the PUT request to upload the file
curl -T "$file_to_upload" "$upload_url"

