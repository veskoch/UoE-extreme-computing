#!/usr/bin/python



# Each mapper will return one line at random with a weight.
# The weight is the number of lines which the mapper has processed.
# Implements a version of https://gregable.com/2007/10/reservoir-sampling.html

import sys
import random

line_count = 0
resevoir = None

for line in sys.stdin:
	if random.randit(0, line_count) == 0:
		resevoir = line.strip()
	line_count += 1

print("{0}\t{1}".format(line_count, resevoir))