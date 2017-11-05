#!/usr/bin/python

import sys

prev_term = None

files = []

for line in sys.stdin:
	term, file, count = line.strip().split("\t")
	count = int(count)


	if prev_term == term:



	for t in terms:
		print("{0}\t{1}".format(t, filename))