#!/usr/bin/python

import sys

# the mapper strips the student entries from their names because we don't need them
# the mapper also codes the records binary with 0 and 1, 0 being 'student', 1 being 'mark'

for line in sys.stdin:
	line = line.strip().split("   ")

	if len(line) == 3:
		# if student entry
		stud_id = line[1]
		print("0\t{0}".format(stud_id))

	elif len(line) == 4:
		# if mark entry
		stud_id = line[1]
		course = line[2]
		grade = line[3]
		print("1\t{0}\t{1}\t{2}".format(stud_id, course, grade))