# 12178, CPTTRN3 - Character Patterns (Act 3)
t = int(input())        # no of test cases
l = [None] * t
c = [None] * t
for i in range(t):      # input
    l[i], c[i] = map(int, input().split())

for i in range(t):
    for j in range(l[i]):  # every line
        print('***' * c[i] + '*')
        print('*..' * c[i] + '*')
        print('*..' * c[i] + '*')
    print('***' * c[i] + '*')
    print("")
