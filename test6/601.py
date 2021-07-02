a = []
n = 1
ans = 0
for i in range(12):
    a.append(eval(input()))
for i in a:
    print("%3d" % i, end="")
    if n % 3 == 0:
        print("")
    n += 1
    if n % 2 == 0:
        ans += i
print(ans)

