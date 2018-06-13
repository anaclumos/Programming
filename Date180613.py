'''
Developed by Sunghyun Cho on June 13th, 2018.

If a string is give, find the length of the longest substring without duplicate character.

ex)
Input: “aabcbcbc”
Output: 3 // “abc”

Input: “aaaaaaaa”
Output: 1 // “a”

Input: “abbbcedd”
﻿Output: 4 // “bced”
'''

def findLongestSubstring(line):
    longest = ""
    string = ""
    length = len(line)
    for x in range(length):
        string = line[x]
        for y in range(x+1, length):
            if line[y] not in string:
                string = string + line[y]
            else:
                if len(longest) < len(string):
                    longest = string
                else:
                    string = ""
                break
    print("Longest substring is \"", longest, "\"")
    return len(longest)

line = input("Input : ")
result = findLongestSubstring(line)
print("Output:", result)