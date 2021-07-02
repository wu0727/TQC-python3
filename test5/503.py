def compute(a, b):
    return ((a + b) * (b - a + 1))/2
a = eval(input())
b = eval(input())
print("%d" % compute(a, b))