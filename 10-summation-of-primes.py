"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	Find the sum of all the primes below two million."""

BELOW = 2000000

checklist = list(range(2, BELOW))

for i in range(2, len(checklist)):  # Clears Sieve of Eratosthenes.
	for j in [x for x in checklist if x > i]:
		if j % i == 0:
			checklist.remove(j)

print(sum(checklist))
