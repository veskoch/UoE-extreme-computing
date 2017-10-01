#!/usr/bin/python

import sys

max_bytes = 0
max_tokens = 0

for line in sys.stdin:
	line = line.strip()
	len_bytes, len_tokens = line.split("\t", 1)
	len_bytes = int(len_bytes)
	len_tokens = int(len_tokens)

	if len_bytes > max_bytes:
		max_bytes = len_bytes

	if len_tokens > max_tokens:
		max_tokens = len_tokens

print("{0}\t{1}".format(max_bytes, max_tokens))