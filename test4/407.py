y = eval(input())
while y != -9999:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print('\033[1m%d is a leap year.' % (y)
              + '\033[0m')
    else:
        print('\033[1m%d is not a leap year.' % (y)
              + '\033[0m')
    y = eval(input())