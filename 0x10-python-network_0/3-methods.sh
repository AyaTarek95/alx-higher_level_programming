#!/bin/bash
# take in URL and display all HTTP methods server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
