#!/usr/bin/python

import sys

# iniatialize
prev_stud = ""

#iterate
for line in sys.stdin:
	tokenized = line.strip().split("\t")

	tag = tokenized[0]
	stud_id = tokenized[1]

	if prev_stud:
		if prev_stud != stud_id:
			print("")

	if tag == "0":
		sys.stdout.write("{0} -->".format(stud_id))

	if tag == "1":
		course = tokenized[2]
		grade = tokenized[3]
		sys.stdout.write("  ({0}, {1})".format(grade, course))

	prev_stud = stud_id

# Check corner cases
# student   124   Kalyn	
# mark   124   AV   97	
# mark   124   INF1-CG   80	
# mark   124   ANLP   68	
# student   129   Alfrey	
# mark   129   ES   45	
# student   133   Aldis	
# student   138   Allis	