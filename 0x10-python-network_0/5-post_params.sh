#!/bin/bash
# Take in a url POST key and display the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
