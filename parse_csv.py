import csv

with open('maps.csv', 'r', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter="|")
  with open('maps-comma.csv', 'w', newline='') as csvfile:
    for row in reader:
      map_id, author, name, difficulty, tags, notes = tuple(row)
      fieldnames = ['map_id', 'author', 'name', 'difficulty', 'tags', 'notes']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writerow({
        "map_id": map_id,
        "author": author,
        "name": name,
        "difficulty": difficulty,
        "tags": tags,
        "notes": notes
      })
