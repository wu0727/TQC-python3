matrix1 = []
matrix2 = []
ans = []
print("\033[1m" + "Enter matrix 1:" + "\033[0m")
for i in range(2):
    matrix1.append([])
    for j in range(2):
        matrix1[i].append(eval(input()))
        print("[%d, %d]: %d" % (i + 1, j + 1, matrix1[i][j]))

print("\033[1m" + "Enter matrix 2:" + "\033[0m")
for i in range(2):
    matrix2.append([])
    ans.append([])
    for j in range(2):
        matrix2[i].append(eval(input()))
        ans[i].append(matrix1[i][j] + matrix2[i][j])
        print("[%d, %d]: %d" % (i + 1, j + 1, matrix2[i][j]))

print("\033[1m" + "Matrix 1:" + "\033[0m")
print("**%d %d **" % (matrix1[0][0], matrix1[0][1]))
print("**%d %d **" % (matrix1[1][0], matrix1[1][1]))

print("\033[1m" + "Matrix 2:" + "\033[0m")
print("**%d %d **" % (matrix2[0][0], matrix2[0][1]))
print("**%d %d **" % (matrix2[1][0], matrix2[1][1]))

print("\033[1m" + "Sum of 2 matrices:" + "\033[0m")
print("**%d %d **" % (ans[0][0], ans[0][1]))
print("**%d %d **" % (ans[1][0], ans[1][1]))