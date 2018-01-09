def FindPrime():
	"""Using Fermat's Litte theorem, we can find the prime closest to 1000."""
	Prime = 999
	primeflag = False
	while (not primeflag):
		primeflag = isprime(Prime)
		if primeflag:
			n = 1
			while pow(10, n, Prime) != 1:
				n += 1
			if Prime-1 == n:
				break
		Prime-=1
		primeflag = False
	return Prime


def isprime(x):
	if x % 2 == 0:
		return False
	for y in range(3,x**1/2, 2):
		if x % y == 0:
			return False
	return True


print(FindPrime())