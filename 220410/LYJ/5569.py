"""
Title : 출근 경로
Link : https://www.acmicpc.net/problem/5569
"""

from math import comb
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    W, H = map(int, input().split())
    
    if W == 2 or H == 2:
        print(2)
    else:
        dp = [[[0, 0, 0, 0] for _ in range(W)] for _ in range(H)]
        for i in range(H):
            dp[i][0][3] = 1
        for j in range(W):
            dp[0][j][1] = 1
        for i in range(1, H):
            for j in range(1, W):
                dp[i][j][0] += dp[i][j - 1][3]
                dp[i][j][1] += dp[i][j - 1][0] + dp[i][j - 1][1]
                dp[i][j][2] += dp[i - 1][j][1]
                dp[i][j][3] += dp[i - 1][j][2] + dp[i - 1][j][3]
        print(sum(dp[-1][-1]) % 100_000)
