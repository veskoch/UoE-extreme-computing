#!/bin/bash

#Set task var
export INPUT=/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part4/queriesLarge.txt


#Clear previous output, if any
rm $LOCAL/output-full.txt
rm $LOCAL/output.out

# Run
./task8.py < INPUT > output-full.txt

# Save first 20 lines of output
cat output-full.txt | head -20 > output.out


# Line below for local testing
# ./task8.py < queriesSmall.txt > output-full.txt