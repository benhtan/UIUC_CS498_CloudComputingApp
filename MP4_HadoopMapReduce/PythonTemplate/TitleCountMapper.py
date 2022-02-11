#!/usr/bin/env python3

import sys
import string



# stopWordsPath = sys.argv[1]
# delimitersPath = sys.argv[2]
stopWordsPath = 'stopwords.txt'
delimitersPath = 'delimiters.txt'

stopWords = []
delimiters = []

# TODO
with open(stopWordsPath) as f:
    # TODO
    stopWords = [line.rstrip('\n') for line in f]
    # print(stopWords)

# TODO 
with open(delimitersPath) as f:
    # TODO
    delimiters = f.read().rstrip('\n')
    delimiters = [c for c in delimiters]
    # print(delimiters)

# text = sys.stdin
text = []
textPath = 'titles-a.txt'

def replaceDelimitersWithSpace(w, d):
    for e in d:
        w = w.replace(e, ' ')
    return w

# print(replaceDelimitersWithSpace('Benson_&_Hedges_Match_Play_Championship',delimiters))

with open(textPath, encoding="utf8") as f:
    text = [line.rstrip('\n') for line in f]

for line in text:
      
    # TODO
    word_list = replaceDelimitersWithSpace(line,delimiters).split()
    
    for word in word_list:
        if word not in stopWords:
            print(word.lower() + '\t' + '1')

    # print('%s\t%s' % (  ,  )) pass this output to reducer
