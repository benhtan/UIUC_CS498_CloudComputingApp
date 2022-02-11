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

# for line in sys.stdin:
  
#     # TODO
#     print(line)

#     # print('%s\t%s' % (  ,  )) pass this output to reducer


