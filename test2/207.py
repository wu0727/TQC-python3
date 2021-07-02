x = eval(input())
if x >= 8000 and x < 18000:
    print("%.1f" % (x * 0.95))
elif x >= 18000 and x < 28000:
    print("%.1f" % (x * 0.9))
elif x >= 28000 and x <= 38000:
    print("%.1f" % (x * 0.8))
else:
    print("%.1f" % (x * 0.7))