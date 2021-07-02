import math
def compute(x, y):
    return math.gcd(x, y)
x,y = eval(input())
m,n = eval(input())
p = (x * n + y * m) / compute(x * n + y * m, y * n)
q = (y * n) / compute(x * n + y * m, y * n)
print("%d/%d + %d/%d = %d/%d" % (x, y, m, n, p, q))