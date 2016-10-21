from node import Node

class LinkedList(object):

	def __init__(self):
		self.head = None

	def set_head(self, head_node):
		self.head = head_node

	def __len__(self):
		count = 0
		current = self.head
		while current:
			count += 1
			current = current.get_next()
		return count

	def __str__(self):
		current = self.head
		output = ""
		while current:
			output += str(current) + " -> "
			current = current.get_next()
		return output

	#pop the last item from the list
	def pop(self):
		if self.head:
			self.head = self.head.get_next()
		else:
			raise IndexError("Index out of range! Empty list!")

	#if contrains 
	def contains(self, value):
		flag = False
		current = self.head
		while current and not flag:
			if current.get_data() = value:
				flag = True
			else:
				current = current.get_next()
		return flag

	def delete(self, value):
		current = self.head
		

