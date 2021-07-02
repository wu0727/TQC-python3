s = input()
x = [int(i) for i in s.split()]

print("Total = ",  sum(x))
print("Total = %.1f" % (sum(x) / len(x)))