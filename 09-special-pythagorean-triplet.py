"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a**2 + b**2 = c**2.
	For example, 32 + 42 = 9 + 16 = 25 = 52.
	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc."""

SUM = 1000

finished = False
result = 0

for a in range(1, SUM):  # Wish I knew a way to cut this range down that would guarantee I wouldn't miss any viable results. Starting at (SUM / 6) worked during testing, but I have no mathematical proof that it's a 'safe' starting point.
	if finished:
		break
	else:
		for b in range(a + 1, SUM):  # Same here. (a * 1.1) worked as well, but again, I have no guarantee that it's a safe starting point.
			if finished:
				break
			else:
				for c in [x for x in range(b, SUM) if a+b+x == SUM]:  # Checks pythagorean property only if the sum property is met.
					if pow(a, 2) + pow(b, 2) == pow(c, 2):
						finished = True
						result = a*b*c
						break  # The problem states that there is only one answer, so it stops once a result is found instead of testing for other possible answers.

result
