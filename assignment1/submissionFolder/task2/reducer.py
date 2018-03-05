#!/usr/bin/python

import sys

# iniatialize
prev_line = False
single_occurence = True

#iterate
for line in sys.stdin:
	line = line.strip()

	# checks if line is 'single' or 'many'
	if prev_line == line:
		single_occurence = False
	# runs on line change
	else:
		if prev_line or prev_line == "": # if not first line in file
			if single_occurence:
				print(prev_line)
		prev_line = line
		single_occurence = True

# Don't forget the last line
if prev_line == line and single_occurence:
	print(line)