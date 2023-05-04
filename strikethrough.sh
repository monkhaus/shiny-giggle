#!/bin/bash

text=$1
formatted_text="\e[9m${text}\e[0m"

echo -e "$formatted_text"
