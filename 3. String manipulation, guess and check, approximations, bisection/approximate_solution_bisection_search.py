# Approximate solution to square root
x = -25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
	ans += step
	numGuesses += 1

print(f"numGuesses = {numGuesses}.")

if abs(ans**2 - x) >= epsilon:
	print("Failed on square root of {x}.")
else:
	print(f"{ans} is close to square root of {x}.\n")

# Bisection search method to finding square root.
# Divides the search space by half at each step. Faster.
x = -25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
	print(f"low = {low}, high = {high}, ans = {ans}.")
	numGuesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0

print(f"numGuesses = {numGuesses}.")
print(f"{ans} is close to square root of {x}.")