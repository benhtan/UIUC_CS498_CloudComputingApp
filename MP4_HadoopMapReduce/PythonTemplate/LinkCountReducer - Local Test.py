#!/usr/bin/env python3
import sys

f = open('partD_LinkCount_mapper_debug output.txt', 'r', encoding="utf8")
n = open('partD_LinkCount_reducer_debug output.txt', 'w', encoding="utf8")

data = {}   # counting the # of parent of each link (how many link goes into another link)
# input comes from STDIN
for line in f:
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
    output = f'{link[0]}\t{link[1]}\n'
    n.write(output)


# TODO
# print('%s\t%s' % (  ,  )) print as final output

f.close()
n.close()