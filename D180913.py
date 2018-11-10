def beautify(number):

	positive = True
	if number < 0:
		positive = False
		number = -1*number
	if number < 1000:
		if not positive:
			number = "-" + str(number)
		return number
	lastThree = str(number%1000).zfill(3)
	others = int(number/1000)
	if len(str(others)) > 3:
		b = beautify(others)
	else:
		b = str(others)
	if positive:
		return b + "," + lastThree
	else:
		return "-" + b + "," + lastThree

while True:
	print()
	userinput = int(input("Input : "))
	print("Output:", beautify(userinput))