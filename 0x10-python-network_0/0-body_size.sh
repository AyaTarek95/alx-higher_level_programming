#!/bin/bash
# take in a URL, sends a request to that URL, and display size of body of response
curl -s "$1" | wc -c
