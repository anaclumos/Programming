def snap(name):
    result = 1
    for character in name.lower():
        result += ord(character)
    return result%2==1

while(True):
    print("")
    name = input("Input name: ")
    print(name, "survived" if snap(name) else "died")
    print("")