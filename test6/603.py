ans = []
for i in range(10):
    ans.append(int(input()))
ans.sort(reverse = True)
print("%d %d %d" % (ans[0], ans[1], ans[2]))