#!/usr/bin/python

import sys

lowest_avg 	= float("inf")
found 		= False

for line in sys.stdin:
	if not found:
	# 'if not found' is just a simple optimization
	# Once we find the lowest average, which will be at the top, because input is sorted in 
	# ascending order, there is no need to run any of the code below
		avg, stud_id = line.strip().split('\t')
		avg = float(avg)

		if avg < lowest_avg:
			lowest_avg = avg
			print("{0}\t{1}".format(avg, stud_id))

		elif avg == lowest_avg:
			print("{0}\t{1}".format(avg, stud_id))

		elif avg > lowest_avg:
			found = True