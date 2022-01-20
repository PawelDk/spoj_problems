# 23919, CHITEST1 - Sum of two numbers
t = int(input())        # no. of test cases
a = [None] * t
b = [None] * t
for i in range(t):      # input
    a[i], b[i] = map(float, input().split())

for i in range(t):
    print(a[i] + b[i])
