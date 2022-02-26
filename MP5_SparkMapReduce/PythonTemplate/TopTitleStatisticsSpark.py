#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext
import math

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1)

#TODO
lines = lines.collect()
numbers = []

for line in lines:
    numbers.append( int(line.split('\t')[1]) )
    
# print(numbers)

def mean(nlist):
    return math.floor(sum(nlist)/len(nlist))

def variance(nlist):
    m = mean(nlist)
    variance = 0
    
    for n in nlist:
        variance += (n - m)**2
        
    return math.floor( variance/len(nlist) )

outputFile = open(sys.argv[2], "w")

outputFile.write(f'Mean\t{mean(numbers)}\n')
outputFile.write(f'Sum\t{sum(numbers)}\n')
outputFile.write(f'Min\t{min(numbers)}\n')
outputFile.write(f'Max\t{max(numbers)}\n')
outputFile.write(f'Var\t{variance(numbers)}\n')

'''
TODO write your output here
write results to output file. Format
outputFile.write('Mean\t%s\n' % ans1)
outputFile.write('Sum\t%s\n' % ans2)
outputFile.write('Min\t%s\n' % ans3)
outputFile.write('Max\t%s\n' % ans4)
outputFile.write('Var\t%s\n' % ans5)
'''

sc.stop()

# spark-submit TopTitleStatisticsSpark.py partA partB

