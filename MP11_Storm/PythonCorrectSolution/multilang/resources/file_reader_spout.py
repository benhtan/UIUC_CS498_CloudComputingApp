# import os
# from os.path import join
from time import sleep

# from streamparse import Spout
import storm


class FileReaderSpout(storm.Spout):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self._complete = False

        storm.logInfo("Spout instance starting...")

        # TODO:
        # Task: Initialize the file reader
        # hint: get the filename from conf argument 
        self.f = open(conf.get("input.file"), 'r')

    def nextTuple(self):
        # TODO:
        # Task 1: read the next line and emit a tuple for it
        # Task 2: don't forget to sleep for 1 second when the file is entirely read to prevent a busy-loop
        #sentence = self.f.readline()
        #if sentence:
        #    storm.logInfo("Emiting %s" % sentence)
        #    storm.emit([sentence])
        #else:
        #    #self._complete = True
        #    sleep(2)
        #    #self.f.close()
        for sentence in self.f.readlines():
            # Emit a random sentence
            storm.logInfo("Emiting %s" % sentence)
            storm.emit([sentence])
        sleep(1)

# Start the spout when it's invoked
FileReaderSpout().run()
