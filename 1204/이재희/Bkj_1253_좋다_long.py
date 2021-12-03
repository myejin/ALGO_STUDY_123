N = int(input())
A = list(map(int, input().split()))
A.sort()

good_cnt = 0

for i in range(N):
    s, e = 0, N-1
    while s < e:
        if s == i or A[s] + A[e] < A[i]:
            s += 1
        elif e == i or A[s] + A[e] > A[i]:
            e -= 1
        else:
            good_cnt += 1
            break

print(good_cnt)