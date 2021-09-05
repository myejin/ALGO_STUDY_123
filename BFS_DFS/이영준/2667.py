"""
Title : 단지번호붙이기
Link : https://www.acmicpc.net/problem/2667
"""


import sys
sys.setrecursionlimit(int(1e6))


def dfs(i: int, j: int):
    global danji, direction, visited, danji_size
    for k in range(4):
        d = direction[k]
        x, y = i + d[0], j + d[1]
        if x < 0 or x >= n:
            continue
        if y < 0 or y >= n:
            continue
        if danji[x][y] == 0:
            continue
        if visited[x][y]:
            continue
        visited[x][y] = True
        danji_size += 1
        dfs(x, y)
    return


n = int(input())
danji = [[int(i) for i in input().strip()] for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
direction = {0: (-1, 0), 1: (0, 1), 2:(1, 0), 3:(0, -1)}
danji_count = 0
danji_sizes = []

for i in range(n):
    for j in range(n):
        if danji[i][j] and not visited[i][j]:
            danji_count += 1
            danji_size = 1
            visited[i][j] = True
            dfs(i, j)
            danji_sizes.append(danji_size)

print(danji_count)
print(*sorted(danji_sizes), sep = '\n')