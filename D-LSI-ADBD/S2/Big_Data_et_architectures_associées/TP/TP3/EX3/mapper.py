#!/usr/bin/env python
import sys

# Read each line from standard input (STDIN)
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    line = line.strip().split(',')
    if line[2] == 'TMAX':
        nom = line[0]
        max_temp = int(line[3])
        print('%s\t%s' % (nom, max_temp))
