# 15708, SMPDIV - Divisibility
t = int(input())  # input
n = [None] * t
x = [None] * t
y = [None] * t
for i in range(t):
    n[i], x[i], y[i] = map(int, input().split())

for i in range(t):  # calc
    for j in range(1, n[i]):
        if j % x[i] == 0:   # div by x
            if j % y[i] != 0:   # not div by y
                print(j, end=' ')
    print("")
