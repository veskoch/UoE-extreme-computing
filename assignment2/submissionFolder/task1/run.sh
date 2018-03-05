#!/bin/bash

#Set task var
export TASK=task1
export OUTPUT=/user/$USER/assignment2/$TASK
export INPUT=/data/assignments/ex2/task1/large/
export LOCAL=/afs/inf.ed.ac.uk/user/s17/s1753272/Desktop/EXC/assignment2/$TASK

#Clear previous output, if any
hdfs dfs -rm -r $OUTPUT
rm $LOCAL/output.out

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.partition.keypartitioner.options="-k1,2" \
 -files $LOCAL/mapper.py,$LOCAL/reducer.py,$LOCAL/combiner.py \
 -input /data/assignments/ex2/part1/large/ \
 -output $OUTPUT \
 -mapper mapper.py \
 -combiner combiner.py \
 -reducer reducer.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

#Save output locally for debugging
hdfs dfs -cat $OUTPUT/part-00000 | head -20 > $LOCAL/output.out