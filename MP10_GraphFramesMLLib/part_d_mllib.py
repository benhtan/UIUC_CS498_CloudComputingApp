from pyspark.mllib.tree import RandomForest
from pyspark import SparkContext

sc = SparkContext()


def predict(training_data, test_data):
    # TODO: Train random forest classifier from given data
    # Result should be an RDD with the prediction of the random forest for each
    # test data point
    return None


if __name__ == "__main__":
    raw_training_data = sc.textFile("dataset/training.data")
    raw_test_data = sc.textFile("dataset/test-features.data")

    # TODO: Parse RDD from raw training data
    # Hint: Look at the format of data required by the random forest classifier
    # Hint 2: map() can be used to process each line in raw_training_data and
    # raw_test_data
    training_data = None

    # TODO: Parse RDD from raw test data
    # Hint: Look at the data format required by the random forest classifier
    test_data = None

    predictions = predict(training_data, test_data)

    # You can take a look at dataset/test-labels.data to see if your
    # predictions were right
    for pred in predictions.collect():
        print(int(pred))
