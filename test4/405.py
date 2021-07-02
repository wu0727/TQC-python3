x = eval(input())
while x != -9999:
    if x >= 90:
        print('\033[1m' + 'A' + '\033[0m')
    elif x >= 80:
        print('\033[1m' + 'B' + '\033[0m')
    elif x >= 70:
        print('\033[1m' + 'C' + '\033[0m')
    elif x >= 60:
        print('\033[1m' + 'D' + '\033[0m')
    else:
        print('\033[1m' + 'E' + '\033[0m')
    x = eval(input())