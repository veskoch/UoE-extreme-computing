
export OUTPUT=/user/$USER/data/output/assignment1/task1/

hdfs dfs -rm -r $OUTPUT

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
 -input /user/$USER/data/input \
 -output $OUTPUT \
 -mapper mapper.py \
 -file mapper.py

# hdfs dfs -cat $OUTPUT/ | head -20 > output.out