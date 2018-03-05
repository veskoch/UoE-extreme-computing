#!/usr/bin/python

import sys
import random


i = 0

top_key = -1
resevoir = None

for line in sys.stdin:
	weight, line = line.strip().split("\t")
	weight = int(weight)

	key = random.uniform(0, 1)**(1.0/weight)

	if key > top_key:
		top_key = key
		resevoir = line

print(resevoir)