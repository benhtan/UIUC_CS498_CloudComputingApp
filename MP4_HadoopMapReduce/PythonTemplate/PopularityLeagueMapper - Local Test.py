#!/usr/bin/env python3
import sys


leaguePath = 'league.txt'
#TODO

n = open('partE_PopularityLeague_mapper_debug output.txt', 'w', encoding="utf8")

league = []
with open(leaguePath) as f:
	for line in f:
              league.append(int(line))

# n.write(str(league))

f = open('partD_LinkCount_reducer_debug output.txt', 'r', encoding="utf8")

for line in f:
       link, count = line.rstrip('\n').split()
       if int(link) in league:
              output = f'{link}\t{count}\n'
              n.write(output)

f.close()
n.close()