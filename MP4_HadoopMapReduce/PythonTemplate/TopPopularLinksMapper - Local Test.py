#!/usr/bin/env python3
import sys

f = open('partD_LinkCount_reducer_debug output.txt', 'r', encoding="utf8")
n = open('partD_TopPopularLinks_mapper_debug output.txt', 'w', encoding="utf8")

for line in f:
       link, count = line.rstrip('\n').split()
       output = f'{link}\t{count}\n'
       n.write(output)


#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
f.close()
n.close()