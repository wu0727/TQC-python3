d = {}
print("Key: ", end = "")
K = input()
while K != "end":
    print("Value: ", end = "")
    c = input()
    d[K] = c
    print("Key: ", end="")
    K = input()
t = sorted(d)
for i in t:
    print("%s: %s" % (i, d[i]))