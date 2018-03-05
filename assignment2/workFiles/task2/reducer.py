#!/usr/bin/python

import sys

i = 0

for line in sys.stdin:
	i += 1
	if i > 10:
		break
	viewCount, postId = line.strip().split("\t")
	print("{0} {1}".format(viewCount, postId))