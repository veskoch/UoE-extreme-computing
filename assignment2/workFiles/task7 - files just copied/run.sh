#!/bin/bash

#Set task var
export INPUT=/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt

# Run
./task7.py 1900000 < INPUT > output.txt


# ./task7.py 1900000 < ../webSmall.txt > output.txt
# parallel --block 5M ./task7.py {} “|” bzip2 “>”{.}.bz2 ::: *