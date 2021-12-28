"""
Title : 백양로 브레이크
Link : https://www.acmicpc.net/problem/11562
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
roads = [[] for _ in range(N + 1)]
dist = [[1000] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v, b = MIIS()
    roads[u].append((v, b))
    dist[u][v] = 0
    if b == 1:
        roads[v].append((u, b))
        dist[v][u] = 0
    else:
        dist[v][u] = 1
for i in range(1, N + 1):
    dist[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        if dist[i][k] == 1000:
            continue
        for j in range(1, N + 1):
            if dist[k][j] == 1000:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for _ in range(int(input())):
    s, e = MIIS()
    print(dist[s][e])
