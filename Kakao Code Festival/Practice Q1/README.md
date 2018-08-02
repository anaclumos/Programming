# Kakao Practice Q1.py

###### Developed by Sunghyun Cho on August 2nd, 2018.

### Problem

가을을 맞아 카카오프렌즈는 단체로 소풍을 떠났다. 즐거운 시간을 보내고 마지막에 단체사진을 찍기 위해 카메라 앞에 일렬로 나란히 섰다. 그런데 각자가 원하는 배치가 모두 달라 어떤 순서로 설지 정하는데 시간이 오래 걸렸다. 네오는 프로도와 나란히 서기를 원했고, 튜브가 뿜은 불을 맞은 적이 있던 라이언은 튜브에게서 적어도 세 칸 이상 떨어져서 서기를 원했다. 사진을 찍고 나서 돌아오는 길에, 무지는 모두가 원하는 조건을 만족하면서도 다르게 서는 방법이 있지 않았을까 생각해보게 되었다. 각 프렌즈가 원하는 조건을 입력으로 받았을 때 모든 조건을 만족할 수 있도록 서는 경우의 수를 계산하는 프로그램을 작성해보자.

첫 번째 줄에 조건의 개수를 나타내는 정수 n(1 ≤ n ≤ 100)이 주어진다. 다음 줄부터 n개의 줄에 걸쳐 문자열이 입력된다.
문자열은 각 프렌즈가 원하는 조건이 N~F=0과 같은 형태로 구성되어 있으며, 상세한 조건은 아래와 같다.

첫 번째 글자와 세 번째 글자는 A, C, F, J, M, N, R, T의 8개 중 하나이다.
각각 어피치, 콘, 프로도, 제이지, 무지, 네오, 라이언, 튜브를 의미한다.
첫 번째 글자는 조건을 제시한 프렌즈, 세 번째 글자는 상대방이다. 첫 번째 글자와 세 번째 글자는 항상 다르다.

두 번째 글자는 항상 ~이다.

네 번째 글자는 =, <, >의 3개 중 하나이다. 각각 같음, 미만, 초과를 의미한다.

다섯 번째 글자는 0 이상 6 이하의 정수의 문자형이며, 조건에 제시되는 간격을 의미한다.
이때 간격은 두 프렌즈 사이에 있는 다른 프렌즈의 수이다.

### Example


|Input|Output|
|---|---|
|```2```<br>```N~F=0```<br>```R~T>2```|3648|
|```2```<br>```M~C<2```<br>```C~M>1```|0|

첫 번째 예제는 문제에 설명된 바와 같이, 네오는 프로도와의 간격이 0이기를 원하고 라이언은 튜브와의 간격이 2보다 크기를 원하는 상황이다.

두 번째 예제는 무지가 콘과의 간격이 2보다 작기를 원하고, 반대로 콘은 무지와의 간격이 1보다 크기를 원하는 상황이다. 이는 동시에 만족할 수 없는 조건이므로 경우의 수는 0이다.

### Code

```python
'''
Developed by Sunghyun Cho on August 2nd.
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
```
