#!/bin/bash

# Create temp dir
mkdir ./temp
# Clear earlier bitarray, if any
rm bitarray_reduced


# Run Bloom filter in parallel
pv /afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt | parallel --pipe --block 10M ./task7.py 1900000

# Reduce the bitarrays from multiple processes
./reduce.py

# Remove temp files
rm -r ./temp/