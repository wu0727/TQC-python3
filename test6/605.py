x = []
ans = 0
for i in range(10):
    n = int(input())
    x.append(n)
    ans += n
ans -= (min(x) + max(x))
print(ans)
print("%.2f" % (ans / 8))