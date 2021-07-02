tem = []
ans = []
for i in range(4):
    print("Week %d" %(i + 1))
    tem.append([])
    for j in range(3):
        print("Day %d:" % (j+1),end="")
        tem[i].append(eval(input()))

for i in range(4):
    ans.extend(tem[i])
print("Average: %.2f" %(sum(ans) / 12))
print("Highest:", max(ans))
print("Lowest:", min(ans))


"""用一維寫好
tem = []
for i in range(4):
    print("Week %d" %(i + 1))
    for j in range(3):
        print("Day %d:" % (j+1),end="")
        tem.append(eval(input()))
print("Average: %.2f" %(sum(tem) / 12))
print("Highest:", max(tem))
print("Lowest:", min(tem))
"""