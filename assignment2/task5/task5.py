#!/usr/bin/python

import sys
import random

# Number of random samples we want
reservoir_size = 50
# List of the random samples
resevoir = []
# Count how many lines we've encountered so far
seen_count = 0


for line in sys.stdin:
	if seen_count < reservoir_size:
		resevoir[seen_count] = line.strip()

	else:
		rand = random.randit(0, seen_count)
		if rand < reservoir_size:
			reservoir[rand] = line.strip()

	seen_count += 1

for line in reservoir:
	print(line)