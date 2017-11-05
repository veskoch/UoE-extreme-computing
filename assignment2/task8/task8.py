#!/usr/bin/python

import sys

threshold = 0.01
error = 0.001
window_size = 1 / error
dictionary = {}
N = 0
i = 0

# Quick test to make sure Lossy Counting makes sense
# 
# count = {}
# for line in sys.stdin:
# 	N += 1
# 	if line in count:
# 		count[line] += 1
# 	else:
# 		count[line] = 1

# d_view = [ (v,k) for k,v in count.iteritems() ]
# d_view.sort(reverse=True) # natively sort tuples by first element
# print(N)
# for v,k in d_view:
#     print "%s: %d" % (k,v)


for line in sys.stdin:
	line = line.strip()
	N += 1
	# inside the window
	if i < window_size:
		if line in dictionary:
			dictionary[line] += 1
		else:
			dictionary[line] = 1
		i += 1
	# between windows
	else:
		i = 0
		for key in list(dictionary):
			if dictionary[key] == 1:
				del dictionary[key]
			else:
				dictionary[key] -= 1

# To reduce false positives to acceptable amount, only
# output counters with frequency f larger than
f = (threshold - error) * N
for key in dictionary:
	if dictionary[key] >= f:
		print(str(key) + "\n")