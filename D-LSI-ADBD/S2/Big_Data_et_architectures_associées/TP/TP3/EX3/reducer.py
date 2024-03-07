#!/usr/bin/env python
import sys

current_name = None
max_temp = 0

for line in sys.stdin:
    # Split the line into fields
    words = line.strip().split('\t')

    nom = words[0].strip()
    temp = words[1].strip()

    try:
        temp = int(temp)
    except ValueError:
        continue

    if current_name is not None and current_name != nom:
        print('%s\t%s' % (current_name, max_temp))
        max_temp = 0

    current_name = nom
    max_temp = max(max_temp, temp)

if current_name is not None:
    print('%s\t%s' % (current_name, max_temp))


