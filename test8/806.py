def compute(X,x):
    ans = X.count(x)
    return ans
X = input()
x = input()
print("%s occurs %d time(s)" % (x, compute(X,x)))
