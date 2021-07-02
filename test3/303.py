a = int(input())
ans = 0
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print("%4d" % (i * j), end = "")
    print("")