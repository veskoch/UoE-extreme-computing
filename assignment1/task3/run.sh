#!/bin/bash

export LOCAL=/afs/inf.ed.ac.uk/user/s17/s1753272/Desktop/EXC/assignment1/task3

# Clear previous output, if any
hdfs dfs -rm -r /user/$USER/data/output/assignment1/task3
hdfs dfs -rm -r /user/$USER/data/output/assignment1/task3-temp
rm $LOCAL/output.out

# Run MapReduce Job 1



hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D mapreduce.partition.keycomparator.options=-k1,1rn \
 -files $LOCAL/mapper.py,$LOCAL/reducer.py \
 -input /user/$USER/data/output/assignment1/task2/part-* \
 -output /user/$USER/data/output/assignment1/task3-temp \
 -mapper mapper.py \
 -reducer reducer.py


# Run MapReduce Job 2 (merge output from Job 1)

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.reduces=1 \
 -files $LOCAL/reducer-2.py \
 -input /user/$USER/data/output/assignment1/task3-temp/part-* \
 -output /user/$USER/data/output/assignment1/task3 \
 -mapper cat \
 -reducer reducer-2.py

# #Save output locally for debugging
hdfs dfs -cat /user/$USER/data/output/assignment1/task3/part-00000 | head -20 > $LOCAL/output.out