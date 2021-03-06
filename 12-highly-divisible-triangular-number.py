#===============================
#	WORK IN PROGRESS
#===============================

"""The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
		1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
	Let us list the factors of the first seven triangle numbers:
		 1: 1
		 3: 1,3
		 6: 1,2,3,6
		10: 1,2,5,10
		15: 1,3,5,15
		21: 1,3,7,21
		28: 1,2,4,7,14,28
	We can see that 28 is the first triangle number to have over five divisors.
	What is the value of the first triangle number to have over five hundred divisors?"""

import time  # For testing


def triangify(integer):
	return sum(range(1, integer+1))


def numberoffactors(integer):
	return len([a for a in range(1, integer+1) if integer % a == 0])


startingpoint = 2500
numbertocheck = triangify(startingpoint)
print("Triangified")  # For testing
NUMBEROFDIVISORS = 500


time.clock()  # For testing

while numberoffactors(numbertocheck) < NUMBEROFDIVISORS:
	startingpoint += 1
	numbertocheck += startingpoint
	if startingpoint % 500 == 0:  # For testing
		print("T =	" + str(int(time.clock())) + ",	Just checked " + str(numbertocheck) + "	(" + str(startingpoint) + ")")  # For testing

print("DONE!\n\n\n")  # For testing
print(str(numbertocheck) + "	" + str(startingpoint))  # For testing

