m = eval(input())
r = eval(input())
n = eval(input())
print("Month \t Amount")
for i in range(1, n + 1):
    m += m * r / 1200
    print('%3d   %.2f' % (i, m))