#!/usr/bin/env python3
import sys


# TODO

words = []

for line in sys.stdin:
       #TODO
       line = line.rstrip('\n')
       words.append(line.split('\t'))

words.sort( key=lambda t: (int(t[1]), t[0]) )

for word in words[-10:]:
       output = f'{word[0]}\t{word[1]}'
       print(output)


#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
