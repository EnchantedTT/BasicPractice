class BubbleSort(object):
	def __init__(self, numbers):
		self.values = numbers
		self.count = len(self.values)

	def sort(self):
		self.bubble()
		return self.values

	def bubble(self):
		for i in range(1, self.count):
			for j in range(0, self.count - i):
				if self.values[j] >= self.values[j + 1]:
					tmp = self.values[j]
					self.values[j] = self.values[j + 1]
					self.values[j + 1] = tmp