#!/bin/bash

#Set task var
export INPUT=/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt


#Clear previous output, if any
rm output.out
rm output-full.txt

# Run
./task6.py 1900000 < INPUT > output-full.txt

# Save first 20 lines of output locally
cat output-full.txt | head -20 > output.out