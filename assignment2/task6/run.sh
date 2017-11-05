#!/bin/bash

#Set task var
export TASK=task6
export OUTPUT=/user/$USER/assignment2/$TASK
export INPUT=/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt


#Clear previous output, if any
hdfs dfs -rm -r $OUTPUT
rm $LOCAL/output.out

# Run
./task6.py 1900000 < INPUT > output-full
hdfs dfs -copyFromLocal output-full OUTPUT

# Save first 20 lines of output locally
cat output-full | head -20 > output.out

./task6.py 1900000 < data.txt > output-full.txt