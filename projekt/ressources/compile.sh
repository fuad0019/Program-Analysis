#!/bin/bash

echo "$1"

COMMAND="javac --class-path ./ressources/class_files -d ./ressources/class_files  ./ressources/java_files/input_files/\VarDeclareTest.java"
eval $COMMAND
jvm2json -s "$1.class" -t "$1.json"




