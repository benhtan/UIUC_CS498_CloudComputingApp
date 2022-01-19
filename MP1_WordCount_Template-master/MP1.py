import random 
import os
import string
import sys

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID) # List of random integer refering to "line index" of input.txt
    ret = []
    # TODO
    titles = sys.stdin.readlines()
    
    def split_on_multiple_chars(string_to_split, set_of_chars_as_string):
        # Recursive splitting
        # Returns a list of strings

        s = string_to_split
        chars = set_of_chars_as_string

        # If no more characters to split on, return input
        if len(chars) == 0:
            return([s])

        # Split on the first of the delimiter characters
        ss = s.split(chars[0])

        # Recursive call without the first splitting character
        bb = []
        for e in ss:
            aa = split_on_multiple_chars(e, chars[1:])
            bb.extend(aa)
        return(bb)
    
    # print(split_on_multiple_chars(titles[13], delimiters + '\n'))
    # print(split_on_multiple_chars('paå„stwa', delimiters + '\n'))
    # print(split_on_multiple_chars('a,b', delimiters + '\n'))
    
    # Make list of words from splitted titles
    titlesIndexed = []
    for idx in indexes:
        titlesIndexed += split_on_multiple_chars(titles[idx], delimiters + '\n')
    
    # Cleanup word list. Make lowercase. Remove empty string. Remove stopWordsList
    toBeRemovedIdx = []
    for idx, word in enumerate(titlesIndexed):
        titlesIndexed[idx] = word.lower()
        if word == '' or word in stopWordsList:
            toBeRemovedIdx.append(idx)
    
    while toBeRemovedIdx:
        titlesIndexed.pop(toBeRemovedIdx.pop())
    
    # print(titlesIndexed[:100])
    
    # Calculate word count
    wordCount = {}
    for word in titlesIndexed:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    
    wordCount = {val[0] : val[1] for val in sorted(wordCount.items(), key = lambda x: (-x[1], x[0]))}
    # print(wordCount)
    
    for i, word in enumerate(wordCount):
        if i == 19:
            break
        # print(f'{word} {wordCount[word]}')
        print(word)
    
    # for word in ret:
    #     print(word)

process(sys.argv[1])
