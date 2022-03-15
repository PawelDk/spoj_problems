# 35296, PRIONPRI - Prime or not Prime!

def is_prime(number_to_check):
    for n in range(2, int(number_to_check**0.5)+1):
        if number_to_check % n == 0:
            return False
    return True


t = int(input())        # no of test cases
number = [None] * t
for i in range(t):      # input
    number[i] = int(input())

for i in range(t):  # iteration through test cases
    if is_prime(number[i]):
        print("YES")
    else:
        print("NO")
