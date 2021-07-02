n1 = 0
n2 = 0
n = 0
for i in range(5):
    v = eval(input())
    if v == 1:
        n1 += 1
        print("\033[1mTotal votes of No.1: Nami= %d" %n1 +
              "\033[0m")
        print("\033[1mTotal votes of No.2: Chopper= %d" % n1 +
              "\033[0m")
        print("\033[1mTotal null votes = %d" % n + "\033[0m")
    elif v == 2:
        n2 += 1
        print("\033[1mTotal votes of No.1: Nami= %d" % n1 +
              "\033[0m")
        print("\033[1mTotal votes of No.2: Chopper= %d" % n2 +
              "\033[0m")
        print("\033[1mTotal null votes = %d" % n + "\033[0m")
    else:
        n += 1
        print("\033[1mTotal votes of No.1: Nami= %d" % n1 +
              "\033[0m")
        print("\033[1mTotal votes of No.2: Chopper= %d" % n2 +
              "\033[0m")
        print("\033[1mTotal null votes = %d" % n + "\033[0m")
if n1 > n2:
    print("\033[1m=> No.1 Nami won the election.\033[0m")
elif n2 > n1:
    print("\033[1m=> No.2 Chopper won the election.\033[0m")
else:
    print("\033[1m=> No one won the election.\033[0m")