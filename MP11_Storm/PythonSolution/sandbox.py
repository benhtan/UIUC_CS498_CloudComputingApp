import heapq
from collections import Counter

wordCount = {'apple': 11, 'dog': 23, 'tree': 3}
res = Counter(wordCount)
print(res.most_common(2))