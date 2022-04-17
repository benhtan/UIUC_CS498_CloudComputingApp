import storm
import redis

class WordCountStoreBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._redis = conf.get("redis")  # redis configuration converted into a dictonary
        storm.logInfo("Word Count Store bolt instance starting...")

        # TODO
        # Connect to Redis using redis.Redis() with redis configuration in self._redis dictionary
        # Hint: Add necessary instance variables and classes if needed
        self._r = redis.Redis(host=self._redis.get('host'), port=self._redis.get('port'), db=self._redis.get('db'), password=self._redis.get('password'))


    def process(self, tup):
        # TODO 
        # Task: save word count pair to redis under the specified hash name
        self._r.hset(name="partAWordCount", key=tup.value[0], value=tup.value[1])
        # End

# Start the bolt when it's invoked
WordCountStoreBolt().run()
