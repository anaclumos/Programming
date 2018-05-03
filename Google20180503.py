'''
Developed by Sunghyun Cho on 3 May 2018

Google Interview Question from Coderbyte.com!

Using the Python language, have the function ArrayAddition(arr)
take the array of numbers stored in arr and return the string
true if any combination of numbers in the array can be added up
to equal the largest number in the array, otherwise return the
string false. For example: if arr contains [4, 6, 23, 10, 1, 3]
the output should return true because 4 + 6 + 10 + 3 = 23.
The array will not be empty, will not contain all the same elements,
and may contain negative numbers. 

Sample Test Cases

Input:5,7,16,1,2
Output:"false"

Input:3,5,-1,8,12
Output:"true"
'''

def ArrayAddition(arr):
    arr.sort()
    largest = arr[-1]
    for x in range(2**(len(arr)-1)-1):
        sum = 0
        boolArray = binaryToArray(x, len(arr)-1)
        for y in range(len(boolArray)):
            if boolArray[y]:
                sum += arr[y]
        if sum == largest:
            return True
    return False

def binaryToArray(value, length):
    b = bin(value)
    s = str(b)
    s = s[2:]
    l = list(s)
    resultArray = []
    for x in range(length-len(l)):
        resultArray.append(False)
    for member in l:
        if member == "0":
            resultArray.append(False)
        else:
            resultArray.append(True)
    return resultArray

# Coderbyte Test Unit
'''
# keep this function call here
print(ArrayAddition(raw_input()))
'''

arr1 = [5,7,16,1,2]
arr2 = [3,5,-1,8,12]

print(arr1)
print(ArrayAddition(arr1))

print(arr2)
print(ArrayAddition(arr2))




  