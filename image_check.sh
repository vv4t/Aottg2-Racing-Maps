#!/bin/bash

for file in maps/*.txt; do
  image_file="images/$(basename "$file" .txt).jpg"
  if [ ! -f "$image_file" ]; then
    echo "Missing image '$image_file'"
  fi
done

echo "---------------------------------------------"

for file in images/*.jpg; do
  text_file="maps/$(basename "$file" .jpg).txt"
  if [ ! -f "$text_file" ]; then
    echo "Image exists for missing map '$text_file'"
  fi
done
