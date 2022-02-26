#!/usr/bin/env python

#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
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

lines = lines.flatMap(lambda line: parentChild(line)).reduceByKey(lambda a, b: a + b)


leagueIds = sc.textFile(sys.argv[2], 1)
leagueIds = leagueIds.map(lambda id: (id,0))

#TODO

output = open(sys.argv[3], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")
lines = lines.join(leagueIds).map(lambda e: (e[0], e[1][0]))
lines = lines.collect()
lines = sorted(lines, key=lambda line: line[1])
lines = [(line[0], i) for i, line in enumerate(lines)]
lines = sorted(lines, key=lambda line: line[0])

for line in lines:
    output.write(f'{line[0]}\t{line[1]}\n')
    
# for id in leagueIds.take(10):
#     output.write(f'ID: {id}\n')

sc.stop()

# spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt partE