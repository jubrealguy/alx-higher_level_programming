#!/bin/bash
# Displays the size of the body of the response
res=$(curl -sS "$1")
size=$(echo -n "$res" | wc -c)
echo $size
