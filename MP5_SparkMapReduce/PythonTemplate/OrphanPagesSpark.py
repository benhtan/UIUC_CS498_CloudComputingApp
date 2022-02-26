#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO
def parentChild(line):
    line = line.rstrip('\n').split(': ')
    parent = line[0]
    childern = line[1].split()
    # childern = [int(e) for e in childern]   # convert to int
    # childern = [child for child in childern if child != parent]     # remove self link pages
    
    res = [(parent, 0)]
    
    for child in childern:
        res.append((child,1))
        
    return res

lines = lines.flatMap(lambda line: parentChild(line)).reduceByKey(lambda a, b: a + b).filter(lambda line: line[1] == 0)
lines = lines.takeOrdered(lines.count())

output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (line + "\n")
for line in lines:
    output.write(f'{line[0]}\n')

sc.stop()

# spark-submit OrphanPagesSpark.py dataset/links/ partC