#!/usr/bin/python

import sys

for line in sys.stdin:
	seq, count = line.strip().split("\t")
	seq = seq.split()
	context = seq[0] + " " + seq[1] + " " + seq[2]
	token = seq[3]

	print("{0}\t{1}\t{2}".format(context, token, count))