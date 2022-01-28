# 1112, NSTEPS - Number Steps

t = int(input())  # no of test cases
x = [None] * t
y = [None] * t
for i in range(t):  # input
    x[i], y[i] = map(int, input().split())  # int float or just string?

for i in range(t):  # calculations
    sum_of_coordinates = x[i] + y[i]
    if x[i] == y[i]:
        if x[i] % 2 == 1:  # odd numbers
            print(sum_of_coordinates-1)
        else:   # even numbers
            print(sum_of_coordinates)
    elif x[i] - y[i] == 2:
        if x[i] % 2 == 1:  # odd numbers
            print(sum_of_coordinates-1)
        else:   # even numbers
            print(sum_of_coordinates)
    else:
        print("No Number")
