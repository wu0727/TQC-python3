ans = []
for i in range(3):
    ans.append([])
    for j in range(3):
        ans[i].append(eval(input()))
ma = [max(ans[0]),max(ans[1]),max(ans[2])]
mi = [min(ans[0]),min(ans[1]),min(ans[2])]
ax = ma.index(max(ma))
ay = ans[ax].index(max(ma))
ix = mi.index(min(mi))
iy = ans[ix].index(min(mi))
print("Index of the largest number %d is: (%d, %d)" %
      (max(ma), ax, ay))
print("Index of the smallest number %d is: (%d, %d)" %
      (min(mi), ix, iy))