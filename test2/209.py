import math
x1 = eval(input())
y1 = eval(input())
if math.sqrt((x1 - 5) ** 2 + (y1 - 6) ** 2) <= 15:
    print("Inside")
else:
    print("Outside")