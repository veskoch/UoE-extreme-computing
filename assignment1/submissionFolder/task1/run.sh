#!/bin/bash

#Set task var
export TASK=task1
export OUTPUT=/user/$USER/data/output/assignment1/$TASK
export INPUT=/data/assignments/ex1/webSmall.txt
export LOCAL=/afs/inf.ed.ac.uk/user/s17/s1753272/Desktop/EXC/assignment1/$TASK

#Clear previous output, if any
hdfs dfs -rm -r $OUTPUT
rm $LOCAL/output.out

#Run
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -input $INPUT \
 -output $OUTPUT \
 -file $LOCAL/mapper.py \
 -mapper mapper.py \
 -reducer NONE

#Save output locally for debugging
hdfs dfs -cat $OUTPUT/part-00000 | head -20 > $LOCAL/output.out