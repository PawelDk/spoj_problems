import os
import time

print("This is testing file")


# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# multiple test cases with mutliple inputs:
t = int(input())        # no of test cases
a = [None] * t
b = [None] * t
for i in range(t):      # input
    a[i], b[i] = map(int, input().split())      # int float or just string?

# ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ====== ======
# rotating wait sign
# import os, time
for i in range(30):
    print('|'),    time.sleep(0.3),     os.system('clear')
    print('/'),    time.sleep(0.3),     os.system('clear')
    print('-'),    time.sleep(0.3),     os.system('clear')
    print('\\'),   time.sleep(0.3),     os.system('clear')
