#!/usr/bin/python

import sys
import random

# Number of random samples we want
reservoir_size = 100
# List of the random samples
reservoir = []
# Count how many lines we've encountered so far
seen_count = 0


for line in sys.stdin:
	if seen_count < reservoir_size:
		reservoir.append(line.strip())

	else:
		rand = random.randint(0, seen_count)
		if rand < reservoir_size:
			reservoir[rand] = line.strip()

	seen_count += 1

for line in reservoir:
	print(line)