#!/bin/bash

# Make the request and save the response to a file
curl -s -o response.txt 0.0.0.0:5000/catch_me

# Extract the message from the response using grep
message=$(grep -o "You got me!" response.txt)

# Remove the response file
rm response.txt

# Output the message
printf "%s\n" "$message"
