"""
Title : 방 번호
Link : https://www.acmicpc.net/problem/1082
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    prices = list(map(int, input().split()))
    M = int(input())
    
    dp = [0] * 51
    for idx, price in enumerate(prices):
        dp[price] = idx
    for i in range(min(prices) * 2, M + 1):
        for j, price in enumerate(prices):
            if i - price >= 0 and dp[i - price]:
                dp[i] = max(dp[i], dp[i - price] * 10 + j)
            pass
    print(max(dp[:M + 1]))
