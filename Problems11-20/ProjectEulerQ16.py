def SumDigits():
	num = str(2**1000)
	num = list(num)
	nums = [int(x) for x in num]
	return sum(nums)


print(SumDigits())
