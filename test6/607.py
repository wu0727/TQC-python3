ans = [[0 for col in range(5)]for row in range(3)]
title = ["1st", "2nd", "3rd"]
for i in range(3):
    print("\033[1m" + "The %s student:"%(title[i]) + "\033[0m")
    for j in range(5):
        ans[i][j] = eval(input())
for i in range(3):
    print("Student %d" % (i+1))
    print("#Sum %d" %(sum(ans[i])))
    print("#Average %.2f" %(sum(ans[i]) / 5))