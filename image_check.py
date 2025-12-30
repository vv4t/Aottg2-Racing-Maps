#!/usr/bin/env python3

import os
import re

from difflib import SequenceMatcher

def find_similar(author, name, image_file):
  image_name = f"{author} - {name}".lower()  
  
  best_similarity = 0.0
  best_file = None
  
  for map_name, map_file in maps:
    match = SequenceMatcher(None, map_name, image_name).find_longest_match()
    similarity = match.size / max(len(map_name), len(image_name))
    
    if similarity > 0.6 and similarity > best_similarity:
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
      if not find_similar(author, name, file):
        no_matches.append(file)
  else:
    print(f"Incorrectly formated: {file}.")

print("Unmatched images:")

for file in no_matches:
  print(file)
