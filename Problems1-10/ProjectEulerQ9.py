def FindTriplet():
	"""Finds a Triplet through iteration."""
	for x in range(1, 500):
		for y in range(1, 500):
			z = 1000-x-y
			if (x**2 + y**2) == (z**2):
				return(x, y, z)

print(FindTriplet() + "\n")