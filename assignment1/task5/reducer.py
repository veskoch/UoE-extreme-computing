#!/usr/bin/python

# Save the 25 most frequent four-token sequences to a heap stream out only those

import sys

i = 0

for line in sys.stdin:
	i += 1
	if i > 25:
		break
	count, seq = line.strip().split("\t")
	print("{0} {1}".format(count, seq))
