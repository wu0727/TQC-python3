f = open("data.txt", 'a+')
for i in range(5):
    f.write('\n' + input())
f.seek(0)
w = f.read()
print(w)
f.close()