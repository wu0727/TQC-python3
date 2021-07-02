data = []
with open("data909.dat", 'w+') as file:
    for i in range(5):
        file.write(input() + '\n')
file = open("data909.dat", 'r+')
d = file.read()
data = d.split()
for i in data:
    print(i,end = " ")
    if(data.index(i) + 1) % 2 == 0:
        print(" ")
        print(" ")