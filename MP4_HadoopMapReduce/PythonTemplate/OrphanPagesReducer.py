#!/usr/bin/env python3
import sys

data = {}   # keep track of each link ID if it has a parent (true) or not (false). 

for line in sys.stdin:
  # TODO
  parent, child = line.rstrip('\n').split('\t')
  
  if parent != child:
      if parent not in data:
            data[parent] = False
      
      data[child] = True

orphan = []

for link in data:
      if data[link] == False:
            orphan.append(int(link))

sorted_orphan = sorted(orphan)

for link in sorted_orphan:
      print(link)

#TODO
# print(xx) print as final output