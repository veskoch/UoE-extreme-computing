#!/bin/bash

export LOCAL=/afs/inf.ed.ac.uk/user/s17/s1753272/Desktop/EXC/assignment1/$TASK

# Clear previous output, if any
hdfs dfs -rm -r /user/$USER/data/output/assignment1/task3
hdfs dfs -rm -r /user/$USER/data/output/assignment1/task3-temp
rm $LOCAL/output.out

# Run MapReduce Job 1
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -input /user/$USER/data/output/assignment1/task2/part-* \
 -output /user/$USER/data/output/assignment1/task3-temp \
 -files $LOCAL/mapper.py, $LOCAL/reducer.py \
 -mapper $LOCAL/mapper.py \
 -reducer $LOCAL/reducer.py


# Run MapReduce Job 2 (merge output from Job 1)

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.reduces=1 \
 -input /user/$USER/data/output/assignment1/task3-temp/part-* \
 -output /user/$USER/data/output/assignment1/task3 \
 -files $LOCAL/reducer.py \
 -mapper cat \
 -reducer reducer.py

#Save output locally for debugging
hdfs dfs -cat /user/$USER/data/output/assignment1/task3/part-00000 | head -20 > $LOCAL/output.out