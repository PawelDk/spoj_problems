# 12156, STRHH - Half of the half
t = int(input())

text = [None] * t
for i in range(t):
    text[i] = input()

for i in range(t):
    x = text[i]             # read string
    x = x[:len(x)//2]       # take first half
    y = ""                  # prepare output
    for j in range(len(x)):
        if j % 2 == 0:
            y += x[j]
    print(y)
