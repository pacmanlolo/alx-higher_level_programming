#!/bin/bash
# script that sends a JSON POST request to a UR
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
