x = input()
ans = 0
for i in range(len(x)):
    print("ASCII code for '%s'is %d" % (x[i], ord(x[i])))
    ans += ord(x[i])
print(ans)