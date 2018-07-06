# D180503.py

###### Developed by Sunghyun Cho on May 3rd, 2018.

### Problem

Make a Function that checks one string is a substring of another string.

### Code

```python
def isSubstring(string1, string2):
    array1 = list(string1)
    array2 = list(string2)
    if len(string1) < len(string2):
        return False
    for x in range(int(len(string1))):
        for y in range(int(len(string2))):
            if len(string1)<x+y:
                if array1[x+y] != array2[y]:
                    continue
            return True
    return False

print("")
in1 = input("Input 1: ")
in2 = input("Input 2: ")
print("Output :", isSubstring(in1, in2))
print("")
```
