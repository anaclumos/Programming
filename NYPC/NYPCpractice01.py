nm = input().split()
n = int(nm[0])
m = int(nm[1])

data = []

for x in range(n):
	data.extend(input().split())

counter = 0

for member in data:
	if member == "NEXON":
		counter = counter + 1

print(counter)