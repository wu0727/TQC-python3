d = input()
be = input()
af = input()
f = open(d, "r+") #r+讀寫
data = f.read()

print("=== Before the deletion")
print(data)
data = data.replace(be, af)
print("=== After the deletion")
print(data)
f.seek(0)
f.write(data)
f.close()
