import math
def compute(a, b, c):
    if (b ** 2) - (4 * a * c) >= 0:
        ans1 = (-1 * b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
        ans2 = (-1 * b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
        return ans1, ans2
    else:
        return 0
a = eval(input())
b = eval(input())
c = eval(input())
if compute(a, b, c) != 0:
    print("%.1f %.1f" % compute(a, b, c))
else:
    print("Your equation has no root.")
