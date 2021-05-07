'''
Boolean Functions
	@author William Clift
	@author Seraiah Kutai
	@date 3 May 2020

	Run:
		python functions.py

'''
class function:
	def __init__(self, expression):
		self.expression = expression
		self.numVar = countVar(expression)

	def evaluate(self, varList):
		if len(varList)==numVar:
			parse(self.expression)
		else
			return "Error"