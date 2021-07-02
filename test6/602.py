ans = 0
for i in range(5):
    x = input()
    if x == "J":
        ans += 11
    elif x == "Q":
        ans += 12
    elif x == "K":
        ans += 13
    elif x == "A":
        ans += 1
    else:
        ans += int(x)
print(ans)