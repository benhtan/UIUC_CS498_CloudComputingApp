from pyspark import SparkContext
from pyspark.sql import SQLContext, SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors
import pyspark.sql.functions as F
from pyspark.sql.types import *
from pyspark.ml.feature import *

############################################
#### PLEASE USE THE GIVEN PARAMETERS     ###
#### FOR TRAINING YOUR KMEANS CLUSTERING ###
#### MODEL                               ###
############################################

NUM_CLUSTERS = 4
SEED = 0
MAX_ITERATIONS = 100
INITIALIZATION_MODE = "random"

sc = SparkContext()
spark = SparkSession(sc)
sqlContext = SQLContext(sc)

FEATURE_COLUMN = [f'val{i}' for i in range(1,12)]


def get_clusters(df, num_clusters, max_iterations, initialization_mode,
                 seed):
    # TODO:
    # Use the given data and the cluster pparameters to train a K-Means model
    # Find the cluster id corresponding to data point (a car)
    # Return a list of lists of the titles which belong to the same cluster
    # For example, if the output is [["Mercedes", "Audi"], ["Honda", "Hyundai"]]
    # Then "Mercedes" and "Audi" should have the same cluster id, and "Honda" and
    # "Hyundai" should have the same cluster id
    # print(df.show())
    vecAssembler = VectorAssembler(inputCols=FEATURE_COLUMN, outputCol="features")
    df_kmeans = vecAssembler.transform(df).select('id', 'features')
    # df_kmeans.show()
    kmeans = KMeans(k=num_clusters, maxIter=max_iterations, initMode=initialization_mode, seed=seed)
    model = kmeans.fit(df_kmeans)
    # centers = model.clusterCenters()

    # print("Cluster Centers: ")
    # for center in centers:
    #     print(center)
    transformed = model.transform(df_kmeans).select('id', 'prediction').collect()
    cluster = {}
    
    for row in transformed:
        if row['prediction'] not in cluster:
            cluster[row['prediction']] = [row['id']]
        else:
            cluster[row['prediction']].append(row['id'])
    
    return [cluster[c] for c in cluster]


def parse_line(line):
    # TODO: Parse data from line into an RDD
    # Hint: Look at the data format and columns required by the KMeans fit and
    # transform functions
    split = line.split(',')
    result = [str(split[0])]
    
    for e in split[1:]:
        result.append(float(e))
    return result


if __name__ == "__main__":
    f = sc.textFile("dataset/cars.data")

    rdd = f.map(parse_line)
    # print(rdd.collect())

    # TODO: Convert RDD into a dataframe
    fields = [StructField("id", StringType(), True)]
    for f in FEATURE_COLUMN:
        fields.append(StructField(f, FloatType(), True))
    
    df = spark.createDataFrame(rdd, StructType(fields))
    # print(df.collect())

    clusters = get_clusters(df, NUM_CLUSTERS, MAX_ITERATIONS,
                            INITIALIZATION_MODE, SEED)
    for cluster in clusters:
        print(','.join(cluster))
