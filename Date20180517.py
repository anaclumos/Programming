'''
Developed by Sunghyun Cho on May 17th, 2018.

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps,
merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''

def mergeThese(array1, array2):
    result = []
    result.append(array1[0] if array1[0] <= array2[0] else array2[0])
    result.append(array1[1] if array1[1] >= array2[1] else array2[1])
    return result

def theseCoincide(array1, array2):
    conditionA = array1[0] >= array2[1] and array1[1] <= array2[0]
    conditionB = array1[1] >= array2[0] and array1[0] <= array2[1]
    return conditionA or conditionB 

line = input('\nEnter array: ').split()
array = []
for x in range(int(len(line)/2)):
    array.append([int(line[2*x]), int(line[2*x+1])])

print('\nInput :', array)
# Printing input
output = [array[0]]
for x in range(len(array)):
    nothingCoincide = True

    for y in range(len(output)):

        if theseCoincide(array[x], output[y]):
            nothingCoincide = False
            output[y] = mergeThese(array[x], output[y])

    if(nothingCoincide):
        output.append(array[x])

print('Output:', output, '\n')
# Printing Output

