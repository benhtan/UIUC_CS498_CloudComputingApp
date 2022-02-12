#!/usr/bin/env python3

import sys
import string



# stopWordsPath = sys.argv[1]       # needed for submission
# delimitersPath = sys.argv[2]      # needed for submission
stopWordsPath = 'stopwords.txt'     # comment before submit
delimitersPath = 'delimiters.txt'   # comment before submit

stopWords = []
delimiters = []

# TODO
with open(stopWordsPath) as f:
    # TODO
    stopWords = [line.rstrip('\n') for line in f]
    # print(stopWords)  # comment before submit

# TODO 
with open(delimitersPath) as f:
    # TODO
    delimiters = f.read().rstrip('\n')
    delimiters = [c for c in delimiters]
    # print(delimiters) # comment before submit

# text = sys.stdin        # needed for submission
text = []               # comment before submit
textPath = 'input.txt'  # comment before submit

def replaceDelimitersWithSpace(w, d):
    for e in d:
        w = w.replace(e, ' ')
    return w.lower()

# print(replaceDelimitersWithSpace('Benson_&_Hedges_Match_Play_Championship',delimiters))   # comment before submit

with open(textPath, encoding="utf8") as f:      # comment before submit
    text = [line.rstrip('\n') for line in f]    # comment before submit

f = open('outputText-debug output.txt', 'w', encoding="utf8")    # comment before submit

for line in text:
      
    # TODO
    word_list = replaceDelimitersWithSpace(line,delimiters).split()
    
    for word in word_list:
        if word not in stopWords:
            output = word + '\t' + '1'
            # print(output)             # needed for submission
            f.write(output + '\n')      # comment before submit

    # print('%s\t%s' % (  ,  )) pass this output to reducer
    
f.close()   # comment before submit
