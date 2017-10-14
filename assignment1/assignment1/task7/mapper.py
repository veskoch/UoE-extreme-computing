#!/usr/bin/python

import sys

# the mapper strips the student entries from their names because we don't need them
# the mapper also changes the value in the first column to save bandwidth - student' to 's', and 'mark' to 'm'

for line in sys.stdin:
	line = line.strip().split("   ")

	if len(line) == 3:
		# if student entry
		stud_id = line[1]
		print("s\t{0}".format(stud_id))

	elif len(line) == 4:
		# if mark entry
		stud_id = line[1]
		course = line[2]
		grade = line[3]
		print("m\t{0}\t{1}\t{2}".format(stud_id, course, grade))