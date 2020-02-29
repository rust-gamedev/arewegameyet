#!/usr/bin/env python3

import sys

import pytoml

for path in sys.argv[1:]:
    path = path.strip()

    # /contributors/data.toml contains nested tables
    if 'contributors' in path:
        print(f"ignoring '{path}'")
        continue
    else:
        print(f"'{path}'")

    output = ''

    with open(path, 'r') as file:
        data = pytoml.load(file)

        for (name, entries) in data.items():
            entries.sort(key=lambda entry: entry['name'].lower())

        output = pytoml.dumps(data)

    with open(path, 'w') as file:
        file.write(output)
