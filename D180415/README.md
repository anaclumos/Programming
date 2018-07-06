# D180415.py

###### Developed by Sunghyun Cho on April 15th, 2018.

### Problem

Reverse every word in String.

### Example

```
Input : 'ABC 123'
Output: 'CBA 321'

```

### Code

```python
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
```
