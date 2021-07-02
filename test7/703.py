s = input()
ans = []
while s != "end":
    ans.append(s)
    s = input()
ans = tuple(ans)
print(ans)
print(ans[:3])
print(ans[len(ans) - 3:len(ans)])