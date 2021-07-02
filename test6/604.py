"""import numpy as np
ans = []
for i in range(10):
    ans.append(int(input()))
a = np.bincount(ans)
print(np.argmax(a))
print(a[np.argmax(a)])"""

ans = []
c = [0] * 10
for i in range(10):
    n = int(input())
    ans.append(n)
    c[ans.index(n)] += 1
print(ans[c.index(max(c))])
print(max(c))
print(c)
