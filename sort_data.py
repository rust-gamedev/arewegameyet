#!/usr/bin/env python3

import sys

import toml

for path in sys.argv[1:]:
    path = path.strip()

    # /contributors/data.toml contains nested tables
    if 'contributors' in path:
        print(f"ignoring '{path}'")
        continue
    else:
        print(f"'{path}'")

    data = toml.load(path)
    for (name, entries) in data.items():
        entries.sort(key=lambda entry: entry['name'].lower())
    with open(path, 'w') as f:
        toml.dump(data, f)

