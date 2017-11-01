#!/usr/bin/python

import sys

# The idea here is to use a version of stripes, as described in lecture. We only
# stdout context followed by a list of counts of the possible forth words, for example:
# big green apple	[7, 4, 3]
# This strategy is possible, because we know the input is sorted and there are no duplicates.
# Later, the reducer will do a merge in case the same context had been split between mappers.
# 
# The motivation is to, 
# 1) reduce the overal size of the dataset and save bandwidth during Shuffle & Sort, and
# 2) lower work the Hadoop sorter has to do (because there are fewer keys)
#
# While technically the list is unbounded,

prev_context = ""
l = []

for line in sys.stdin:
	seq, count = line.strip().split("\t")
	count = int(count)
	context = seq.rsplit(" ",1)[0]

	if prev_context != context:
		if prev_context:
		# if we have previous context, i.e. ..
		# .. not first line in stdin
			print("{0}\t{1}".format(prev_context, l))

		l = []
		l.append(count)
		prev_context = context

	else:
		l.append(count)


if prev_context == context:
	print("{0}\t{1}".format(prev_context, l))