#!/usr/bin/env python3
import sys

words = []

for line in sys.stdin:
       line = line.rstrip('\n')
       words.append(line.split('\t'))

words.sort( key=lambda t: (int(t[1]), t[0]) )

for word in words[-10:]:
       output = f'{word[0]}\t{word[1]}'
       print(output)