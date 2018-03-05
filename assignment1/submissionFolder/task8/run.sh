#!/bin/bash

#Set task var
export TASK=task8
export OUTPUT=/user/$USER/data/output/assignment1/$TASK
export INPUT=/user/$USER/data/output/assignment1/task7/part-*
export LOCAL=/afs/inf.ed.ac.uk/user/s17/s1753272/Desktop/EXC/assignment1/$TASK

#Clear previous output, if any
hdfs dfs -rm -r $OUTPUT
rm $LOCAL/output.out

#Run
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D mapreduce.partition.keycomparator.options="-k1,1n" \
 -D mapreduce.job.reduces=1 \
 -files $LOCAL/reducer.py,$LOCAL/mapper.py,$LOCAL/combiner.py \
 -input $INPUT \
 -output $OUTPUT \
 -reducer reducer.py \
 -mapper mapper.py \
 -combiner combiner.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

#Save output locally for debugging
hdfs dfs -cat $OUTPUT/part-00000 | head -20 > $LOCAL/output.out