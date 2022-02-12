#!/usr/bin/env python3
import sys
import math


f = open('partB_TopTittlesStatistic_mapper_debug output.txt', encoding="utf8")

number = []

def mean(nlist):
    return math.floor(sum(nlist)/len(nlist))

def variance(nlist):
    m = mean(nlist)
    variance = 0
    
    for n in nlist:
        variance += (n - m)**2
        
    return math.floor( variance/len(nlist) )

for line in f:
    # TODO
    count = line.rstrip('\n')
    number.append(int(count))

# print(number)
print(f'Mean\t{mean(number)}')
print(f'Sum\t{sum(number)}')
print(f'Min\t{min(number)}')
print(f'Max\t{max(number)}')
print(f'Var\t{variance(number)}')

f.close()
