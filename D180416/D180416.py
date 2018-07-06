'''
Developed by Sunghyun Cho on April 16th, 2018.

Find the sum of all even fibonacci numbers smaller than the input.

Input : N = 12
Output: 10 // 0, 1, 1, 2, 3, 5, 8... but add only even numbers: 2 + 8 = 10.
'''

userInput = int(input("Input Number: "))

fibonacci = [0, 1]

while fibonacci[-1] < userInput:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

fibonacci = fibonacci[:-1]

sum = 0

for member in fibonacci:
    if member%2==0:
        sum += member

print(sum)