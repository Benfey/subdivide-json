# subidivde-json
Divide your .json file into smaller, equally-sized partitions

Use:
  1. pip install -r requirements.txt
  2. Example usage: python3 subdivide_json.py --file myjson --chunks 10 --output myjson_split

Result:
  myjson.json will be split into ten equal chunks, with any overflow being written to an eleventh file. 
