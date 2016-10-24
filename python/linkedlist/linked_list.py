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
			if current.get_data() == value:
				flag = True
			else:
				current = current.get_next()
		return flag

	#delete all exist value
	def delete(self, value):
		current = self.head
		prev = None
		while current:
			if current.get_data() == value:
				if prev:
					prev.set_next(current.get_next())
				else:
					self.head = current.get_next()
				break
			else:
				prev = current
				current = current.get_next()

	#put value in the front
	def push(self, value):
		node = Node(value)
		node.set_next(self.head)
		self.set_head(node)

	def append(self, value):
		node = Node(value)
		current = self.head
		if current == None:
			self.set_head(node)
			return

		while current.get_next:
			current = current.get_next()

		current.set_next(node)

	def reverse(self):
		current = self.head
		if not current:
			return
		if len(self) == 1:
			return
		elif len(self) == 2:
			tmp = self.head
			tmp.set_next(None)
			self.head = self.head.get_next()
			self.head.set_next(tmp)
		else:
			while current.get_next():
				current_next = current.get_next()
				current.set_next(current_next.get_next())
				current_next.set_next(self.head)
				self.set_head(current_next)

