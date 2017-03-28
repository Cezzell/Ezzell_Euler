def isPrime(n):
	p = 3
	while p < n**0.5 + 1:
		if n % p == 0:
			return False
		p += 2
	if n%2 == 0:
		return False
	return True

def FindPrimes():
	prime = [2]
	hold = 3
	while hold < 2000000:
		if isPrime(hold):
			prime.append(hold)
		hold += 2
	return prime

def SumPrimes():
	Primes = FindPrimes()
	return sum(Primes)

print(SumPrimes())