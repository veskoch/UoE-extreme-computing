#!/usr/bin/python

import sys

# most answering author seen so far by the reducer/combiner
most_answered = {}
most_count = -1
most_owner = None
most_posts = []

# sliding window of one currently tracked author
answered = []
prev_userId = None

for line in sys.stdin:
	userId, postId = line.strip().split("\t")
	postId = postId.strip().split(", ")

	if not prev_userId:
	# first line in file
		answered += postId
	else:
		if prev_userId == userId: 	
		# current user is same as previous user
			answered += postId
		else:		
		# current user is different than previous user
			if len(answered) > most_count:
			# we found new most prolific user
				most_count = len(answered)
				most_owner = prev_userId
				most_posts = answered

			# in any case, null counts and keep looking
			answered = []
			answered += postId

	# on each iteration
	prev_userId = userId

# Don't forget the last line
if prev_userId == userId:
	if len(answered) > most_count:
		most_count = len(answered)
		most_owner = prev_userId
		most_posts = answered

	most_posts = ', '.join(map(str, most_posts))
	print("{0} -> {1}".format(most_owner, most_posts))