#!/bin/bash

#Set task var
export TASK=task2
export OUTPUT=/user/$USER/data/output/assignment1/$TASK
export INPUT=/user/$USER/data/output/assignment1/task1/part-*
export LOCAL=/afs/inf.ed.ac.uk/user/s17/s1753272/Desktop/EXC/assignment1/$TASK

#Clear previous output, if any
hdfs dfs -rm -r $OUTPUT
rm $LOCAL/output.out

#Run
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -files $LOCAL/mapper.py,$LOCAL/reducer.py \
 -input $INPUT \
 -output $OUTPUT \
 -mapper mapper.py \
 -reducer reducer.py

#Save output locally for debugging
hdfs dfs -cat $OUTPUT/part-00000 | head -20 > $LOCAL/output.out