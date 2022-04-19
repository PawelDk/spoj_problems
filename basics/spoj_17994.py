# 17994, PCROSS1 - Cross Pattern (Act 1)

t = int(input())  # no of test cases
m = [None] * t
n = [None] * t
ci = [None] * t
cj = [None] * t
for i in range(t):  # input
    m[i], n[i], ci[i], cj[i] = map(int, input().split())

for i in range(t):  # calculations
    for row in range(m[i]):
        if row == ci[i]-1:
            print('*'*n[i])
        else:
            for column in range(n[i]):
                if column == cj[i]-1:
                    print('*', end='')
                else:
                    print('.', end='')
            print("")
