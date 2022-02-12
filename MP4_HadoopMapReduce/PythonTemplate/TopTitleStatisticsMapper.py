#!/usr/bin/env python3
import sys


for line in sys.stdin:
    # TODO
    count = line.rstrip('\n').split('\t')[1]
    print(count)
    # print('%s\t%s' % (  ,  )) pass this output to reducer
