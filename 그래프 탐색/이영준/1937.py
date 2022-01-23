"""
Title : 욕심쟁이 판다
Link : https://www.acmicpc.net/problem/1937
"""

import sys
input = sys.stdin.readline


n = int(input())
bambu = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

count = {}
for i in range(n):
    for j in range(n):
        b = bambu[i][j]
        if b in count:
            count[b].append((i, j))
        else:
            count[b] = [(i, j)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
max_move = 1

for b in sorted(count.keys()):
    for i, j in count[b]:
        move = dp[i][j]
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < n and 0 <= nj < n:
                # 대나무가 더 많다면
                if bambu[i][j] < bambu[ni][nj]:
                    # 이동횟수가 더 많아 진다면
                    if move + 1 > dp[ni][nj]:
                        dp[ni][nj] = move + 1
                        if move + 1 > max_move:
                            max_move = move + 1

print(max_move)
