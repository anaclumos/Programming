import math
'''
Developed by Sunghyun Cho on April 30th, 2018

If an integer is given, find if it is a palindrome.
Do not change the integer in string form.
ex)
Input : 12345
Output: False
Input : -101
Output: False
Input : 11111
Output: True
Input : 12421
﻿Output: True
'''

def checkPalindrome(number):
    if number < 0:
        return False
    else:
        dgts = int(math.log10(number))
        for x in range(int(dgts/2)):
            if get(number,x,dgts)!=get(number,dgts-x,dgts):
                return False
        return True

def get(number, nth, digits):
    return int(number/10**(digits - nth))%10

print("")
print("Output:", checkPalindrome(int(input("Input : "))))
print("")