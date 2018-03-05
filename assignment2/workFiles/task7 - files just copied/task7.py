#!/usr/bin/python

from bitarray import bitarray
import sys
import math
import mmh3

hash_count = 5
array_size = 100

class Bloom():
	def __init__(self, num_entries, false_rate):

		"""
		At initialization, determine the optimal size of the bit array 
		(self.array_size) and number of hash functions (self.hash_count) based
		on the expected number of items that will be inserted (num_entries) 
		and the desired upper boundary for the false positive rate (false_rate).

		:: num_entries :: int()   expected number of items that will inserted
		:: false_rate  :: float() desired false positive rate (for 1% enter 0.01)

		"""

		self.array_size = - int(num_entries * (math.log2(false_rate) / math.log(2)))
		self.hash_count = int((self.array_size / num_entries) * math.log(2))

		self.bit_array = bitarray(self.array_size)
		self.bit_array.setall(0)

	def insert(self, line):
		for seed in range(self.hash_count):
			p = mmh3.hash(line, seed) % self.array_size
			self.bit_array[p] = 1

	def lookup(self, line):
		"""
		Returns False if the line is *definitely not in* the set.
		Returns True if the line is *possibly in* the set.
		"""
		definitelyNotIn = False
		for seed in range(self.hash_count):
			p = mmh3.hash(line, seed) % self.array_size
			if self.bit_array[p] == 0:
				return False
		return True


num_entries = sys.argv[1]
bloom = Bloom(num_entries, 0.01)

for line in sys.stdin:
	bloom.insert(line)

print(bloom)