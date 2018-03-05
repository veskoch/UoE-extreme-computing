#!/bin/bash

#Set task var
export TASK=task7
export OUTPUT=/user/$USER/data/output/assignment1/$TASK
export INPUT=/data/assignments/ex1/uniSmall.txt
export LOCAL=/afs/inf.ed.ac.uk/user/s17/s1753272/Desktop/EXC/assignment1/$TASK

#Clear previous output, if any
hdfs dfs -rm -r $OUTPUT
rm $LOCAL/output.out

#Run
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D mapreduce.partition.keypartitioner.options="-k2,2n" \
 -D mapreduce.partition.keycomparator.options="-k2,2n -k1,1r" \
 -D stream.map.output.field.separator="   " \
 -D stream.num.map.output.key.fields=4 \
 -files $LOCAL/reducer.py,$LOCAL/mapper.py \
 -input $INPUT \
 -output $OUTPUT \
 -mapper mapper.py \
 -reducer reducer.py \
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

#Save output locally for debugging
hdfs dfs -cat $OUTPUT/part-00000 | head -20 > $LOCAL/output.out