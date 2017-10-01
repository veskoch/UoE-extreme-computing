#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	tokenized = line.split()
	len_bytes = len(bytes.decode(line))
	len_tokens = len(tokenized)
	print("{0}\t{1}".format(len_bytes, len_tokens))