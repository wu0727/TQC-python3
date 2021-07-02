f = open("read.txt")
w = f.read()
f.close()
ans = [int(i) for i in w.split()]
print(sum(ans))