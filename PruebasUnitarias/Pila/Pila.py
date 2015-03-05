class EmptyStackError(Exception):
	pass

class Pila:

	def __init__(self):
		self.list = []

	def isEmpty(self):
		res = (len(self.list) == 0)
		return res

	def push(self,element):
		self.list.append(element)

	def top(self):
		top_element = self.list[-1]
		return top_element

	def pop(self):

		if self.isEmpty():
			raise EmptyStackError
		self.list.pop()