'''
Boolean Functions
	@author William Clift
	@author Seraiah Kutai
	@dat 3 May 2020

	Run:
		python functions.py

'''
class Error(Exception):
    pass

class InvalidValueException(Error):
    pass

class var:
	def __init__(self, name, value):
		try:
			self.name = name
			self.next = null
			if(type(value)==int and (value==0 or value==1))
				self.value = value
			else
				raise InvalidValueException
		except InvalidValueException:
			print("Invalid Value")
			

class symbolTable:
	def __init__(self, head):
		self.head = head
		self.tail = head
		self.size = 1

	def add(self, name, value):
		newVar = var(name, value)
		self.tail.next = newVar
		self.tail = newVar
		self.size += 1

	def purge(self):
		self.head = null
		self.tail = null

class function:

	def __init__(self, expression):
		self.expression = expression
		self.numVar = countVar(expression)

	def evaluate(self, varList):
		if len(varList)==numVar:
			parse(self.expression)
		else
			return "Error"


