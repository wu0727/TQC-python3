"""x = input()
n = 0
a = len(x)
ans = ""
for i in range(len(x) - 1, -1 , -1):
    if x[i] == ' ':
        n += 1
    if n == 3:
        a = i
        break
for i in range(a+1, len(x) - 1):
    ans += x[i]
print(ans)"""
x = input()
l = x.split()
print(" ".join(l[-3:]))