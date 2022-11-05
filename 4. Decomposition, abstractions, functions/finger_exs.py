"""

Write a function isIn that accepts two strings as arguments
and returns True if either string occurs anywhere in the
other, and False otherwise.

"""

def isIn(argument1, argument2):
	if argument1 in argument2:
		print(f"{argument1} appears in {argument2}.")
	elif argument2 in argument1:
		print(f"{argument2} appears in {argument1}.")
	else:
		print("The strings have notihing in common.")

isIn('Sustainable Energy', 'Sustainable')