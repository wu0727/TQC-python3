d = {}
print("Key: ", end = "")
K = input()
while K != "end":
    print("Value: ", end = "")
    c = input()
    d[K] = c
    print("Key: ", end = "")
    K = input()
print("Search key: ", end = "")
print(input() in d)