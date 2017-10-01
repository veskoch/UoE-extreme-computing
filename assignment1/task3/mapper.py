#!/usr/bin/python

import sys

max_bytes = 0
max_tokens = 0

for line in sys.stdin:
	line = line.strip()
	tokenized = line.split()
	len_bytes = len(bytes.decode(line))
	len_tokens = len(tokenized)

	if len_bytes > max_bytes:
		max_bytes = len_bytes

	if len_tokens > max_tokens:
		max_tokens = len_tokens

# negate since Hadoop sorts in ascending order by default (that will be useful in Reduce)
print("{0}\t{1}".format(-max_bytes, "bytes"))
print("{0}\t{1}".format(-max_tokens, "tokens"))