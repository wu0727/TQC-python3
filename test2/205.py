x = input()
if x >= 'A' and x <= 'Z' or x >= 'a' and x <= 'z':
    print("%c is an alphabet." % (x))
elif x >= '0' and x <= '9':
    print("%c is a number." % (x))
else:
    print("%c is a symbol." % (x))