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

	if not bytes_found and Type == "bytes":
		max_bytes = Value

	if not tokens_found and Type == "tokens":
		max_tokens = Value

	# no need to to do more iterations than necessary
	if tokens_found and bytes_found:
		break

print("{0}\t{1}".format(-max_bytes, -max_tokens))