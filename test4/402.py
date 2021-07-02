x = eval(input())
ans = []
while x != 9999:
    ans.append(x)
    x = eval(input())
print(min(ans))