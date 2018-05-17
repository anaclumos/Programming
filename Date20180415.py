'''
Developed by Sunghyun Cho on 15 April 2018.

if an integer array is given, make an array with every element become a multiplication of the other array memebers.
No devisions, Time Complexity O(n).
ex) [1, 2, 3, 4, 5] - [120, 60, 40, 30, 24]
'''

array = [1, 2, 3, 4, 5]

result1 = []
result2 = []
final = []
for member in array:
    result1.append(1)
    result2.append(1)

for x in range(1, len(array)):
    result1[x] = result1[x-1] * array[x-1]

for x in range(len(array)-2, -1, -1):
    result2[x] = result2[x+1] * array[x+1]

for x in range(len(array)):
    final.append(result1[x]*result2[x])

print(final)