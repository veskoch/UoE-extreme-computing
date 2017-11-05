#!/bin/bash

#Set task var
export INPUT=/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt

#Clear previous output, if any
rm $LOCAL/output.out
rm $LOCAL/output-full.txt

# Run
./task5.py < INPUT > output-full.txt

# Save first 20 lines of output locally
cat output-full.txt | head -20 > output.out