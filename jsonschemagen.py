#!/usr/bin/env python3

"""
Tool for creating JSON schema from JSON. Input and output are files.
Requires module "genson" to be installed (https://pypi.org/project/genson/).
Should be run from command line.
Required parameters:
-i: input file path in JSON format. Defaults to "json.txt".
-o: output file path. Defaults to "json_schema.txt" in current directory.
"""

import argparse
import json
import sys

import genson


JSONFILE = "json.txt"
OUTFILE = "json_schema.txt"


def write_result(data, filename):
    with open(filename, "w") as file:
        file.write(data)


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--jsonfile", help="File with JSON.", default=JSONFILE)
parser.add_argument("-o", "--outfile", help="Name of the file to export results to.", default=OUTFILE)
args = parser.parse_args()


try:
    in_json = open(args.jsonfile, 'r')
except FileNotFoundError:
    print("JSON file not found.")
    sys.exit(1)

s = genson.SchemaBuilder()
s.add_object(eval(in_json.read()))
res = json.dumps(json.loads(s.to_json()), indent=4)
try:
    write_result(res, args.outfile)
except Exception:
    print(res)
