#!/usr/bin/env python3
import sys

f = open('links.txt', encoding="utf8")
n = open('partD_LinkCount_mapper_debug output.txt', 'w', encoding="utf8")

for line in f:
      #TODO
      line = line.rstrip('\n').split(': ')
      parent = line[0]
      childern = line[1].split()

      for child in childern:
            output = f'{parent}\t{child}'
            n.write(output + '\n')
      # print('%s\t%s' % (  ,  )) pass this output to reducer

f.close()
n.close()