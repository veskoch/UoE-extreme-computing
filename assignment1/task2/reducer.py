#!/usr/bin/python

import sys

# iniatialize
prev_line = False
single_occurence = True

#iterate
for line in sys.stdin:
	line = line.strip()		#housekeeping

	# line appears at least twice?
	if prev_line == line:
		single_occurence = False

	else:
		if (prev_line or prev_line == "") and single_occurence:		# this accounts for empty lines
			print(prev_line)

		prev_line = line
		single_occurence = True

# Don't forget the last line
if prev_line == line and single_occurence:
	print(line)