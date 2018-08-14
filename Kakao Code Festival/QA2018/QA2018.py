'''
Solved by Sunghyun Cho on August 14th, 2018.
'''
def firstContest(x):
	if x == 0:
		return 0
	elif x == 1:
		return 5000000
	elif x <= 3:
		return 3000000
	elif x <= 6:
		return 2000000
	elif x <= 10:
		return 500000
	elif x <= 15:
		return 300000
	elif x <= 21:
		return 100000
	else:
		return 0

def secondContest(x):
	if x == 0:
		return 0
	elif x == 1:
		return 5120000
	elif x <= 3:
		return 2560000
	elif x <= 7:
		return 1280000
	elif x <= 15:
		return 640000
	elif x <= 31:
		return 320000
	else:
		return 0

rotnum = int(input())
initialArray = []
for x in range(rotnum):
	initialArray.append(input().split())
for member in initialArray:
	print(firstContest(int(member[0])) + secondContest(int(member[1])))

