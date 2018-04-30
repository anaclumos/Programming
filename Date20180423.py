'''
Developed by Sunghyun Cho on 23 April 2018.

If an integer n if given, find all
combinations of parentheses with
n "("s and n ")"s.
ex)
Input: 1
Output: ["()"]
Input: 2
Output: ["(())", "()()"]
Input: 3
Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]
'''

class Node():
	def __init__(self, ultimateInput, content):
		self.content = content
		self.childs = []
		if(len(content) == 2 * ultimateInput):
			array.append(self.content)
		if(len(content) < 2 * ultimateInput):
			if(self.opened() < ultimateInput):
				self.childs.append(Node(ultimateInput, content + '('))
			if(self.opened() > self.closed()):
				self.childs.append(Node(ultimateInput, content + ')'))
	def opened(self):
		return self.content.count('(')
	def closed(self):
		return self.content.count(')')

print("")
array = []
test = Node(int(input("Enter Number: ")), "")
print("total: ", len(array))
print(array)
print("")