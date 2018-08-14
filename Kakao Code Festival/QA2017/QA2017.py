'''
Solved by Sunghyun Cho on August 2nd.
'''
#----------------------------------------------------------------
# Node class definition.
class Node():
    def __init__(self, member, membersLeft, parent, conditions):
        self.member = member
        self.childs = []
        self.parent = parent
        self.membersLeft = membersLeft
        self.conditions = conditions

        # if any members are left in List "membersLeft", make a child node. 
        if len(self.membersLeft) != 0:
            for person in self.membersLeft:
                new = self.membersLeft[:]
                new.remove(person)
                self.childs.append(Node(person, new, self, self.conditions))
 
        # if no more member left, string-ify the node collection and check validity.
        if len(self.childs)==0:
            answer = self.stringify()
            # print(answer)
            validity = valid(answer, conditions)
            # print(validity, "\n")
            if validity:
                array.append(answer)

    # string-ifies the node collection.
    def stringify(self):
        string = self.member
        while(self.parent.member != ""):
            string = self.parent.member + string
            self = self.parent
        return string

#----------------------------------------------------------------
# Validity checking
def valid(string, conditions):
    validity = True
    for condition in conditions:
        target1 = condition[0]
        target2 = condition[2]

        loc1 = string.find(target1)
        loc2 = string.find(target2)

        validkey = condition[3]
        validvalue = int(condition[4])

        '''
        # Code for debugging
        print("target1", target1)
        print("target2", target2)
        print("loc1", loc1)
        print("loc2", loc2)
        print("validkey", validkey)
        print("validvalue", validvalue)
        '''

        if validkey == "<":
            if not abs(loc2-loc1)-1 < validvalue:
                return False

        if validkey == ">":
            if not abs(loc2-loc1)-1 > validvalue:
                return False

        if validkey == "=":
            if not abs(loc2-loc1)-1 == validvalue:
                return False
    return True
#----------------------------------------------------------------
# Main method
rotNum = int(input())
conditions = []
for x in range(rotNum):
    conditions.append(input())

# print(conditions)

array = []
everymember = ["A", "C", "F", "J", "M", "N", "R", "T"]

node = Node("", everymember, "", conditions)

# print(array)
print(str(len(array)))

