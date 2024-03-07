#!/usr/bin/env python
import sys

# Initialize variables
current_word = None
current_count = 0
word = None

# Read each line from standard input (STDIN)
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    line = line.strip()
    # Split the data using tab as separator, as specified in mapper.py
    word, count = line.split('\t', 1)
    # Convert count (currently a string) to integer
    try:
        count = int(count)
    except ValueError:
        # If count was not a number, then ignore/delete this line
        continue
    # This IF condition works because Hadoop sorts the output of mapping
    # by key (here: the word) before passing it to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Output the result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# Don't forget to output the last occurrence if necessary!
if current_word == word:
    print('%s\t%s' % (current_word, current_count))

