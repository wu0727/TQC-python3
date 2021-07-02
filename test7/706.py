x = eval(input())
for i in range(x):
    s = input()
    ans = set(s.lower())
    ans.remove(' ')
    print(len(ans) == 26)
