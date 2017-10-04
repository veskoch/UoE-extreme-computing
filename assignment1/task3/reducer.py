#!/usr/bin/python

import sys

bytes_found = False
tokens_found = False
max_bytes = 0
max_tokens = 0

for entry in sys.stdin:
	entry = entry.strip()
	Value, Type = entry.split("\t")
	Value = int(Value)

	if Type == "bytes":
		max_bytes = Value
		bytes_found = True

	if Type == "tokens":
		max_tokens = Value
		tokens_found = True

	# no need to to do more iterations than necessary
	if tokens_found and bytes_found:
		break

print("{0}\t{1}".format(max_bytes, "bytes"))
print("{0}\t{1}".format(max_tokens, "tokens"))