# Ask the user for and integer and prints the root and power that equals that integer
x = int(input("Enter an integer: "))
ans = False

def power(a,b):
	return a ** b

for root in range(1,abs(x)+1):
	for pwr in range(2,7):
		if power(root,pwr) == x:
			break
	if power(root,pwr) == x:
		ans = True
		break

if ans == True:
	print(f"{root}ˆ{pwr} equals {x}.")
else:
	print("There is no root/power pair that equals your integer in the given range.")