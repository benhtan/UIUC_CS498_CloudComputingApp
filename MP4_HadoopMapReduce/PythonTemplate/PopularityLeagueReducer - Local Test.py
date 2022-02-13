#!/usr/bin/env python3
import sys
#TODO
f = open('partE_PopularityLeague_mapper_debug output.txt', 'r', encoding="utf8")
n = open('partE_PopularityLeague_reducer_debug output.txt', 'w', encoding="utf8")
# input comes from STDIN
data = []   # storing link and count
counts = [] # storing only counts

for line in f:
    # TODO
    link, count = line.rstrip('\n').split()
    link = int(link)
    count = int(count)
    data.append( (link, count) )
    counts.append(count)
    

data.sort(key=lambda t: (t[0]), reverse=True)
counts.sort()

# n.write(str(data))
# n.write(str(counts))
# idx = counts.index(624)
# print(idx)

for el in data:
    link = el[0]
    idx = counts.index(el[1])
    output = f'{link}\t{idx}\n'
    n.write(output)

#TODO
# print('%s\t%s' % (  ,  )) print as final output
f.close()
n.close()