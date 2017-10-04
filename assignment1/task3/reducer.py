#!/usr/bin/python

import sys

max_bytes = 0
max_tokens = 0

for entry in sys.stdin:
	entry = entry.strip()
	Value, Type = entry.split("\t")
	Value = int(Value)

	if Type == "bytes" and Value > max_bytes:
		max_bytes = Value

	if Type == "tokens" and Value > max_tokens:
		max_tokens = Value

print("{0}\t{1}".format(max_bytes, max_tokens))