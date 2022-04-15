# 12185, CPTTRN5 - Character Patterns (Act 5)

t = int(input())        # no of test cases
l = [None] * t
c = [None] * t
s = [None] * t
for i in range(t):      # input
    l[i], c[i], s[i] = map(int, input().split())

for i in range(t):  # iteration through test cases

    print(('*' + '*' * s[i]) * c[i] + '*')  # first line

    for j in range(l[i]):  # iteration through rows in grid

        for k in range(s[i]):   # iterations through lines

            for m in range(c[i]):   # iteration through columns in grid
                print("*", end="")
                for n in range(s[i]):   # iteration throug lines in cell !
                    if m % 2 == 0:
                        if k == n:
                            print("\\", end="")
                        else:
                            print(".", end="")
                    else:
                        if k == s[i] and n == 0:    # - i don't know the relation yet
                            print("/", end="")
                        else:
                            print(".", end="")

                    # print(".", end="")
                print("", end="")
            print("*")   # new line at the end of line

        print(('*' + '*' * s[i]) * c[i] + '*')  # last line in row in grid

    print("")
