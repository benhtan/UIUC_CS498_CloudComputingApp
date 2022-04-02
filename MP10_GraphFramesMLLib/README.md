# CS 498 - MP10 GraphFrames and MLLib Templates

This repository contains templates to help you get started with MP10.

## Log
Last updated in May 2021, by Yifan Chen (yifanc3@illinois.edu).

Last updated in May 2021, by Sam Cheng (rcheng12@illinois.edu).

# ML vs MLLib
- Parts B and D (MLLib exercises) can be solved using either the
Dataframe-based API (pyspark.ml) or the RDD-based API (pyspark.mllib).
The corresponding templates for each have the suffix `_ml` and `_mllib`.
Make sure you rename the python files corresopnding to parts B and D to 
`part_b.py` and `part_d.py` respectively before submitting them.

# Execution instructions
- Each file can be executed by running
```spark-submit part_xxx.py```
- You can alternatively run the following to get rid of spark logs
```spark-submit part_xxx.py 2> /dev/null```
- Make sure that you have the given dataset in the directory you are running
the given code from. The structure this repository is arranged in is recommended.
- While the extra argument for graphframes is not required for part b
and part d, it is not necessary to remove it these parts
