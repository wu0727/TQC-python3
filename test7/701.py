ans = []
x = eval(input())
while x != -9999:
    ans.append(x)
    x = eval(input())
ans = tuple(ans)
print(ans)
print("Length: %d" % len(ans))
print("Max:", max(ans))
print("Min:", min(ans))
print("Sum:", sum(ans))