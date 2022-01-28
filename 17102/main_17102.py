# 17102, SMPSEQ3 - Fun with Sequences
# the isssue is ascending.

n = int(input())
S = list(map(int, input().split()))

m = int(input())
Q = list(map(int, input().split()))

new_list = list(set(S) - set(Q))
new_list.sort()
for i in new_list:
    if i == new_list[-1]:
        print(i)
    else:
        print(i, end=' ')
