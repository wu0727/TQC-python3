print("Enter group X’s subjects:")
x = input()
X = set()
while x != "end":
    X.add(x)
    x = input()
Y = set()
print("Enter group Y’s subjects:")
y = input()
while y != "end":
    Y.add(y)
    y = input()
print(X | Y)#所有
print(X & Y)#共同
print(Y - X)#Y有X沒有
print(X ^ Y)#彼此沒有
