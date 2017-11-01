#!/usr/bin/python

import sys

# The mapper inserts a flag at the end of each line. The flag indicates whether
# we have encountered one or more than one instaces of the same text. Initially,
# we set all lines to 'S', meaning 'single' occurence so far.  Later, combiners, 
# if called, will collapse repetitive lines to one changing the flag to 'M', 
# meaning that 'more than one' instance has been detected. Reducers will of course
# discard all lines with flag 'M.' However, since combiners do not have complete visibility
# on the entire dataset, reducers will also discard cases of repetitive lines which bear
# the 'S' flag (that happens because repetitive lines may be sent to different mappers).

for line in sys.stdin:
	print(line.strip())