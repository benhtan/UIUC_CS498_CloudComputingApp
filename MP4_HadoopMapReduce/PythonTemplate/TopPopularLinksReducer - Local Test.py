#!/usr/bin/env python3
import sys

f = open('partD_TopPopularLinks_mapper_debug output.txt', 'r', encoding="utf8")
n = open('partD_TopPopularLinks_reducer_debug output.txt', 'w', encoding="utf8")

data = []

# input comes from STDIN
for line in f:
    # TODO
    data.append(line.rstrip('\n'))
    # n.write(str(data))
    # print('%s\t%s' % (  ,  )) print as final output
for link in data[-10:]:
    output = link + '\n'
    n.write(output)

f.close()
n.close()