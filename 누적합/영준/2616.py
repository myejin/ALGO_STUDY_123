"""
Title : 소형기관차
Link : https://www.acmicpc.net/problem/2616
"""

from itertools import accumulate
import sys
input = sys.stdin.readline


trains = int(input())
people_count = list(map(int, input().split()))
max_count = int(input())

base = sum(people_count[:max_count])
prefix_sum = []
for i in range(max_count, trains):
    prefix_sum.append(base)
    base += people_count[i]
    base -= people_count[i - max_count]
else:
    prefix_sum.append(base)

dp = [[0] * len(prefix_sum) for _ in range(3)]
dp[0][0] = prefix_sum[0]
dp[1][max_count] = prefix_sum[0] + prefix_sum[max_count]
dp[1][max_count * 2] = prefix_sum[0] + prefix_sum[max_count] + prefix_sum[max_count * 2]
for i in range(1, len(prefix_sum)):
    dp[0][i] = max(dp[0][i - 1], prefix_sum[i])
for i in range(max_count + 1, len(prefix_sum)):
    dp[1][i] = max(dp[1][i - 1], dp[0][i - max_count] + prefix_sum[i])
for i in range(max_count * 2 + 1, len(prefix_sum)):
    dp[2][i] = max(dp[2][i - 1], dp[1][i - max_count] + prefix_sum[i])

print(dp[-1][-1])
