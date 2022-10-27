# numXs = int(input("How many times should I print the letter X?"))
# toPrint = ''
# counter = 0
# while counter < numXs:
# 	toPrint += 'X'
# 	counter += 1
# print(toPrint)

# # Find a positive integer that is divisible by both 11 and 12
# x = 1
# while True:
# 	if x%11 == 0 and x%12 == 0:
# 		break
# 	x += 1
# print(f"{x} is divisible by 11 and 12")

# Asks user to input 10 integers and prints largest odd number that was entered
integers = []
counter = 0

while counter < 10:
	integer = int(input("Choose an integer."))
	if integer % 2 != 0:
		integers.append(integer)
	counter += 1

if len(integers) == 0:
	print("No integers were chosen.")
else: 
	print(f"The greatest odd integer entered is {max(integers)}.")