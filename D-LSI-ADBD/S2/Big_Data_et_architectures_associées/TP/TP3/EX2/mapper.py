#!/usr/bin/env python
import sys

# Read each line from standard input (STDIN)
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    words = line.strip().split('|')
    
    print('%s\t%s' % (words[2], words[4]))

