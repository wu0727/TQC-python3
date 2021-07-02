import math
def compute(n):
    ans = [0, 1]
    for i in range(n - 1):
        ans.append(ans[i] + ans[i + 1])
        print(ans[i], end=" ")
    print(ans[n - 1])
compute(eval(input()))
