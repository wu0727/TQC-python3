even = 0
for i in range(10):
    x = eval(input())
    if x % 2 == 0:
        even += 1
print("Even numbers: %d" % even)
print("Odd numbers: %d" % (10 - even))