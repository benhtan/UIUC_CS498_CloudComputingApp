from pyspark import *
from pyspark.sql import SparkSession
from graphframes import *

sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()


def get_connected_components(graphframe):
    # TODO:
    # get_connected_components is given a graphframe that represents the given graph
    # It returns a list of lists of ids.
    # For example, [[a_1, a_2, ...], [b_1, b_2, ...], ...]
    # then a_1, a_2, ..., a_n lie in the same component,
    # b_1, b2, ..., b_m lie in the same component, etc
    comp = g.connectedComponents().collect()
    result_dict = {}
    for row in comp:
        if row['component'] not in result_dict:
            result_dict[row['component']] = [row['id']]
        else:
            result_dict[row['component']].append(row['id'])
    print(result_dict)
    # print(result.select("id", "component").orderBy("component").collect())
    return [[]]


if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    with open('dataset/graph.data') as f:  # Do not modify
        for line in f:
            src = line.split()[0]  # TODO: Parse src (source) from line
            dst_list = line.split()[1:]  # TODO: Parse dst_list (destination) from line
            vertex_list.append((src,))
            edge_list += [(src, dst) for dst in dst_list]
    
    # print(vertex_list)
    # print(edge_list)
    
    vertices = spark.createDataFrame(vertex_list, ["id"])  # TODO: Create vertices dataframe
    edges = spark.createDataFrame(edge_list, ["src", "dst"])  # TODO: Create edges dataframe

    g = GraphFrame(vertices, edges)
    sc.setCheckpointDir("/tmp/connected-components")

    result = get_connected_components(g)
    # for line in result:
    #     print(' '.join(line))
