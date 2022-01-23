# 29154, ALCATRAZ1 - SUM OF DIGITS
t = int(input())        # no of test cases
numbers = [None] * t
for i in range(t):      # input
    numbers[i] = input()

for i in range(t):      # calculating
    sumOfDigits = 0
    for j in numbers[i]:
        sumOfDigits += int(j)
    print(sumOfDigits)
