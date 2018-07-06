'''
Developed by Sunghyun Cho on July 6th, 2018.

If two strings are given, check if two string can be encoded one-to-one.

ex)
Input : “EGG”, “FOO”
Output: True // E->F, G->O
Input : “ABBCD”, “APPLE”
Output: True // A->A, B->P, C->L, D->E
Input : “AAB”, “FOO”
Output: False
'''

print()
ds = input("Decoded: ")
es = input("Encoded: ")
print()

def checkPasscode(ds, es):
    if len(ds) != len(es):
        return False
    dic = {}
    
    for x in range(len(ds)):
            if ds[x] in dic and es[x] == dic[ds[x]]:
                continue
            if ds[x] not in dic and es[x] not in dic.values():
                dic[ds[x]] = es[x]
                continue
            if ds[x] in dic and es[x] not in dic.values():
                return False
            if ds[x] not in dic and es[x] in dic.values():
                return False
            if ds[x] in dic and es[x] != dic[ds[x]]:
                return False
    # print(dic)
    return True

print(checkPasscode(ds, es))