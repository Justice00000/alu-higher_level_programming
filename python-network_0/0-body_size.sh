#!/bin/bash
#Send request and get the size of the response body in bytes
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
