#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
# text = sys.stdin
text = []
textPath = 'outputText.txt'
with open(textPath, encoding="utf8") as f:
    text = [line.rstrip('\n') for line in f]

word_counter = {}
# input comes from STDIN
for line in text:
    # TODO
    word_count = line.split('\t')
    
    if word_count[0] in word_counter:
        word_counter[word_count[0]] += int(word_count[1])
    else:
        word_counter[word_count[0]] = 1

# print(word_counter)
f = open('wordCount.txt', 'w', encoding="utf8")

for word in word_counter:
    output = f'{word}\t{word_counter[word]}'
    # print(output)
    f.write(output + '\n')
    

# TODO
# print('%s\t%s' % (  ,  )) print as final output

f.close()