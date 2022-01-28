# 1, TEST - Life, the Universe, and Everything
n = []
while True:
    number = int(input())
    if number == 42:
        number = int(input())
        break
    else:
        n.append(number)

for i in n:
    print(i)
