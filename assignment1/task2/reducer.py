#!/usr/bin/python

import sys

line = ""
prev_line = ""

for line in sys.stdin:
	line = line.strip()

	if prev_line == line:
		continue

	else:
		if prev_line:
			print(prev_line)

		prev_line = line

# Don't forget the last line
if prev_line == line:
	print(line)