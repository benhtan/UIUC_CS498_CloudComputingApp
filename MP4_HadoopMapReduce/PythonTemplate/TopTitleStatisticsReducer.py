#!/usr/bin/env python3
import sys
import math


def mean(nlist):
    return math.floor(sum(nlist)/len(nlist))

def variance(nlist):
    m = mean(nlist)
    variance = 0
    
    for n in nlist:
        variance += (n - m)**2
        
    return math.floor( variance/len(nlist) )

number = []

for line in sys.stdin:
    count = line.rstrip('\n')
    number.append(int(count))

#TODO
# print('%s\t%s' % (  ,  )) print as final output
print(f'Mean\t{mean(number)}')
print(f'Sum\t{sum(number)}')
print(f'Min\t{min(number)}')
print(f'Max\t{max(number)}')
print(f'Var\t{variance(number)}')
