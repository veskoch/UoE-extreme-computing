#!/usr/bin/python

import os
from bitarray import bitarray

ba_reduced = None

# List dir
for fn in os.listdir("./temp/"):
	# Match prefix
	if fn[:3] == "ba_":
		# Open file
		with open("./temp/" + fn, 'rb') as f:
			# First Bitarray: Read from File
			if not ba_reduced:
				ba_reduced = bitarray()
				ba_reduced.fromfile(f)
			# Later Bitarrays: Bitwise OR
			else:
				ba = bitarray()
				ba.fromfile(f)
				ba_reduced = ba_reduced | ba

with open("bitarray_reduced", 'wb') as f:
	ba_reduced.tofile(f)