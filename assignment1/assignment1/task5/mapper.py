#!/usr/bin/python

import sys
import heapq

# Save the 25 most frequent four-token sequences to a heap stream out only those
top25 = []

for line in sys.stdin:
	seq, count = line.strip().split("\t")
	count = int(count)

	if len(top25) < 25:
		heapq.heappush(top25, (count, seq))
	else:
		if count > heapq.nsmallest(1, top25)[0][0]:
			heapq.heappop(top25)
			heapq.heappush(top25, (count, seq))

for token in top25:
	print("{0}\t{1}".format(token[0], token[1]))