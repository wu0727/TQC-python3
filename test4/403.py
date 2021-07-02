a = eval(input())
b = eval(input())
n = 10
s = 0
N = 0
for i in range(a, b + 1):
    if i % 4 == 0 or i % 9 == 0:
        print("%4d" % i, end="")
        n -= 1
        N += 1
        s += i
    if n == 0:
        n = 10
        print("")
print("")
print(N)
print(s)