def LetterCounts():
	count = 0

	#for one to nine
	count += 36
	#for ten to nineteen
	count += 70
	#for twenty to twenty nine
	count = count + 60 + 36
	#for thirty to thirty nine
	count = count + 60 + 36
	#for forty to forty nine
	count += 86
	#for fifty to fifty nine
	count += 86
	#for sixty to sixty nine
	count += 86
	#for seventy to seventy nine
	count += 106
	#for eighty to eighty nine
	count += 96
	#for ninety to ninety nine
	count += 96
	#for one hundred to one hundred and ninenty nine
	count += 1000 #one hundred
	count += 297 #and
	count += 854 #numbers 1 to 99
	#for two hundred to two hundred and ninenty nine
	count += 1000
	count += 297
	count += 854
	#for three hundred etc...
	count += 1200
	count += 297
	count += 854
	#for four hundred
	count += 1100
	count += 297
	count += 854
	#for five hundred
	count += 1100
	count += 297
	count += 854
	#for six hundred
	count += 1000
	count += 297
	count += 854
	#for seven hundred
	count += 1200
	count += 297
	count += 854
	#for eight hundred
	count += 1200
	count += 297
	count += 854
	#for nine hundred
	count += 1100
	count += 297
	count += 854
	#for one thousand
	count += 11

	return count

print (LetterCounts())
