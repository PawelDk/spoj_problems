# 17103, SMPSEQ4 - Fun with Sequences (Act 2)

n = int(input())
S = list(map(int, input().split()))

m = int(input())
Q = list(map(int, input().split()))

new_list = list(set(Q).intersection(S))
new_list.sort()
for i in new_list:
    if i == new_list[-1]:
        print(i)
    else:
        print(i, end=' ')
