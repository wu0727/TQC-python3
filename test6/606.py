def compute(r, c):
    x = [[0 for col in range(c)] for row in range(r)]
    for i in range(c):
        x[0][i] = i
        print("%4d" % (x[0][i]), end="")
    print("")
    for i in range(r - 1):
        for j in range(c):
            x[i + 1][j] = x[i][j] - 1
            print("%4d" % (x[i + 1][j]), end="")
        print("")
r = int(input())
c = int(input())
compute(r, c)