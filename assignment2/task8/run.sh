#!/bin/bash

#Set task var
export TASK=task8
export OUTPUT=/user/$USER/assignment2/$TASK
export INPUT=/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part4/queriesLarge.txt


#Clear previous output, if any
hdfs dfs -rm -r $OUTPUT
rm $LOCAL/output.out

# Run
./task8.py < INPUT > output-full
hdfs dfs -copyFromLocal output-full OUTPUT

# Save first 20 lines of output locally
cat output-full | head -20 > output.out