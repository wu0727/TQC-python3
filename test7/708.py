def compute():
    D = {}
    print("Key:", end="")
    K = input()
    while K != "end":
        print("Value:", end="")
        v = input()
        D[K] = v
        print("Key:", end="")
        K = input()
    return D
print("Create dict1:")
dict1 = compute()
print("Create dict2:")
dict2 = compute()

dict1.update(dict2)
for i in dict1:
    print("%s: %s" % (i,dict1[i]))