import json
import csv


csv_file = open('song_dataset.csv', 'r')
json_file = open('song_dataset.json', 'w')
fieldnames = ('Id', 'Album', 'Title', 'Lyrics')
reader = csv.DictReader(csv_file, fieldnames)
out = json.dumps([row for row in reader], sort_keys=True, indent=2)
json_file.write(out)
