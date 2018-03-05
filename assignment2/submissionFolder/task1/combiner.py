#!/usr/bin/python

import sys

prev_term = None
total = 0

# Hadoop sends each file to different mapper.
# Hence, we know all terms below are from the same file.

for line in sys.stdin:
	term, file, count = line.strip().split("\t")
	count = int(count)

	if prev_term == term:
		total += count
	else:
		if prev_term:
			print("{0}\t{1}\t{2}".format(prev_term, file, total))

		prev_term = term
		total = count


if prev_term == term:
	print("{0}\t{1}\t{2}".format(prev_term, file, total))