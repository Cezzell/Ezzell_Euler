def isPrime(n):
	"""Finds out if a number is prime."""
	p = 3
	while p < n**0.5 + 1:
		if n % p == 0:
			return False
		p += 2
	if n%2 == 0:
		return False
	return True

def FindPrimes():
	"""Returns an array of primes under the threshold 2,000,000"""
	prime = [2]
	hold = 3
	while hold < 2000000:
		if isPrime(hold):
			prime.append(hold)
		hold += 2
	return prime

def SumPrimes():
	"""Sums the primes."""
	Primes = FindPrimes()
	return sum(Primes)

print(SumPrimes() + "\n")