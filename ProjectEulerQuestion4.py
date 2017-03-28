def FindPalindrome():
	"""Finds the largest Palindrome made from two 3 digit numbers"""
	Palindromes = []
	for x in range(100,1000):
		for y in range(100,1000):
			hold = x*y
			string = str(hold)
			if string == string[len(string)::-1]:
				Palindromes.append(hold)
	return max(Palindromes)

print(FindPalindrome())