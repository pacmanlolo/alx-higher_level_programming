#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -si "$1" | sed -n 's/Content-Length: \([0-9]\+\)/\1/p'
