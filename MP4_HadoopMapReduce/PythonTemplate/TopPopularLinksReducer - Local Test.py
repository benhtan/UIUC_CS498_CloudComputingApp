#!/usr/bin/env python3
import sys

f = open('partD_TopPopularLinks_mapper_debug output.txt', 'r', encoding="utf8")
n = open('partD_TopPopularLinks_reducer_debug output.txt', 'w', encoding="utf8")

data = []

# input comes from STDIN
for line in f:
    # TODO
    link, count = line.rstrip('\n').split()
    data.append( (int(link), int(count)) )
    # n.write(str(data))
    # print('%s\t%s' % (  ,  )) print as final output

data.sort( key=lambda t: (t[1], t[0]) )
# n.write(str(data))
for link in data[-10:]:
    output = f'{link[0]}\t{link[1]}\n'
    n.write(output)

f.close()
n.close()