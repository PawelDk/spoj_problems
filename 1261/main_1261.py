# 1261, JPESEL - Pesel
t = int(input())        # no. of test cases
pesel = [None] * t
for i in range(t):      # input
    pesel[i] = input()

for i in range(t):
    control_sum = int(pesel[i][0]) * 1 + \
                  int(pesel[i][1]) * 3 + \
                  int(pesel[i][2]) * 7 + \
                  int(pesel[i][3]) * 9 + \
                  int(pesel[i][4]) * 1 + \
                  int(pesel[i][5]) * 3 + \
                  int(pesel[i][6]) * 7 + \
                  int(pesel[i][7]) * 9 + \
                  int(pesel[i][8]) * 1 + \
                  int(pesel[i][9]) * 3 + \
                  int(pesel[i][10]) * 1
    if control_sum > 0:
        if control_sum % 10 == 0:
            print("D")
        else:
            print("N")
