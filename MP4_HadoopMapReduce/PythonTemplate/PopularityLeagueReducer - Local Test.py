#!/usr/bin/env python3
import sys
#TODO
f = open('partE_PopularityLeague_mapper_debug output.txt', 'r', encoding="utf8")
n = open('partE_PopularityLeague_reducer_debug output.txt', 'w', encoding="utf8")
# input comes from STDIN
for line in f:
    # TODO
    link, count = line.rstrip('\n').split()
    link = int(link)
    count = int(count)


#TODO
# print('%s\t%s' % (  ,  )) print as final output
f.close()
n.close()