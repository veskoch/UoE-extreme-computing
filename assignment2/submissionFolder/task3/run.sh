#!/bin/bash

#Set task var
export LOCAL=/afs/inf.ed.ac.uk/user/s17/s1753272/Desktop/EXC/assignment2/task3

#Clear previous output, if any
hdfs dfs -rm -r /user/$USER/assignment2/task3/
hdfs dfs -rm -r /user/$USER/assignment2/temp/task3/
rm $LOCAL/output.out


# Run Job 1
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2nr" \
 -D stream.num.map.output.key.fields=2 \
 -D mapreduce.job.reduces=1 \
 -files $LOCAL/mapper.py,$LOCAL/reducer.py \
 -input /data/assignments/ex2/part2/stackLarge.txt \
 -output /user/$USER/assignment2/temp/task3/ \
 -mapper mapper.py \
 -reducer reducer.py

#Run Job 2
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
 -D mapreduce.partition.keycomparator.options="-k1,1n" \
 -D mapreduce.job.reduces=1 \
 -files $LOCAL/reducer2.py,$LOCAL/combiner2.py \
 -input /user/$USER/assignment2/temp/task3/part-* \
 -output /user/$USER/assignment2/task3/ \
 -mapper cat \
 -combiner combiner2.py \
 -reducer reducer2.py

#Save output locally for debugging
hdfs dfs -cat /user/$USER/assignment2/task3/part-00000 | head -20 > $LOCAL/output.out


# For debugging on a single machine 
# cat stackLarge.txt | ./mapper.py | sort -k1,1n -k2,2nr | ./reducer.py | sort -k1,1n | ./combiner2.py | ./reducer2.py > ha.txt

