class Node(object):
	def __init__(self, nID=None, edge=[]):
		self.nID = nID
		self.edge = edge

	def get_nID(self):
		return self.nID

	def set_nID(self, nID):
		self.nID = nID

	def get_edge(self):
		return self.edge

	def set_edge(self, edge):
		self.edge = edge

	def __str__(self):
		return str(self.nID)