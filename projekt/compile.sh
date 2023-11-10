#!/bin/bash

echo "$1"

COMMAND="javac -classpath $1.java"
eval $COMMAND
jvm2json -s "$1.class" -t "$1.json"




