import heapq
from collections import Counter

import storm


class TopNFinderBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")

        # Create a new counter for this instance
        self._top_N = Counter()
        self.n = conf.get("N")

    def process(self, tup):
        '''
        TODO:
        Task: keep track of the top N words
        Hint: implement efficient algorithm so that it won't be shutdown before task finished
              the algorithm we used when we developed the auto-grader is maintaining a N size min-heap
        '''
        word = tup.values[0]
        count = tup.values[1]
        self._top_N[word] = count
        n_keys_sorted_by_values = heapq.nlargest(self.n, self._top_N, key=self._top_N.get)
        top_n_words = ', '.join(n_keys_sorted_by_values)
        storm.logInfo("Emiting %s" % top_n_words)
        storm.emit([top_n_words])


# Start the bolt when it's invoked
TopNFinderBolt().run()
