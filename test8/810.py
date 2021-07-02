k = eval(input())
for x in range(k):
    s = input()
    a = [float(i) for i in s.split()]
    print("\033[1m%.2f\033[0m" %(max(a) - min(a)))
