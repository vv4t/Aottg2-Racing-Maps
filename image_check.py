#!/usr/bin/env python3

import os
import re

from difflib import SequenceMatcher

SIMILARITY_SCORE = 0.6
FIND_SIMILAR = False

def find_similar(author, name, image_file):
  image_name = f"{author} - {name}".lower()  
  
  best_similarity = 0.0
  best_file = None
  
  a = set([ x + y for x, y in zip(image_name, image_name[1:]) ])
  
  for map_name, map_file in maps:
    b = set([ x + y for x, y in zip(map_name, map_name[1:]) ])

    similarity = len(a.intersection(b)) / len(a.union(b))
    
    if similarity > SIMILARITY_SCORE and similarity > best_similarity:
      best_similarity = similarity
      best_file = map_file
  
  if best_file:
    image_file = "images/" + image_file
    renamed_image = "images/" + best_file.replace(".txt", ".jpg")
    print("Rename:")
    print(f" FROM: {image_file}")
    print(f" INTO: {renamed_image}")
    if input("Confirm (y/n): ") == "y":
      os.rename(image_file, renamed_image)
      print("Confirmed.")
      print()
    return True
  else:
    return False

maps = []

for file in os.listdir("maps"):
  match = re.match(r"(.*?) - (.*) ((?:★|☆)+).txt", file)
  if match:
    author, name, difficulty = (match.group(1), match.group(2), match.group(3))
    map_name = f"{author} - {name}".lower()
    maps.append((map_name, file)) 
  else:
    print(f"Incorrectly formated: {file}.")

no_matches = []

for file in os.listdir("images"):
  match = re.match(r"(.*?) - (.*) ((?:★|☆)+).jpg", file)
  if match:
    author, name, difficulty = (match.group(1), match.group(2), match.group(3))
    map_file = f"maps/{author} - {name} {difficulty}.txt"
    if not os.path.isfile(map_file):
      if not FIND_SIMILAR or not find_similar(author, name, file):
        no_matches.append(file)
  else:
    print(f"Incorrectly formated: {file}.")

print("Unmatched images:")

for file in no_matches:
  print(f"- {file}")
