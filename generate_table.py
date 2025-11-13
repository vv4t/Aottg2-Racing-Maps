#!/usr/bin/env python3

import os
import re
import csv

with open('maps.csv', 'w', newline='') as csvfile:
  fieldnames = ['map_id', 'author', 'name', 'difficulty']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="|")

  writer.writeheader()

  for map_id, file in enumerate(os.listdir("maps")):
    match = re.match(r"(.*?) - (.*) ((?:★|☆)+).txt", file)
    if match:
      author, name, difficulty = (match.group(1), match.group(2), match.group(3))
      difficulty = difficulty.count("★") + difficulty.count("☆") * 0.5
      writer.writerow({
        "map_id": map_id,
        "author": author,
        "name": name,
        "difficulty": difficulty,
      })
    else:
      print(f"Incorrectly formated: {file}.")
