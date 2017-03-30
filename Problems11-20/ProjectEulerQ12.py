""" The sum of the first N numbers is (n(n+1))/2 so we only need to find the 
new divisors of n+1"""

def NumberOfDivisors(Number):
	"""Helper Function to find the number of Divisors"""
	if Number % 2 == 0:
		Number = Number/2
	Factors = 1
	while Number % 2 == 0:
		Factors += 1
		Number = Number/2
	Counter = 3
	while Number != 1:
		mult = 0
		while Number % Counter == 0:
			mult += 1
			Number = Number/Counter
		Factors = Factors * (mult + 1)
		Counter += 2
	return Factors


def FindTriangleNumber():
	Number = 1
	Lfact = NumberOfDivisors(Number)
	Rfact = NumberOfDivisors(Number+1)
	while Lfact*Rfact < 500:
		Number += 1
		Lfact = NumberOfDivisors(Number)
		Rfact = NumberOfDivisors(Number+1)
	return Number *(Number +1)/2

print(FindTriangleNumber())