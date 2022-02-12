#!/usr/bin/env python3
import sys

f = open('partA_top5_mapper_output.txt', encoding="utf8")

# input comes from STDIN
for line in f:
    # TODO
    word = line.rstrip('\n')
    print(word)
    # print('%s\t%s' % (  ,  )) print as final output

f.close()