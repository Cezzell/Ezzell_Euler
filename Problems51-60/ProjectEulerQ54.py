""" Helper  Functions to  assist with deciphering hands"""
def RoyalFlush(Value, Suit):
	"""
	Checking for a royal flush hand. Checks all suits are the same
	then checks that there is one each of A, K, Q, J, T.
	"""
	
	# A useful structure for checking values
	CheckValues = ['A', 'K', 'Q', 'J', 'T']

	# Check that all suits are the same
	CheckSuit = Suit[0]
	for suit in Suit:
		if CheckSuit != suit:
			return False

	# Check that all the values are accounted for
	for value in CheckValues:
		if value not in Value:
			return False
	return True

def StraightFlush(Value, Suit):
	"""
	Checking for a Straight Flush hand. Similar to royal flush, but checks
	each starting value and the following values.
	"""

	# A useful structure for  checking values
	CheckValues =['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K' ]
	
	# Check that all suits are the same
	CheckSuit = Suit[0]
	for suit in Suit:
		if CheckSuit != suit:
			return False

	#Check that values are in order 
	for x in range(9):
		if CheckValues[x] in Value:
			for y in range(1,5):
				if CheckValues[x+y] not in Value:
					return False
			return True

def FourOfAKind(Value, Suit):
	"""
	Checking for Four of a kind, only checks first two values since 4 cards
	are needed for 4 of a kind.	
	"""
	flag = False
	hold = 'X'

	#Checks first two values
	for val in Value[:2]:
		#iterates through all values
		for y in Value:
			# value matches
			if val == y:
				continue
			# value does not match, but we can consider this the high card
			else if val != y and hold == 'X' :
				hold = y
			# value does not match, and we already considered a high card
			else:
				Flag = True
		# If we didn't fail return True and high value
		if !Flag:
			return (True, hold)
	# No four of a kind
	return (False, -1)

def




P1WinCounter = 0
"""Simple File Handler so that we can read in the poker hands. """
File = open('poker.txt', 'r')

"""Now we read in line at a time and parse hands"""

for line in File.readlines():
	# Create hands for both players
	Cards = line.split(" ")
	P1Hand = Cards[:5]
	P1Values = [P1Hand[x][0] for x in P1Hand]
	P1Suits = [P1Hand[x][1] for x in P1Hand]
	P1HandScore = 100

	P2Hand = Cards[5:]
	P2Values = [P2Hand[x][0] for x in P2Hand]
	P1Suits = [P2Hand[x][1] for x in P2Hand]
	P2HandScore = 100


