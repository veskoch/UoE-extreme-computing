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
	-D stream.map.output.field.separator="   " \
	-D stream.num.map.output.key.fields=2 \
	-D mapreduce.map.output.key.field.separator=.
	-D num.key.fields.for.partition=2
 -D mapreduce.partition.keycomparator.options="-k2,2nr -k1,1" \
 -files $LOCAL/mapper.py,$LOCAL/reducer.py \
 -input $INPUT \
 -output $OUTPUT \
 -mapper cat \
 -reducer reducer.py

#Save output locally for debugging
hdfs dfs -cat $OUTPUT/part-00000 | head -20 > $LOCAL/output.out