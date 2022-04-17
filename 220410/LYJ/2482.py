"""
Title : 색상환
Link : https://www.acmicpc.net/problem/2482
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    K = int(input())
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][0] = 1
        dp[i][1] = i
    for i in range(3, N + 1):
        for j in range(2, K + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) % 1_000_000_003
    print((dp[N - 1][K] + dp[N - 3][K - 1]) % 1_000_000_003)
