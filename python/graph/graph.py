class Graph(object):
	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes

	def get_nodes(self):
		return self.nodes

	def addNode(self, node):
		self.nodes.append(node)

	def __str__(self):
		output = ''
		for node in self.nodes:
			for e in node.edge:
				output += str(e.start) + " -" + str(e.weight) + "-> " + str(e.end) + "\n"
			output += "\n"
		return output.strip()