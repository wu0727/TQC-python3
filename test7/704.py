x = eval(input())
s = set()
while x != -9999:
    s.add(x)
    x = eval(input())
print("Length: ", len(s))
print("Max: ", max(s))
print("Min: ", min(s))
print("Sum: ", sum(s))