x = int(input())
if x % 3 == 0:
    if x % 5 == 0:
        print("%d is a multiple of 3 and 5." % (x))
    else:
        print("%d is a multiple of 3." % (x))
elif x % 5 == 0:
    print("%d is a multiple of 5." % (x))
else:
    print("%d is not a multiple of 3 and 5." % (x))