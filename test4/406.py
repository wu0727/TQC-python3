m = eval(input())
while m != -9999:
    k = eval(input())
    BMI = k / (m / 100) ** 2
    print('\033[1m' + 'BMI: %.2f'  % BMI + '\033[0m')
    if BMI >= 30:
        print('\033[1m' + 'State: fat' + '\033[0m')
    elif BMI >= 25:
        print('\033[1m' + 'State: over weight' + '\033[0m')
    elif BMI >= 18.5:
        print('\033[1m' + 'State: over weight' + '\033[0m')
    else:
        print('\033[1m' + 'State: under weight' + '\033[0m')
    m = eval(input())
