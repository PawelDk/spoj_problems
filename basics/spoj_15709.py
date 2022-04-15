# 15709, SMPCIRC - Two Circles
# Math equations from here: https://www.matmana6.pl/wzajemne-polozenie-dwoch-okregow
import math

t = int(input())        # no of test cases
Xo1 = [None] * t
Yo1 = [None] * t
R1 = [None] * t
Xo2 = [None] * t
Yo2 = [None] * t
R2 = [None] * t
for i in range(t):      # input
    Xo1[i], Yo1[i], R1[i], Xo2[i], Yo2[i], R2[i],  = map(int, input().split())

for i in range(t):      # calculations
    distance_of_centers = math.sqrt((Xo1[i] - Xo2[i])**2 + (Yo1[i] - Yo2[i])**2)
    radius_difference = abs(R1[i] - R2[i])
    if distance_of_centers < radius_difference:     # output
        print("I")
    elif distance_of_centers == radius_difference:
        print("E")
    else:
        print("O")
