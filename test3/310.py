import  math
n = eval(input())
ans = 0
for i in range(1, n):
    ans += 1 / (math.sqrt(i) + math.sqrt(i + 1))
print('%.4f' % ans)