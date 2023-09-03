#!/bin/bash

if ! command -v wget &>/dev/null; then
    echo "Error: wget is not installed. Please install it before running this script."
    exit 1
fi

base_url="http://local.server"
file1="sample_1.txt"
file2="sample_2.txt"
file3="sample_3.txt"
file4="sample_4.txt"

wget "${base_url}/${file1}" -O ~/se2001/assignment_1/s1.txt

curl -o ~/se2001/assignment_1/s2.txt "${base_url}/${file2}"

curl -o ~/se2001/assignment_1/s3.txt "${base_url}/${file3}"

curl -o ~/se2001/assignment_1/s4.txt "${base_url}/${file4}"
