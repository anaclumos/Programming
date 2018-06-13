'''
Developed by Sunghyun Cho on April 27th, 2018.

There is an integer array
with every element appearing twice.
If we randomly delete two different elements,
find those two elements.
'''
line = input("\nEnter Array: ")
userInput = [int(x) for x in line.split()]

print("\nInput: ", userInput)
result = []

for element in userInput:
    if element not in result:
        result.append(element)
        continue
    if element in result:
        result.remove(element)
        continue

print("\nResult: ", result, "\n")