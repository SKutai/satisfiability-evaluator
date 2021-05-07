
class Parse:
	def __init__(self):
		pass

	def evaluate(self, tokens):
		print(self.evaluateExpression(tokens))


	def evaluateExpression(self, tokens):
		stack = []
		for e in tokens:
			ty = e[0]					# Get the Token Type
			if ty == 'rpar':
				eval = []
				while True:
					token = stack.pop()
					if token[0] == 'lpar':
						value = self.evaluateExpression(eval)
						stack.append(value)
						break
					else:
						eval.append(token)
			elif ty == 'spc':
				break
			else:
				stack.append(e)

		right = stack.pop()
		if len(stack) < 1:
			return right
		if right[0] == 'true':
			middle = stack.pop()
			if middle[0] == 'n':
				return ['false', '0']
			elif middle[0] == 'o':
				return ['true', '1']
			elif middle[0] == 'x':
				left = stack.pop()
				if left[0] == 'false':
					return ['true', '1']
				else:
					return ['false', '0']
			elif middle[0] == 'a':
				left = stack.pop()
				if left[0] == 'true':
					return ['true', '1']
				else:
					return ['false', '0']
		else:	# Right is False
			middle = stack.pop()
			if middle[0] == 'n':
				return ['true', '1']
			elif middle[0] == 'o':
				left = stack.pop()
				if left[0] == 'true':
					return ['true', '1']
				else:
					return ['false', '0']
			elif middle[0] == 'x':
				left = stack.pop()
				if left[0] == 'true':
					return ['true', '1']
				else:
					return ['false', '0']
			elif middle[0] == 'a':
				return ['false', '0']
		return