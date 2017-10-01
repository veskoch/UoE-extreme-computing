#!/usr/bin/python

import sys

line = ""
prev_line = ""
single_occurence = True

for line in sys.stdin:
	line = line.strip()

	if prev_line == line:
		single_occurence = False

	else:
		if prev_line and single_occurence:
			print(prev_line)

		prev_line = line
		single_occurence = True

# Don't forget the last line
if prev_line == line and single_occurence:
	print(line)