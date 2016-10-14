import random

class Quicksort(object):
	def __init__(self, numbers):
		self.values = numbers
		self.count = len(self.values)

	def sort(self):
		self.quick(0, self.count - 1)
		return self.values

	def quick(self, left, right):
		if left == right:
			return

		i = left
		j = right

		point_index = random.randint(left, right)

		point = self.values[point_index]

		while i <= j:
			while self.values[i] < point:
				i += 1
			while self.values[j] > point:
				j -= 1
			if i <= j:
				if i < j:
					tmp = self.values[i]
					self.values[i] = self.values[j]
					self.values[j] = tmp
				i += 1
				j -= 1

		if left < j:
			self.quick(left, j)
		if right > i:
			self.quick(i, right)