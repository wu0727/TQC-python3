x = float(input())
y = float(input())
z = float(input())
t = (x / 60) + (y / 3600)
ans = z / t
print("speed %.1f" % (ans / 1.6))