x = int(input())
ans = 0
for i in range(x):
    y = input()
    for j in range(len(y)):
        ans += int(y[j])
    print("Sum of all digits of %d is %d" % (y, ans))
