"""The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?"""

TARGETNUMBER = 600851475143


def isprime(integer):
	if not isinstance(integer, int):
		return False
	elif integer < 1:
		return False
	elif integer in [2, 3]:
		return True
	else:
		output = True
		for x in range(2, int(pow(integer, 0.5))):  # We only need to search up to the square root, cutting the workload from O(N) to O(N**(1/2)).
			if integer % x == 0:  # If we find any factors (other than our original number and 1), then the number can't be prime.
				output = False
				break
			else:
				pass
		return output


print(max([x for x in sum([[x, int(TARGETNUMBER/x)] for x in range(1, int(pow(TARGETNUMBER, 0.5))) if TARGETNUMBER % x == 0], []) if isprime(x)]))
