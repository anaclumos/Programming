def enter(n):
	[print() for x in range(n)]

def drawLeaf(n):
	for x in range(1, n+1):
		print((" "  * (27-x)) + ("* " * x))

enter(8)

drawLeaf(3)
drawLeaf(5)
drawLeaf(7)

enter(2)

print(" "  * 17, end='')
print("Merry Christmas...?")

enter(8)