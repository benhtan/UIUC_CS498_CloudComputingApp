from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql import SparkSession

sc = SparkContext()
sqlContext = SQLContext(sc)
spark = SparkSession(sc)

# read from text file. split each line into 4 colums. convert to tuple (string, int, int, int)
gbooks = sc.textFile("gbooks").map(lambda t: t.split()).map( lambda t: ( t[0], int(t[1]), int(t[2]), int(t[3]) ) )
# print(gbooks.collect())

# create dataframe schema
schema = StructType([ StructField("word", StringType()), StructField("count1", IntegerType()), StructField("count2", IntegerType()), StructField("count3", IntegerType()) ])

# create dataframe using data and schema
gbooks_df = spark.createDataFrame(gbooks, schema)
# print(gbooks_df.collect())

# Creates a temporary view using the DataFrame
gbooks_df.createOrReplaceTempView("gbooks_view")

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)


# Spark SQL - DataFrame API


####
# 5. Joining (10 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####

df2 = gbooks_df.select("word", "count1").distinct().limit(100);
df2.createOrReplaceTempView('gbooks2')

# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API

# output: 210

results = spark.sql("SELECT count(word) FROM gbooks2 INNER JOIN gbooks2 ON count1")

results.show()

