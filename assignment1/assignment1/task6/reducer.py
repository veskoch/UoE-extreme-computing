#!/usr/bin/python

import sys, math, ast

prev_context = None
prev_l = {}

def findEntropy(context, l):
	""" 
	Calculates tne entropy of tokens for a given context, following the 
	formula specified in the assignment sheet.
	:: context 		:: three-word context, divided by single space
	:: l 			:: list of integers, indicating the counts of unique tokens which have been observed
										 to follow the given context

	"""

	entropy = 0
	for nominator in l:
		prob = float(nominator) / sum(l)
		entropy -= prob * math.log(prob, 2)
		# here do the entropy math deivision and sumation
	print("{0} {1}\t".format(context, entropy))


for line in sys.stdin:
	context, l = line.strip().split("\t")
	#cast to correct datatypes
	l = ast.literal_eval(l)

	if prev_context != context:
		if prev_context: 
		# enter here only if we have previous context, i.e. ..
		# .. this is not the first line in stdin
			# by now we should looped at least once ..
			# and we should have all the numbers to crunch the entropy 
			findEntropy(prev_context, prev_l)
		prev_l = l
		prev_context = context
		
	else:
	# when previous context = current context ..
	# .. merge the current list to the main list
		prev_l = prev_l + l

# Don't forge the last line
if prev_context == context:
	findEntropy(prev_context, prev_l)