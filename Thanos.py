'''
Developed by Sunghyun Cho on May 27th, 2018.

Thanos snapped his finger, after collecting all six Infinity stones.
Are you alive?
'''

def snap(name):
    result = 1
    for character in name.lower():
        result += ord(character)
    return result%2==1

while(True):
    print("")
    name = input("Input Full Legal Name: ")
    print("")
    print(name, "survived." if snap(name) else "died.")