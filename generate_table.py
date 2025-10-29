#!/usr/bin/env python3

import os
import re
import csv

with open('maps.csv', 'w', newline='') as csvfile:
  fieldnames = ['map_id', 'author', 'name', 'difficulty', 'type']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

  writer.writeheader()

  for map_id, file in enumerate(os.listdir("maps")):
    match = re.match(r"(.*) - (.*) ((?:★|☆)+) (\[SPD\]|\[LVA\]|\[SPD, LVA\]).txt", file)
    if match:
      author, name, difficulty, tags = (match.group(1), match.group(2), match.group(3), match.group(4))
      writer.writerow({
        "map_id": map_id,
        "author": author,
        "name": name,
        "difficulty": difficulty,
        "type": tags
      })
    else:
      print(f"Incorrectly formated: {file}.")
