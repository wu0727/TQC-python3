ans = []
print("\033[1m" + "Create tuple1:" + "\033[0m")
x = eval(input())
while x != -9999:
    ans.append(x)
    x = eval(input())
print("\033[1m" + "Create tuple2:" + "\033[0m")
x = eval(input())
while x != -9999:
    ans.append(x)
    x = eval(input())
print("Combined tuple before sorting:", tuple(ans))
print("Combined list after sorting:", sorted(ans))