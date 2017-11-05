#!/usr/bin/python


import sys
import


path = os.environ["mapreduce_map_input_file"]
filename = path.rsplit('/', 1)[-1]

for line in sys.stdin:
	terms = line.strip().split(" ")

	for term in terms:
		print("{0}\t{1}\t1".format(term, filename))