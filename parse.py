from symbolTable import symbolTable

class Parse:
	def __init__(self):
		pass

	def evaluate(self, tokens):

        # check if this line is assigning to variable
        addingToTable = False
        if tokens[0][0] == 'vari' and tokens[1][0] == 'asgn':
            name = tokens[0][1]
            tokens = tokens[2:] # pop the first two tokens off
            addingToTable = True

        # resolve the value of the line
        val = self.evaluateExpression(tokens)
		print(val)

        # add the variable to the symbol table
        if addingToTable:
            symbolTable.add(name, val)

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

        # check for a variable
        # then change the value of right to mimic reading a true or false
        if right[0] == 'vari':
            variVal = right[1]
            if variVal == '1':
                right = ['true', '1']
            else:
                right = ['false', '0']

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