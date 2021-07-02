s = input()
s = s.split("-")
for i in s:
    if not i.isdigit():
        print("Invalid SSN")
        break
else:
    print("Valid SSN")