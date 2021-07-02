s = input()
ans = False
if len(s) < 8:
    print("Invalid password")
else:
    for i in range(len(s)):
        if not s[i].isdigit() and not s[i].isalpha():
            print("Invalid password")
            break
        elif s[i].isupper():
            ans = True
    if ans:
        print("Valid password")
    else:
        print("Invalid password")