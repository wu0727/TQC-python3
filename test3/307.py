x = int(input())
for i in range(1, x + 1):
    for j in range(1, x + 1):
        print("%-2d* %-2d= %-4d" % (j, i, i * j), end = "")
    print("")