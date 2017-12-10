"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
	The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000."""

factor1 = 3
factor2 = 5
upperlimit = 1000

print(sum([x for x in range(1, upperlimit) if x % factor1 == 0 or x % factor2 == 0]))
