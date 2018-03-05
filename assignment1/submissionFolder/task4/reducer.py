#!/usr/bin/python

import sys

# iniatialize
seq = ""
prev_seq = ""
count_total = 0

#iterate
for line in sys.stdin:
	seq, count = line.strip().split("\t")
	count = int(count)

	if prev_seq == seq:
		count_total += count

	else:
		if prev_seq:
			print("{0}\t{1}".format(prev_seq, count_total))

		prev_seq = seq
		count_total = count

# Don't forget the last line
if prev_seq == seq:
	print("{0}\t{1}".format(prev_seq, count_total))