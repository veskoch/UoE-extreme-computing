#!/usr/bin/python

import sys
import heapq
import xml.etree.ElementTree as ET

for line in sys.stdin:
	post = ET.fromstring(line.strip()).attrib
	if post["PostTypeId"] == "2":
		print("{0} -> {1}".format(post["OwnerUserId"], post["Id"]))