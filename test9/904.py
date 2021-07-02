f = open("read904.txt", 'r')
x = f.read()
people = x.split()
n = []
h = []
w = []

for i in range(int(len(people) / 3)):
    n.append(people[i * 3])
    h.append(eval(people[i * 3 + 1]))
    w.append(eval(people[i * 3 + 2]))
print(x)
print("Average height: %.2f" % (sum(h) / len(h)))
print("Average weight: %.2f" % (sum(w) / len(h)))
print("The tallest is %s with %.2fcm" %
      (n[h.index(max(h))], max(h)))
print("The heaviest is %s with %.2fkg" %
      (n[w.index(max(w))], max(w)))