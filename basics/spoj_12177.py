# 12177, CPTTRN2 - Character Patterns (Act 2)
t = int(input())        # no of test cases
l = [None] * t
c = [None] * t
for i in range(t):      # input
    l[i], c[i] = map(int, input().split())

for i in range(t):
    for j in range(l[i]):  # every line
        if j == 0 or j == l[i]-1:
            for k in range(c[i]):
                print("*", end='')
        else:
            if c[i] == 1:               # it might be done better?
                print("*", end='')
            else:
                print("*", end='')
                for k in range(c[i]-2):
                    print(".", end='')
                print("*", end='')
        print("")
    print("")
