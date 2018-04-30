'''
Developed by Sunghyun Cho on 15 April 2018.

if an integer array is given, make an array with every element become a multiplication of the other array memebers.
No devisions, Time Complexity O(n).
ex) [1, 2, 3, 4, 5] - [120, 60, 40, 30, 24]
'''

array = [1, 2, 3, 4, 5]
result = []
for element in array:
	result.append(1)

for a in range(len(array)):
	for b in range(len(array)):
		if a==b:
			continue
		else:
			result[b] *= array[a]

print(result)