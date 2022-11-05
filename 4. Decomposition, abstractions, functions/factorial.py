# Iterative implementation of factorial
def factI(n):
	"""
	Assumes n and int > 0.
	Returns n!.
	"""
	result = 1
	while n > 1:
		result = result * n
		n -= 1
	return result

# Recursive implementation of factorial
def factR(n):
	"""
	Assumes n and int > 0.
	Returns n!.
	"""
	if n == 1:
		return n
	else:
		return n*factR(n-1)

print(factI(9))
print(factR(9))