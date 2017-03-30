def FindSundays():
	Months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	Count = 0
	Week = 2

	for x in range(1901,2001):
		if x % 4 == 0:
			Months[1] = 29
		else:
			Months[1] = 28
		for y in range(12):
			Week = (Week +Months[y]) % 7
			if Week == 0:
				Count += 1
	return Count


print FindSundays()
