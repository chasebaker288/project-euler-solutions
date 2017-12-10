"""A palindromic number reads the same both ways.
	The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
	Find the largest palindrome made from the product of two 3-digit numbers."""

NUMBEROFDIGITS = 3
UPPERLIMIT = int(pow(10, NUMBEROFDIGITS))
result = 9  # In case we tested 1-digit number for some reason
test = 0

if NUMBEROFDIGITS > 1:
	for i in range(int(UPPERLIMIT/10), UPPERLIMIT):  # There's probably a way to reduce this range by choosing a higher starting point, but I haven't been able to mathematically prove this, let alone where such a point would be.
		for j in range(i, UPPERLIMIT):  # No sense in trying A*B if B*A didn't work.
			if str(i*j) == str(i*j)[::-1]:
				test = i*j
				if test > result:
					result = test
				else:
					pass
			else:
				pass
else:
	pass

print(result)
