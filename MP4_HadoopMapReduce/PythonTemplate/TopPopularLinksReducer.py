#!/usr/bin/env python3
import sys


data = []
# input comes from STDIN
for line in sys.stdin:
    # TODO
    link, count = line.rstrip('\n').split()
    data.append( (int(link), int(count)) )
    # n.write(str(data))
    # print('%s\t%s' % (  ,  )) print as final output

data.sort( key=lambda t: (t[1], t[0]) )
# n.write(str(data))
for link in data[-10:]:
    output = f'{link[0]}\t{link[1]}'
    print(output)
