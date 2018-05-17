'''
Developed by Sunghyun Cho on 15 April 2018.

Reverse every word in String.
ex) 'ABC 123' - 'CBA 321'
'''

def reverse(wordList):
    result = []
    for word in wordList:
        string = ""
        for alphabet in word:
            string = alphabet + string
        result.append(string)
    return result


userInput = input('Input String: ')

wordList = userInput.split()
reversedList = reverse(wordList)
result = ""
for word in reversedList:
    result += word
    result += " "
result = result[:-1]
print(result)