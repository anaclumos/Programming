# D180531.py

###### Developed by Sunghyun Cho on May 31st, 2018.

### Problem

Given a collection of intervals, merge all overlapping intervals.

### Example

```
Input: [10, 5, 4, 3, -1]
Output: 5

Input: [3, 3, 3]
Output: Does not exist.
```

### Code

```python
class Queue:

    def __init__(self):
        self.one = None
        self.two = None

    def add(self, integer):
        if self.one is None and self.two is None:
            self.one = integer
        elif integer > self.one and self.two is None:
            self.two = self.one
            self.one = integer
        elif self.one > integer and self.two is None:
            self.two = integer
        elif self.one < integer:
            self.two = self.one
            self.one = integer
        elif self.one > integer and integer > self.two:
            self.two = integer

    def get(self):
        if self.one == self.two or self.two is None:
            return("Does not exist.")
        else:
            return(self.two)

queue = Queue()
while True:
    queue.add(int(input("\nInput : ")))
    print("Output:", queue.get(), "\n")
```
