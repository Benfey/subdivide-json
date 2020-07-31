import json
import argparse

"""
Written by Anton Benfey on July 31st 2020.
This file will split a given .json file into x amount of sub files.

Example usage: python3 subdivide_json.py --file myjson --chunks 10 --output myjson_split
"""

parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True, help="type: string -- the json file (without .json) you want to split. Ex: myfile")
parser.add_argument('--chunks', type=int, required=True, help="type: int -- the number of chunks you want to divide your file into. Ex: 5")
parser.add_argument('--output', required=True, help="type: string -- the name of your output files (without .json). Ex: myfile_output")
args = parser.parse_args()

def split_json():
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    with open(args.file + '.json') as fn:
        data = json.loads(fn.read())
        chunked_file = chunks(data, len(data) // args.chunks)

    for index, part in enumerate(chunked_file):
        with open(args.output + "_" + str(index + 1) + ".json", "w") as fn:
            fn.write(json.dumps(part, indent=4))

if __name__ == '__main__':
    split_json()
