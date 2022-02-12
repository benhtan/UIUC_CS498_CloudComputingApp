#!/usr/bin/env python3
import sys

f = open('partC_OrphanPages_mapper_debug output.txt', encoding="utf8")
n = open('partC_OrphanPages_reducer_debug output.txt', 'w', encoding="utf8")

data = {}   # keep track of each link ID if it has a parent (true) or not (false). 

for line in f:
  # TODO
  parent, child = line.rstrip('\n').split('\t')
  
  if parent not in data:
        data[parent] = False
  
  data[child] = True

n.write(str(data))
#TODO
# print(xx) print as final output

f.close()
n.close()