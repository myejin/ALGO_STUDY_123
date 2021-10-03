"""
Title : 투자의 귀재 배주형
Link : https://www.acmicpc.net/problem/19947
"""

import sys

input = sys.stdin.readline

h, y = map(int, input().split())
dp = [0] *  (y + 1)
dp[0] = h
for i in range(1, y + 1):
    if i >= 5:
        dp[i] = max(int(dp[i - 1] * 1.05), int(dp[i - 3] * 1.20), int(dp[i - 5] * 1.35))
    elif i >= 3:
        dp[i] = max(int(dp[i - 1] * 1.05), int(dp[i - 3] * 1.20))
    else:
        dp[i] = int(dp[i - 1] * 1.05)

print(dp[-1])