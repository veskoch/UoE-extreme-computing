#!/usr/bin/python

import sys

# The idea here is using stripes (as described in lecture): group pairs into an ..
# .. associate array (i.e. Python dictionary)
# 
# The motivation is to collapse on context, 
# 1) reducing the overal size of the dataset and saving bandwidth during Shuffle & Sort, and
# 2) lowering work the Hadoop sorter has to do (because there are fewer keys)


prev_context = ""
# subtotal is is the preliminary denominator ..
# later we will get the sum of all subtotals to get the final denominator
subtotal = 0
d = {}

for line in sys.stdin:
	seq, count = line.strip().split("\t")
	count = int(count)
	seq = seq.split()
	context = seq[0] + " " + seq[1] + " " + seq[2]
	token = seq[3]

	if prev_context != context:
		if prev_context:
		# if we have previous context, i.e. ..
		# .. not first line in stdin
			print("{0}\t{1}\t{2}".format(prev_context, d, subtotal))
			subtotal = 0

		d = {}
		d[token] = count
		subtotal += count
		prev_context = context

	else:
		if token in d:
			d[token] += int(count)
		else:
			d[token] = int(count)
		subtotal += int(count)


if prev_context == context:
	print("{0}\t{1}\t{2}".format(prev_context, d, subtotal))