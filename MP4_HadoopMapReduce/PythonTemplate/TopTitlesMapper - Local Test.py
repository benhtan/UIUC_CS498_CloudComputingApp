#!/usr/bin/env python3
import sys


# TODO

f = open('prePartA_output_TitleCount.txt', encoding="utf8")
words = []

for line in f:
       line = line.rstrip('\n')
       words.append(line.split('\t'))

words.sort(key=lambda t: int(t[1]))

print(words[-5:])
#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer

f.close()