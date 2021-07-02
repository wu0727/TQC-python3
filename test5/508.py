import math
def compute(x, y):
    #m = min(x, y)
    #ans = []
    #for i in range(1, m + 1):
    #    if x % i == 0 and y % i == 0:
    #        ans.append(i)
    #return ans
    return math.gcd(x, y)
x,y = eval(input())
#print(max(compute(x, y)))
print(compute(x, y)) 