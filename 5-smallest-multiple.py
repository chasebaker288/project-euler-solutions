"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
	
UPTO = 20
factors = list(range(1, UPTO+1))
result = 1

for i in range(2, UPTO):  # Looks at previous entries, and removes any previously 'counted' factors.
	for j in factors[:i]:
		if factors[i] % j == 0:
			factors[i] /= j
		else:
			pass

for i in factors:
	result *= i

int(result)
