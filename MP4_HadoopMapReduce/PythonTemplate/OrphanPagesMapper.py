#!/usr/bin/env python3
import sys


for line in sys.stdin:
  # TODO
  line = line.rstrip('\n').split(': ')
  parent = line[0]
  childern = line[1].split(' ')

  for child in childern:
        output = f'{parent}\t{child}'
        print(output)
  # print('%s\t%s' % (  ,  )) pass this output to reducer
