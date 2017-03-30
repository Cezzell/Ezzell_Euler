def fact(num):
	res = 1
	for x in range(2, num):
		res = res * x
	return res

def FactDigitSum():

	Number = fact(100)
	Sum = 0

	while Number:
		Sum += Number % 10
		Number = Number // 10

	return Sum

print FactDigitSum()