import storm
import random
import time

# Define some sentences
SENTENCES = """
the cow jumped over the moon
an apple a day keeps the doctor away
four score and seven years ago
snow white and the seven dwarfs
i am at two with nature
""".strip().split('\n')


class SentenceSpout(storm.Spout):
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Spout instance starting...")

    # Process the next tuple
    def nextTuple(self):
        time.sleep(0.2)
        # TODO
        # Task: randomly generate sentence from sentences string array
        # Note: only generate one sentence in this function
        pass
        # End


# Start the spout when it's invoked
SentenceSpout().run()
