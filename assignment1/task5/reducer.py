#!/usr/bin/python

import sys
# Save the 25 most frequent four-token sequences to a heap stream out only those
i = 0

for line in sys.stdin:
	i += 1
	if i > 5:
		break
	count, seq = line.strip().split("\t")
	print("{0} {1}".format(count, seq))
