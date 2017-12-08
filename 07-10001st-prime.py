"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
	What is the 10,001st prime number?"""

NTH = 10001
primes = [2]
numbertocheck = 3

while len(primes) < NTH:
	composite = False
	for i in primes:
		if numbertocheck % i == 0:
			composite = True
			break
		else:
			pass
	if not composite:
		primes.append(numbertocheck)
	else:
		pass
	numbertocheck += 1

primes[-1]
