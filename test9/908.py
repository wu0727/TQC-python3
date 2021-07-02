fn = input()
n = eval(input())
d = {}
ans = []
with open(fn, 'r') as file:
    for line in file:
        for w in line.split():
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
for i in d:
    if d[i] == n:
        ans.append(i)
ans.sort()
for i in ans:
    print(i)