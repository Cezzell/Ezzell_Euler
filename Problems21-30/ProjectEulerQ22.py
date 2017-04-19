File = open('names.txt', 'r')
string = File.read()
string = string.split(",")

string =[x.translate(None, '"') for x in string]
names = sorted(string)


def FindTotalScore(names):
	"""Takes in every name and adds there values and multiplies by position."""
	scores =[]
	final = 0
	for x in range(len(names)):
		scores.append(sum([(ord(y)-64)%32for y in names[x]]))
	for x in range(len(scores)):
		final += (x+1)*scores[x]
	return final

print(FindTotalScore(names))
