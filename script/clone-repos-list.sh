#!/usr/bin/env bash

rm -R -f acorn-*

readarray array <<< $( cat "$@" )

mkdir -p $(pwd) && cd $(pwd) 

for element in ${array[@]}
do
  echo "clonning $element"
  git clone $element
done