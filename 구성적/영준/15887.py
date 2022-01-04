"""
Title : 욱제는 결벽증이야!!
Link : https://www.acmicpc.net/problem/15887
"""

import sys
input = sys.stdin.readline


N = int(input())
seq = list(map(int, input().split()))
sorted_seq = sorted(seq)

count = 0
ans = []
for i in range(1, N + 1):
    if seq == sorted_seq:
        break
    if seq[i - 1] != i:
        count += 1
        idx = seq.index(i) + 1
        seq[i-1:idx] = seq[i-1:idx][::-1]
        ans.append((i, idx))

print(count)
for line in ans:
    print(*line)


'''
# TLE
N = int(input())
seq = list(map(int, input().split()))


count = 0
ans = []
while True:
    st = -1
    intervals = []
    for i in range(N - 1):
        if st == -1 and seq[i] > seq[i + 1]:
            st = i
        elif st != -1 and seq[i] < seq[i + 1]:
            intervals.append((st, i))
            st = -1
    else:
        if st != -1:
            intervals.append((st, N - 1))
    if not intervals:
        break
    else:
        count += 1
        intervals.sort(key=lambda x:-(x[1] - x[0]))
        s, e = intervals[0]
        ans.append((s + 1, e + 1))
        while s < e:
            seq[s], seq[e] = seq[e], seq[s]
            s += 1
            e -= 1

print(count)
for line in ans:
    print(*line)
'''
