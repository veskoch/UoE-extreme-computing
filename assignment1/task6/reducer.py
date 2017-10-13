#!/usr/bin/python

import sys, math, ast

prev_context = ""
prev_d = {}
denominator = 0

def findEntropy(context, d, denominator):
	""" 
	Calculates tne entropy of tokens for a given context, following the 
	formula specified in the assignment sheet.
	:: context 		:: three-word context, divided by single space
	:: d 			:: dictionary, keys are single-word tokens (str) which follow the given context, 
							       values are counts of of the four-word context + token
	:: denominator 	:: int, total sum of all counts in d (values in the dictionary)

	"""
	entropy = 0
	for key in prev_d:
		prob = float(prev_d[key]) / denominator
		entropy -= prob * math.log(prob, 2)
		# here do the entropy math deivision and sumation
	print("{0}\t{1}".format(context, entropy))


for line in sys.stdin:
	context, d, subtotal = line.strip().split("\t")
	#cast to correct datatypes
	d = ast.literal_eval(d)
	subtotal = int(subtotal)

	if prev_context != context:
		if prev_context: 
		# enter here only if we have previous context, i.e. ..
		# .. this is not the first line in stdin
			# by now we should looped at least once ..
			# and we should have all the numbers to crunch the entropy 
			findEntropy(prev_context, prev_d, denominator)
			denominator = 0
		prev_d = d
		prev_context = context
		denominator += subtotal
		
	else:
	# when previous context = current context ..
	# .. merge the current dictionary to the main dictionary
		for key in d:
			if key in prev_d:
				prev_d[key] += int(d[key])
			else:
				prev_d[key] = int(d[key])

# Don't forge the last line
if prev_context == context:
	findEntropy(prev_context, prev_d, denominator)