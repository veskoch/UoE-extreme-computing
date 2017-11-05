#!/usr/bin/python


import sys
import heapq
import xml.etree.ElementTree as ET

top10 = []

# Push the 10 most popular questions 
# to a heap and print out only those

for line in sys.stdin:
	post = ET.fromstring(line.strip()).attrib
	if post["PostTypeId"] == "1" and "ViewCount" in post:
		viewCount = int(post["ViewCount"])
		if len(top10) < 10:
			heapq.heappush(top10, (viewCount, post["Id"]))
		else:
			if viewCount > heapq.nsmallest(1, top10)[0][0]:
				heapq.heappop(top10)
				heapq.heappush(top10, (viewCount, post["Id"]))

for el in top10:
	print("{0}\t{1}".format(el[0], el[1]))