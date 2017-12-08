"""The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?"""

TARGETNUMBER = 600851475143
factors = []
primesfound = []
count = 0

for x in range(1, int(pow(TARGETNUMBER, 0.5) + 1)):  # By only checking up to the square root, the workload is cut drastically while still finding every factor.
	if TARGETNUMBER % x == 0:
		factors.append(x)
		factors.append(int(num/x))  # If x is a factor of z, then z/x must also be a factor of z, hence getting 2 factors at once.

factors.sort()

for x in factors:
	count += 1
	if pow(x, 0.5) != int(pow(x, 0.5)):  # If the square root is an integer, then the square root is a factor and therefore the number can't be prime, so we can narrow our search to cases where the square root is not an integer.
		primetest = []
		for y in range(1, int(pow(x, 0.5))):
			if x % y == 0:
				primetest.append(y)
				primetest.append(int(x/y))
				if len(primetest) >= 3:  # If it doesn't have EXACTLY two factors (itself and 1), then it can't be prime.
					break
				else:
					pass
			else:
				pass
		if len(primetest) == 2:  # See previous comment
			primesfound.append(max(primetest))  # The only factor we care about is the prime, which is the larger of the two.
		else:
			pass
	else:
		pass

max(primesfound)
