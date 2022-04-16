import storm
from collections import Counter


class CountBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")

        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        # TODO
        # Task: word count
        # Hint: using instance variable to tracking the word count
        # Get the word from the inbound tuple
        word = tup.values[0]
        # Increment the counter
        self._counter[word] +=1
        count = self._counter[word]
        storm.logInfo("Emitting %s:%s" % (word, count))
        # Emit the word and count
        storm.emit([word, count])
        # End


# Start the bolt when it's invoked
CountBolt().run()
