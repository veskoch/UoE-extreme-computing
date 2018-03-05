#!/usr/bin/python

import sys

prev_postId = None
prev_authId = None

for line in sys.stdin:
	line = line.strip().split("\t")

	if len(line) == 2:
		# This line contains Answer meta-data.
		# Save to compare with the next line.
		prev_postId = line[0]
		prev_authId = line[1]
	else:
		# This line is a Question which has an Accepted Answer
		# If the Id of the Question matches the Id on the previous line, then jackpot!
		if prev_postId == line[0]:
			# We found an Accepted Answer.
			# print: [ID of the author of the answer] -> [ID of the parent question]
			print("{0}\t{1}".format(prev_authId, prev_postId))
		prev_postId = None
		prev_authId = None