#!/usr/bin/env python
import sys

current_store = None
total_sales = 0

for line in sys.stdin:
    # Split the line into fields
    words = line.strip().split()

    nom = words[0].strip()
    cout = words[1].strip()

    try:
        cout_float = float(cout)
    except ValueError:
        continue
    

    if current_store is not None and current_store != nom:
        print('%s\t%s' % (current_store, total_sales))
        total_sales = 0
    
    current_store = nom
    total_sales += cout_float


if current_store is not None:
    	print('%s\t%s' % (current_store, total_sales))

