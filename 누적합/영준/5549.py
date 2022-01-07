"""
Title : 행성 탐사
Link : https://www.acmicpc.net/problem/5549
"""

from itertools import accumulate
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


M, N = MIIS()
K = int(input())
planet_map = [input().strip() for _ in range(M)]

# set table
jungle = [[0] * (N + 1) for _ in range(M + 1)]
ocean = [[0] * (N + 1) for _ in range(M + 1)]
ice = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(1, M + 1):
    for j in range(1, N + 1):
        if planet_map[i - 1][j - 1] == 'J':
            jungle[i][j] += 1
        elif planet_map[i - 1][j - 1] == 'O':
            ocean[i][j] += 1
        else:
            ice[i][j] += 1

# get prefix sum
for i in range(1, M + 1):
    jungle[i] = list(accumulate(jungle[i]))
    ocean[i] = list(accumulate(ocean[i]))
    ice[i] = list(accumulate(ice[i]))
    for j in range(1, N + 1):
        jungle[i][j] += jungle[i - 1][j]
        ocean[i][j] += ocean[i - 1][j]
        ice[i][j] += ice[i - 1][j]

# query
for _ in range(K):
    a, b, c, d = MIIS()
    print(
        jungle[c][d] - jungle[a - 1][d] - jungle[c][b - 1] + jungle[a - 1][b - 1],
        ocean[c][d] - ocean[a - 1][d] - ocean[c][b - 1] + ocean[a - 1][b - 1],
        ice[c][d] - ice[a - 1][d] - ice[c][b - 1] + ice[a - 1][b - 1]
    )
