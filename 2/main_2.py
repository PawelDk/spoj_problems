# 2, PRIME1 - Prime Generator
# issue is runtime to long. Try other alghorithm:
# https://eduinf.waw.pl/inf/alg/001_search/0012.php
# https://home.agh.edu.pl/~zobmat/2021/rzepka_radoslaw/algorytmy.html


t = int(input())        # no of test cases
m = [None] * t
n = [None] * t
for i in range(t):      # inputs
    m[i], n[i] = map(int, input().split())

for i in range(t):      # calculations, every test case

    for number in range(m[i], n[i] + 1):
        if number > 1:
            for j in range(2, number):
                if (number % j) == 0:
                    break
            else:
                print(number)
    print("")

    #the above also gives time limit exceded

'''
old version 
    for j in range(m[i], n[i]+1):     # every number in range
        if j > 1:
            for k in range(2, math.ceil(math.sqrt(j))+1):  # every natural possible divider
                if j % k == 0:
                    break
            else:
                    print(j)
    print("")
'''

'''
older version 
for i in range(t):      # calculations, every test case
    for j in range(m[i], n[i]+1):     # every number in range
        is_prime = True
        for k in range(2, math.ceil(math.sqrt(j))+1):   # every natural possible divider
            if j % k == 0:
                is_prime = False
                break
        if is_prime and j != 1:
            print(j)
    print("")
'''