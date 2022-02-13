#!/usr/bin/env python3
import sys

data = {}   # counting the # of parent of each link (how many link goes into another link)

# input comes from STDIN
for line in sys.stdin:
    # TODO
    parent, child = line.rstrip('\n').split('\t')
    
    if parent != child:
        child = int(child)
        
        if child in data:
            data[child] += 1
        else:
            data[child] = 1

data = list(data.items())
data.sort( key=lambda t: (t[1], t[0]) )

for link in data:
    output = f'{link[0]}\t{link[1]}'
    print(output)