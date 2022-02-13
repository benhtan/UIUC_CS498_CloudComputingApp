#!/usr/bin/env python3
import sys


# TODO



for line in sys.stdin:
       link, count = line.rstrip('\n').split()
       output = f'{link}\t{count}'
       print(output)


#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
