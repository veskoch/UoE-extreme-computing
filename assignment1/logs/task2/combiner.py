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
		line = tokenized[0].strip()
	else:
		line = ""

	# checks if line is 'single' or 'many'
	if flag == "M":
		single_occurence = False
	if prev_line == line:
		single_occurence = False
	# runs on line change
	if prev_line != line:
		if prev_line or prev_line == "": # if not first line in file
			if single_occurence:		
				print(prev_line + "\tS")
			else:
				# put a marker indicating the line is a duplicate
				# keep in output to match against output of other mappers
				print(prev_line + "\tM")
		prev_line = line
		single_occurence = True

# Don't forget the last line
if prev_line == line:
	print(line + "\tS")