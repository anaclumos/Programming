def firstWin(a, b):
	if a == "R":
		if b == "R":
			return 0
		if b == "S":
			return 1
		if b == "P":
			return -1
	if a == "S":
		if b == "R":
			return -1
		if b == "S":
			return 0
		if b == "P":
			return 1
	if a == "P":
		if b == "R":
			return 1
		if b == "S":
			return -1
		if b == "P":
			return 0

while True:
	p1 = input()
	if p1 == "E":
		break 
	p2 = input()

	trials = len(p1)
	won1 = 0
	won2 = 0
	for n in range(trials):
		if firstWin(p1[n], p2[n]) == 1:
			won1 += 1
		if firstWin(p1[n], p2[n]) == -1:
			won2 += 1
	print("P1: "+str(won1))
	print("P2: "+str(won2))