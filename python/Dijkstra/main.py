from node import Node
from edge import Edge
from graph import Graph

def initGraph():
	graph = Graph()

	#Node A
	node_a = Node('A')
	graph.addNode(node_a)

	a_edges = []
	edge_1 = Edge(node_a.nID, 'B', 10)
	a_edges.append(edge_1)
	edge_2 = Edge(node_a.nID, 'C', 20)
	a_edges.append(edge_2)
	edge_3 = Edge(node_a, 'E', 30)
	node_a.set_edge(a_edges)

	#Node B
	node_b = Node('B')
	graph.addNode(node_b)

	b_edges = []
	edge_4 = Edge(node_b, 'C', 5)
	b_edges.append(edge_4)
	edge_5 = Edge(node_b, 'E', 10)
	b_edges.append(edge_5)
	node_b.set_edge(b_edges)

	#Node C
	node_c = Node('C')
	graph.addNode(node_c)

	c_edges = []
	edge_6 = Edge(node_c, 'D', 30)
	c_edges.append(edge_6)
	node_c.set_edge(c_edges)

	#Node D
	node_d = Node('D')
	graph.addNode(node_d)

	#Node E
	node_e = Node('E')
	graph.addNode(node_e)

	e_edges = []
	edge_7 = Edge(node_e, 'D', 20)
	e_edges.append(edge_7)
	node_e.set_edge(e_edges)

	return graph

def main():
	graph = initGraph()
	print graph

if __name__ == "__main__":
	main()