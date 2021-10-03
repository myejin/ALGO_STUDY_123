"""
Title : 동물원
Link : https://www.acmicpc.net/problem/1309
"""

import sys

input = sys.stdin.readline

n = int(input())

# 각 열은 왼쪽, 오른쪽에 사자가 있을 때, 사자가 없을때
dp = [[0 for _ in range(3)] for _ in range(n + 1)]
dp[0][2] = 1
for i in range(1, n + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901

print(sum(dp[-1]) % 9901)