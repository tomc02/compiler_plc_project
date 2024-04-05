#!/bin/bash
# This script is used to generate the lexer and parser for the Project.g4 grammar file
java -jar antlr-4.13.1-complete.jar Project.g4 -Dlanguage=Python3