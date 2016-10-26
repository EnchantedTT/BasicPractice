class Edge(object):
	def __init__(self, start, end, weight):
		self.start = start
		self.end = end
		self.weight = weight

	def get_start(self):
		return self.start

	def get_end(self):
		return self.end

	def get_weight(self):
		return self.weight

	def set_start(self, start):
		self.start = start

	def set_end(self, end):
		self.end = end

	def set_weitht(self, weight):
		self.weight = weight