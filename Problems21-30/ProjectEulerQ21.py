def SumFactors(x):
	"""Factors and sums"""
	s = 0
	for y in range(1, x):
		if x%y == 0:
			s+=y
	return s

def SumAmicables():
	"""Sums the Amicable Numbers under 10000"""
	Amicables = [SumFactors(y) for y in range(1,10001)]
	s = 0
	for x in range(10000):
		hold = Amicables[x]
		if hold <= 10000 and Amicables[hold-1] == x+1 and x+1 < hold:
				s+=hold
				s = s+x+1
	return s


print(SumAmicables())