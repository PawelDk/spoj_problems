# 7974, ACPC10A - What’s Next

a1 = []
a2 = []
a3 = []
while True:  # input
    x1, x2, x3 = map(float, input().split())
    if x1 == 0 and x2 == 0 and x3 == 0:
        break
    a1.append(x1), a2.append(x2), a3.append(x3)

for i in range(len(a1)):    # calculations
    if a2[i]-a1[i] == a3[i]-a2[i]:  # AP
        print("AP", int(a3[i]+a2[i]-a1[i]))
    else:
        if (a2[i]*a2[i]) == (a1[i]*a3[i]):  # GP
            if a2[i] == 0 and a3[i] == 0:
                print("GP", "0")
            else:
                print("GP", int(a3[i]*a3[i]/a2[i]))
