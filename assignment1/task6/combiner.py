#!/usr/bin/python

import sys

# time two MapReduce jobs: one with two MapReducers, the other one with unbounded memeory problem
# I suppose the unbounded memeory will be faster 

# The idea here is to collapse tokens on context.
#
# For example, given 'big green apple' context, 
# 		big green apple 	pie 	7
# 		big green apple 	donut 	4
# 		big green apple 	candy 	3
# We collapse three lines to one:
#		big green apple | 'pie donut candy' | '7 4 3'
# 
# The motivation is to reduce repetitive strings, which 
# 1) reduces the overal size of the dataset saving bandwidth, and
# 2) lowers work the Hadoop sorter has to do (because there are fewer keys)


prev_context = ""
prev_token = ""
prev_count = -1

bound = 500
tokens = ""
counts = ""

# WHAT HAPPENS ON
# first iteration
# when line appears only once
# first time line appears

for line in sys.stdin:
	context, token, count = line.strip().split("\t")
 
	if prev_context == context:
		tokens.append(" " + prev_token)
		counts.append(" " + prev_count)

	else:
		if prev_context: # if not first line
			print("{0}\t{1}\t{2}".format(context, tokens, counts))





# Don't forge the last line
