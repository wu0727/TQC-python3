x = input()
ln = 0
wn = 0
cn = 0
with open(x, 'r+') as f:
    for line in f:
        ln += 1
        wn += len(line.split())
        cn += sum([len(n) for n in line.split()])
print(ln, "line(s)")
print(wn, "word(s)")
print(cn, "character(s)")