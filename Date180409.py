'''
Developed by Sunghyun Cho on April 9th, 2018.

if an int array is given, find the maximum sum of continuously increasing set of numbers.
Time Complexity: O(n).

Input: [-1, 3, -1, 5]
Output: 7 // 3 + (-1) + 5

Input: [-5, -3, -1]
Output: -1 // -1

Input: [2, 4, -2, -3, 8]
Output: 9 // 2 + 4 + (-2) + (-3) + 8
'''

def findBiggestSum(array):
    print(array)
    maxSum = array[0]
    current = array[0]
    for x in range(1,len(array)):
        if array[x] > current and current < 0:
            current = array[x]
        else:
            current += array[x]
        if maxSum < current:
            maxSum = current
    return maxSum

array = [-1, 3, -1, 5]
print(findBiggestSum(array))
