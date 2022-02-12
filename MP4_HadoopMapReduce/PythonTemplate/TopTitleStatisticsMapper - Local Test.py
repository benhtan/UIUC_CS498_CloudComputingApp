#!/usr/bin/env python3
import sys

f = open('partA_output_TopTittles_docker.txt', encoding="utf8")
n = open('partB_TopTittlesStatistic_mapper_debug output.txt', 'w', encoding="utf8")

for line in f:
    # TODO
    count = line.rstrip('\n').split('\t')[1]
    print(count)
    n.write(count + '\n')
    # print('%s\t%s' % (  ,  )) pass this output to reducer

f.close()
n.close()