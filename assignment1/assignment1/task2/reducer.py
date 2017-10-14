#!/usr/bin/python

import sys

# iniatialize
prev_line = False
single_occurence = True

#iterate
for entry in sys.stdin:
	tokenized = entry.strip().rsplit("\t", 1)	# split stdin in two parts: text and flag
	flag = tokenized[-1]						# catch the flag
	if len(tokenized) > 1:						# accomodate for empty text
		line = tokenized[0]
	else:
		line = ""

	# line appears more than once?
	if prev_line == line or flag == "M":
		single_occurence = False

	else:
		if (prev_line or prev_line == "") and single_occurence:         # this accounts for empty lines
			print(prev_line)

		prev_line = line
		single_occurence = True

# Don't forget the last line
if prev_line == line and single_occurence:
	print(line)