# 12187, CPTTRN6 - Character Patterns (Act 6)

t = int(input())        # no of test cases
l = [None] * t
c = [None] * t
h = [None] * t
w = [None] * t
for i in range(t):      # input
    l[i], c[i], h[i], w[i] = map(int, input().split())

for i in range(t):      # iteration through test cases
    for j in range(l[i]+1):  # iteration through rows of cells
        for k in range(h[i]):   # iteration through rows in cell
            print(('.' * w[i] + '|') * c[i] + '.' * w[i])
        if j != l[i]:
            print(('-' * w[i] + '+') * c[i] + '-' * w[i])
    print("")
