import math
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print('({},{})'.format(x1,y1))
print('({},{})'.format(x2,y2))
print("Distance = %.4f" % (d))