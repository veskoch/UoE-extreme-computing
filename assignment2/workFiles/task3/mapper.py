#!/usr/bin/python

import sys
import heapq
import xml.etree.ElementTree as ET

for line in sys.stdin:
	post = ET.fromstring(line.strip()).attrib
	if post["PostTypeId"] == "1":
		if "AcceptedAnswerId" in post:
			# If a post is a Question, which has an accepted answer, 
			# print the post Id.
			print(post["AcceptedAnswerId"])
	if post["PostTypeId"] == "2":
		# If a post is an Answer, 
		# print the Id of the parent post and the Id of the user who answered the question.
		print("{}\t{}\t{}".format(post["Id"], post["OwnerUserId"], post["ParentId"]))