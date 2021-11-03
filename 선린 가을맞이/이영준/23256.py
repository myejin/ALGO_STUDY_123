"""
Title : 성인 게임
Link : https://www.acmicpc.net/problem/23256
"""

import sys
input = sys.stdin.readline


dp = [[0] * 2 for _ in range(1_000_001)]
dp[1] = [3, 7]
for i in range(2, 1_000_001):
    dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 1][1]) % 1_000_000_007
    dp[i][1] = (dp[i - 1][0] * 4 + dp[i - 1][1] * 3) % 1_000_000_007


for _ in range(int(input())):
    print(dp[int(input())][1])
