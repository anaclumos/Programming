'''
Developed by Sunghyun Cho on May 5th, 2018.

Google University Student Internship Interview Question from Mailprogramming.com

If an array and integer k is given,
pull the array by k.

ex:
Input : [1, 2, 3, 4, 5] / K = 2
Output: [3, 4, 5, 1, 2]

Input : [0, 1, 2, 3, 4] / K = 1
Output: [1, 2, 3, 4, 0]
'''
def pull(array, k):
    result = []
    r = len(array)
    for x in range(r):
        result.append(array[(x+k)%r])
    return result

line = input("\nEnter Array: ")
array = [int(x) for x in line.split()]

k = int(input("Enter K    : "))

print("")
print(pull(array, k))
print("")