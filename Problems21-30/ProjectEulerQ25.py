def Find1000Digit():
	"""Find the first 1000 digit fibbonaci number's index."""
	Last = 1
	Current = 1
	ind = 2
	while (Current <(10**999)):
		hold = Current
		Current = Current + Last
		Last = hold
		ind+=1
	return ind

print(Find1000Digit())