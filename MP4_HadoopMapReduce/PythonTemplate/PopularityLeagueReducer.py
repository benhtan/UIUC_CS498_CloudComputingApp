#!/usr/bin/env python3
import sys
#TODO
data = []   # storing link and count
counts = [] # storing only counts
# input comes from STDIN
for line in sys.stdin:
    # TODO
    link, count = line.rstrip('\n').split()
    link = int(link)
    count = int(count)
    data.append( (link, count) )
    counts.append(count)

data.sort(key=lambda t: (t[0]), reverse=True)
counts.sort()

for el in data:
    link = el[0]
    idx = counts.index(el[1])
    output = f'{link}\t{idx}'
    print(output)
#TODO
# print('%s\t%s' % (  ,  )) print as final output