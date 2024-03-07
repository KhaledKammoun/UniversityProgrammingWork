#!/usr/bin/env python
import sys

# Read each line from standard input (STDIN)
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Iterate over each word and output it with count 1 to STDOUT
    for word in words:
        # Output the results to STDOUT
        print('%s\t%s' % (word, 1))

