from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql import SparkSession

sc = SparkContext()
sqlContext = SQLContext(sc)
spark = SparkSession(sc)

gbooks = sc.textFile("gbooks").map(lambda t: t.split()).map( lambda t: ( t[0], int(t[1]), int(t[2]), int(t[3]) ) )
# print(gbooks.collect())

schema = StructType([ StructField("word", StringType()), StructField("count1", IntegerType()), StructField("count2", IntegerType()), StructField("count3", IntegerType()) ])

gbooks_df = spark.createDataFrame(gbooks, schema)
# print(gbooks_df.collect())

gbooks_df.printSchema()

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)


# Spark SQL - DataFrame API



