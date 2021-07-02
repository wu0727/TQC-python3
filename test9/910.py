file = open("read910.dat", 'r', encoding = 'UTF-8')
d = file.read().split()
males = 0
females = 0
for i in d:
    print(i, end = " ")
    if (d.index(i) + 1) % 4 == 0:
        print(" ")
    if i == "0":
        females += 1
    if i == "1":
        males += 1
file.close()
print("Number of males: ", males)
print("Number of females: ", females)