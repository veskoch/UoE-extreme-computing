#!/usr/bin/python

from collections import defaultdict
import sys

prev_term = None

term_index = defaultdict(int)


def format(term_index):
	# fox : 3 : {(d1.txt, 1), (d2.txt, 1),  (d3.txt, 1)}

	string = str()
	for filename in sorted(term_index):
		if string == "":
			string = "({0}, {1})".format(filename, term_index[filename])
		else:
			string += ", ({0}, {1})".format(filename, term_index[filename])

	return("{" + string + "}")


for line in sys.stdin:
	term, file, count = line.strip().split("\t")
	count = int(count)

	if prev_term == term:
		term_index[file] += count

	else:
	# current term is different than previous term
		if prev_term:
			print("{} : {} : {}".format(prev_term, len(term_index), format(term_index)))

		term_index = defaultdict(int)
		prev_term = term
		term_index[file] = count

if prev_term == term:
	print("{} : {} : {}".format(prev_term, len(term_index), format(term_index)))