def FindSpiralSum():
	"""Find the spiral sum described through iteration."""

	Size = 1
	s = 1
	step = 2
	hold = 1
	while Size < 1001:
		s = s +(hold +step)
		s = s +(hold +2*step)
		s = s +(hold +3*step)
		s = s +(hold +4*step)
		Size+=2
		hold = hold + 4*step
		step+=2
	return s

print(FindSpiralSum())