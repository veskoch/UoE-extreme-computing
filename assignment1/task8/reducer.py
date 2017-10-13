#!/usr/bin/python

import sys

lowest_avg = float("inf")

for line in sys.stdin:
	avg, stud_id = line.strip().split('\t')
	avg = float(avg)

	if avg < lowest_avg:
		lowest_avg = avg
		print("{0}\t{1}".format(stud_id, avg))

	elif avg == lowest_avg:
		print("{0}\t{1}".format(stud_id, avg))
