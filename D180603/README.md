# D180603.py

###### Developed by Sunghyun Cho on June 3rd, 2018.

### Problem

If an int array is given, keep the integer order and move all 0 to the right end.

### Example

```
Input : [0, 5, 0, 3, -1]
Output: [5, 3, -1, 0, 0]

Input : [3, 0, 3]
﻿Output: [3, 3, 0]
```

### Code

```python
def moveZerosIn(array):
	for x in range(len(array)):
		if array[x] == 0:
			array.pop(x)
			array.append(0)

line = list(int(x) for x in input("\nInput Array: ").split())

print("\nInput :",line)
moveZerosIn(line)
print("Output:",line,"\n")
```
