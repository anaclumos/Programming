rotnum = input()
wordNum = input().split()

answer = ""

for member in wordNum:
	answer = answer + str(chr(int(member)))
	answer = answer + " "

answer = answer[:-1]

print(answer)
