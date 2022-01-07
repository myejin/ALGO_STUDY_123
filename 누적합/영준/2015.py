"""
Title : 수들의 합 4
Link : https://www.acmicpc.net/problem/2015
"""

from itertools import accumulate
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, K = MIIS()
seq = list(MIIS())
prefix_sum = list(accumulate(seq))

ans = 0
last = {}
for i in range(N):
    if prefix_sum[i] == K:
        ans += 1
    if prefix_sum[i] - K in last:
        ans += last[prefix_sum[i] - K]
    if prefix_sum[i] in last:
        last[prefix_sum[i]] += 1
    else:
        last[prefix_sum[i]] = 1

print(ans)
