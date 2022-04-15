# 12180, CPTTRN4 - Character Patterns (Act 4)
t = int(input())        # no of test cases
l = [None] * t
c = [None] * t
h = [None] * t
w = [None] * t
for i in range(t):      # input
    l[i], c[i], h[i], w[i] = map(int, input().split())

for i in range(t):
    for j in range(l[i]):  # every line of the grid
        print(('*' + '*' * w[i]) * c[i] + '*')
        for k in range(h[i]):
            print(('*' + '.' * w[i]) * c[i] + '*')
    print(('*' + '*' * w[i]) * c[i] + '*')
    print("")
