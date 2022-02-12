#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
text = sys.stdin              # needed for submission
# text = []                       # comment before submit
# textPath = 'outputText.txt'     # comment before submit
# with open(textPath, encoding="utf8") as f:          # comment before submit
#     text = [line.rstrip('\n') for line in f]        # comment before submit

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
# f = open('wordCount.txt', 'w', encoding="utf8")     # comment before submit

for word in word_counter:
    output = f'{word}\t{word_counter[word]}'
    print(output)             # needed for submission
    # f.write(output + '\n')      # comment before submit
    

# TODO
# print('%s\t%s' % (  ,  )) print as final output

# f.close()       # comment before submit