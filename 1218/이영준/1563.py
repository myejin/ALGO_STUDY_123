"""
Title : 개근상
Link : https://www.acmicpc.net/problem/1563
"""

import sys
input = sys.stdin.readline
N = int(input())


# 전체 날짜 - 지각 횟수 - 연속 결석
dp = [[[0] * 3 for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 1

for i in range(1, N + 1):
    dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % 1_000_000
    dp[i][0][1] = dp[i - 1][0][0] % 1_000_000
    dp[i][0][2] = dp[i - 1][0][1] % 1_000_000
    dp[i][1][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2] + dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2]) % 1_000_000
    dp[i][1][1] = dp[i - 1][1][0] % 1_000_000
    dp[i][1][2] = dp[i - 1][1][1] % 1_000_000

print((sum(dp[-1][0]) + sum(dp[-1][1])) % 1_000_000)
