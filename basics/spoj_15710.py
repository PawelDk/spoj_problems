# 15710, SMPSUM - Iterated sums

a, b = input().split()
calculated_sum = 0
for i in range(int(a), int(b)+1):
    calculated_sum += i*i
print(calculated_sum)
