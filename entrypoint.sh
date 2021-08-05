#!/bin/sh

# Check for sort column. Print usage if it's null
if [ -z $1 ]
then
    echo "\n ERROR: Set a sort column using 'make run sort_column=xxx' \n"
    exit 1
fi

python3 app.py $1