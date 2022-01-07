"""
Title : 구간 합 구하기 5
Link : https://www.acmicpc.net/problem/11660
"""

import sys, itertools
input = sys.stdin.readline


n, m = map(int ,input().split())
seq = [[0] * (n + 1)] + [[0] + list(itertools.accumulate(map(int, input().split()))) for _ in range(n)]

for i in range(2, n + 1):
    for j in range(1, n + 1):
        seq[i][j] += seq[i - 1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(seq[x2][y2] - seq[x1 - 1][y2] - seq[x2][y1 - 1] + seq[x1 - 1][y1 - 1])
