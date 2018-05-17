'''
Developed by Sunghyun Cho on 5 April 2018.

Every alphabet can be written in number like following.
a = 1, b = 2, ... y = 25, z = 26.
if a string with integer values inside is given,
find out how many interpretations can be made with
the combinations of the string characters as alpabet.

예)
input: "111"
output: 3 // "aaa", "ak", "ka"
'''

class Tree():
    def __init__(self, string, content, parent):
        self.content = content
        self.childs = []
        self.parent = parent
        if len(string)>0:
            self.childs.append(Tree(string[1:], string[0], self))
        if len(string)>1 and int(string[0:2])<=26:
            self.childs.append(Tree(string[2:], string[0:2], self))
        if len(self.childs)==0 :
            array.append(self.stringify())

    def stringify(self):
        string = chr(int(self.content)+96)
        while(self.parent.content != ""):
            string = (chr(int(self.parent.content)+96)) + string
            self = self.parent
        return string

array = []
tree = Tree(str(input("Input Number: ")), "", "")
print("answer: " + str(len(array)))
print(array)