#!/usr/bin/env python3
import sys

f = open('partA_top5_mapper_output.txt', encoding="utf8")

words = []

for line in f:
       line = line.rstrip('\n')
       words.append(line.split('\t'))

words.sort( key=lambda t: (int(t[1]), t[0]) )

# print(words[-5:])
#TODO
for word in words[-10:]:
       output = f'{word[0]}\t{word[1]}'
       print(output)
    #    n.write(output + '\n')
# print('%s\t%s' % (  ,  )) pass this output to reducer

f.close()