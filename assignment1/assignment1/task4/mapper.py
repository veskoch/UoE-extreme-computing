#!/usr/bin/python

import sys

for line in sys.stdin:
	tokens = line.strip().split()

	if len(tokens) > 3:
		for i in range(0, len(tokens) - 3):
			print("{0} {1} {2} {3}\t{4}".format(tokens[i], tokens[i+1], tokens[i+2], tokens[i+3], 1))
