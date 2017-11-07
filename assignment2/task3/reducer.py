#!/usr/bin/python

import sys

prev_postId = None

for line in sys.stdin:
	line = line.strip().split("\t")

	if len(line) == 1:
		# We found a Question with an Accepted Answer. 
		# Save the answer Id to compare it with the next line.
		prev_postId = line[0]
	else:
		# This line contains Answer meta-data.
		# If the Id of the Answer matches the Id on the previous line, then jackpot!
		if prev_postId == line[0]:
			# We found an Accepted Answer.
			# print: [ID of the author of the answer] -> [ID of the parent question]
			print("{0} -> {1}".format(line[1], line[2]))
		prev_postId = None