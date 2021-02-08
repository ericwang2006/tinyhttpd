#!/bin/bash
echo "Content-Type: text/html"
echo
echo $CONTENT_LENGTH
echo $QUERY_STRING
read  -n $CONTENT_LENGTH LINE
echo $LINE
