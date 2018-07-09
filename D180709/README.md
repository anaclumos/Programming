# D180709.py

###### Developed by Sunghyun Cho on July 6th, 2018.

### Problem

Given a string of digits, generate all possible valid IP
address combinations.

IP addresses must follow the format A.B.C.D where
A, B, C, and D are numbers between 0 and 255.

### Example

```
Input : "2542540121"
output: 2 // [254.25.40.121] [254.254.0.121]
```

### Code

```python
class Node():
    def __init__(self, string, content, parent):
        self.content = content
        self.childs = []
        self.parent = parent
        if len(string)>0:
            self.childs.append(Node(string[1:], string[0:1], self))
        if len(string)>1 and int(string[0:2])<=99:
            self.childs.append(Node(string[2:], string[0:2], self))
        if len(string)>1 and int(string[0:3])<=255:
            self.childs.append(Node(string[3:], string[0:3], self))
        if len(self.childs)==0:
            answer = self.stringify()
            validIP = True
            if answer.count(".") != 3:
            	validIP = False
            for member in answer.split("."):
                if len(member)>1 and member.startswith("0"):
                    validIP = False
                    break;
            if validIP:
                array.append(answer)

    def stringify(self):
        string = self.content
        while(self.parent.content != ""):
            string = self.parent.content + "." + string
            self = self.parent
        return string

def remove_duplicates_in(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

array = []
node = Node(str(input("\nInput : ")), "", "")
answer = remove_duplicates_in(array)
print("Output:", str(len(answer)))

print()
print(answer)
print()
```
