# 12176, CPTTRN1 - Character Patterns (Act 1)
t = int(input())        # no of test cases
l = [None] * t
c = [None] * t
for i in range(t):      # input
    l[i], c[i] = map(int, input().split())

for i in range(t):
    for j in range(l[i]):  # every line
        for k in range(c[i]):  # every column
            if j % 2 == 0:
                if k % 2 == 0:
                    print("*", end='')
                else:
                    print(".", end='')
            else:
                if k % 2 == 0:
                    print(".", end='')
                else:
                    print("*", end='')
        print("")
    print("")
