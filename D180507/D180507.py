'''
Developed by Sunghyun Cho on May 7th, 2018.

If an integer array & target number is given,
find the two indices that
their sum is the target number.
Time Complexity O(n).
ex)
Input : [2, 5, 6, 1, 10], target 8
Output: [0, 2] // array[0] + array[2] = 8
'''

def search(array, target):
    l = len(array)
    for x in range(l-1):
        for y in range(x, l):
            if array[x]+array[y] == target:
                return [x, y]
    return "No Answer"

line = input("\nEnter array  : ")
array = [int(x) for x in line.split()]

target = int(input("Enter target : "))

print("")
print(search(array, target))
print("")
# Time Complexity currently O(n^2).
# Will be fixed...