#! usr/bin/python

import sys
import re

for line in sys.stdin:
	el = line.strip().split(' --> ')

	if len(el) > 1:	
	# if student has grades
		records = el[1].strip().split('  ')
		num_courses = len(records)
		if num_courses > 3:
		# if student has taken more than 3 courses
			stud_id = el[0]
			summed = 0
			for record in records:
				# course = re.search(r"([A-Z])\w+", record).group()
				summed += float(re.search(r"[0-9]+", record).group())

		avg = summed / num_courses

		print("{0}\t{1}".format(avg, stud_id))
