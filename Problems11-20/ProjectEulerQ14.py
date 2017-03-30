

def FindLongCollatz():
	results = []
	for x in range(500000,1000001):
		y = x 
		count = 0
		while y != 1:
			if y % 2 == 0:
				y = y/2
				count += 1
			else:
				y = (3*y) + 1
				count += 1
		results.append(count)
	ret = 500000+ results.index(max(results))
	return ret


print FindLongCollatz()
