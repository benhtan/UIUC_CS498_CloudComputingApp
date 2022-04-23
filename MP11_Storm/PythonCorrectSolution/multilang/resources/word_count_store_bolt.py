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
        self.r = redis.StrictRedis(host=self._redis.get('host'), port=self._redis.get('port'), db=self._redis.get('db'), password=self._redis.get('password'), socket_connect_timeout=self._redis.get('timeout'))
        
    def process(self, tup):
        #Skip this for now
        self.r.hset(self._redis.get('hashKey'), tup.values[0], tup.values[1])

# Start the bolt when it's invoked
WordCountStoreBolt().run()
