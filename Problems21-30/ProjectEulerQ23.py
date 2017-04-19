def FindAbundentSums():
	"""Creates a list of all the sums less than the target value"""
	Abun = []
	Sums = [False for x in range(28123)]

	for x in range(1,28112):
		s = SumFactorBadly(x)
		if (s > (x+1)):
			Abun.append(x)
	for x in range(len(Abun)):
		for y in range(x, len(Abun)):
			val = Abun[x]+Abun[y]
			if val < 28123:
				Sums[val] = True
	return Sums





def SumFactorBadly(n):
	"""Factors easily, but inneficiently"""
	s = 0
	for x in range(1,n):
		if n%x == 0:
			s+=x
	return s


def FindLastSum(sums):
	"""Finds the final sum in the problem"""
	Last = 0
	for x in range(len(sums)):
		if sums[x] == False:
			Last+=(x)

	return Last

print(FindLastSum(FindAbundentSums()))