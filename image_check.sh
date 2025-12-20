#!/bin/bash

for file in maps/*.txt; do
  if [ ! -f "maps/$(basename "$file" .txt).jpg" ]; then
    echo "Missing image for '$file'"
    echo "Expected maps/$(basename "$file" .txt).jpg'"
  fi
done
