'''
Developed by Sunghyun Cho on August 2nd.

첫 번째 줄에 조건의 개수를 나타내는 정수 n(1 ≤ n ≤ 100)이 주어진다. 다음 줄부터 n개의 줄에 걸쳐 문자열이 입력된다.
문자열은 각 프렌즈가 원하는 조건이 N~F=0과 같은 형태로 구성되어 있으며, 상세한 조건은 아래와 같다.

첫 번째 글자와 세 번째 글자는 A, C, F, J, M, N, R, T의 8개 중 하나이다.
각각 어피치, 콘, 프로도, 제이지, 무지, 네오, 라이언, 튜브를 의미한다.
첫 번째 글자는 조건을 제시한 프렌즈, 세 번째 글자는 상대방이다. 첫 번째 글자와 세 번째 글자는 항상 다르다.

두 번째 글자는 항상 ~이다.

네 번째 글자는 =, <, >의 3개 중 하나이다. 각각 같음, 미만, 초과를 의미한다.

다섯 번째 글자는 0 이상 6 이하의 정수의 문자형이며, 조건에 제시되는 간격을 의미한다.
이때 간격은 두 프렌즈 사이에 있는 다른 프렌즈의 수이다.
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

