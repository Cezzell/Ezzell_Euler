def isPrime(n):
	""" Checks for a prime number"""
	if n%2 == 0:
		return False
	p = 3
	while p < n**0.5 + 1:
		if n % p == 0:
			return False
		p += 2
	return True

def FindPrime():
	"""Iterates through odd numbers counting primes"""
	prime = 2
	count = 1
	hold = 3
	while count < 10001:
		if isPrime(hold):
			prime = hold
			count += 1
		hold += 2
	return prime

print(FindPrime() + "\n")
