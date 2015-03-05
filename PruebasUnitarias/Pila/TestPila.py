import unittest
from Pila import Pila,EmptyStackError

class TestPila(unittest.TestCase):

	
	def testEmptyStack(self):
		
		### ARRANGE
		p = Pila()

		### ACT
		# NADA

		#ASSERT
		self.assertTrue(p.isEmpty())

		### ARRANGE
		p = Pila()

		### ACT
		p.push("Hola")

		#### ASSERT
		self.assertFalse(p.isEmpty())

	def testPushPush(self):

		### ARRANGE
		p = Pila()

		### ACT
		p.push("Hola")
		p.push("Chao")

		#ASSERT
		self.assertEquals("Chao",p.top())	

	def testPushPushPop(self):

		### ARRANGE
		p = Pila()

		### ACT
		p.push("Hola")
		p.push("Chao")
		p.pop()

		#ASSERT
		self.assertEquals("Hola",p.top())

	def testEmptyStackError(self):

		p = Pila()

		self.assertRaises(EmptyStackError,p.pop)	

	
if __name__ == "__main__":

	unittest.main()