"""
Title : Dance Dance Revolution
Link : https://www.acmicpc.net/problem/2342
"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(idx, right, left):
    global seq, l, dp
    if idx == l - 1:
        return 0
    if dp[idx][right][left] != -1:
        return dp[idx][right][left]
    dp[idx][right][left] = min(
        dfs(idx + 1, seq[idx], left) + move_count(right, seq[idx]),
        dfs(idx + 1, right, seq[idx]) + move_count(left, seq[idx]),
    )
    return dp[idx][right][left]


def move_count(before, after):
    if before == after:
        return 1
    if before == 0:
        return 2
    if abs(after - before) % 2:
        return 3
    return 4

seq = list(map(int, input().split()))
l = len(seq)
dp = [[[-1] * 5 for _ in range(5)] for _ in range(l)]

print(dfs(0, 0, 0))
