#!/bin/bash
# send a DELETE request to URL passed as first argument and display body of response
curl -sX DELETE "$1"
