import heapq
from collections import Counter

import storm


class TopNFinderBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")

        # TODO:
        # Task: set N
        self._N = conf.get('N')    # a constant
        # End

        # Hint: Add necessary instance variables and classes if needed
        self._topN = []         # list of tuples
        self._wordCount = {}    # dict of word and the count

    def process(self, tup):
        '''
        TODO:
        Task: keep track of the top N words
        Hint: implement efficient algorithm so that it won't be shutdown before task finished
              the algorithm we used when we developed the auto-grader is maintaining a N size min-heap
        '''
        self._wordCount[tup.values[0]] = tup.values[1]
        counter = Counter(self._wordCount)
        topN = counter.most_common(self._N)     # list of tuples
        
        if topN != self._topN:
            self._topN = topN
            storm.logInfo(f'TopN: {self._topN}')
            tempList = [e[0] for e in self._topN]
            storm.emit( [ f'top-{self._N}', ', '.join(tempList) ] )
        # End


# Start the bolt when it's invoked
TopNFinderBolt().run()
