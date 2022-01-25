"""
Title : 경쟁적 전염
Link : https://www.acmicpc.net/problem/18405
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, K = MIIS()
grid = [list(MIIS()) for _ in range(N)]
S, X, Y = MIIS()

virus = {i: [] for i in range(1, K + 1)}
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            virus[grid[i][j]].append((i, j))

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
for _ in range(S):
    for v in range(1, K + 1):
        next_pos = []
        for x, y in virus[v]:
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                    grid[nx][ny] = v
                    next_pos.append((nx, ny))
        virus[v] = next_pos[::]

print(grid[X - 1][Y - 1])
