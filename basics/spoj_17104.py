# 17104, SMPSEQ5 - Fun with Sequences (Act 3)
# the issue: when firs list was longer.

n = int(input())
S = list(map(int, input().split()))

m = int(input())
Q = list(map(int, input().split()))

indexes = []
length_of_check = min(len(S), len(Q))
for i in range(length_of_check):
    if S[i] == Q[i]:
        indexes.append(i+1)

for i in indexes:
    if i == indexes[-1]:
        # print(i, end='')
        print(i)
    else:
        print(i, end=' ')
