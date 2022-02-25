#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''
# python TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ partA
# spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ partA

import sys
from pyspark import SparkConf, SparkContext

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stopWords = []
delimiters = []

with open(stopWordsPath) as f:
	#TODO
    stopWords = [line.rstrip('\n') for line in f]

with open(delimitersPath) as f:
    #TODO
    delimiters = f.read().rstrip('\n')
    
def titleToWords(title):
    global delimiters
    global stopWords
    
    for e in delimiters:
        title = title.replace(e, ' ')
    
    title = title.lower().split()
    
    for e in title:
        if e in stopWords:
            title.remove(e)
    
    return title

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[3], 1)

#TODO
res = lines.flatMap(lambda line: titleToWords(line))
res = res.map(lambda word: (word,1)).reduceByKey(lambda a, b: a + b)
res = res.take(500)

outputFile = open(sys.argv[4],"w",encoding="utf8")

#TODO
#write results to output file. Foramt for each line: (line +"\n")
for e in res:    
    outputFile.write(f'{e}\n')

outputFile.close()

sc.stop()
