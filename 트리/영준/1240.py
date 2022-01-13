"""
Title : 노드사이의 거리
Link : https://www.acmicpc.net/problem/1240
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, M = MIIS()
nodes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y, d = MIIS()
    nodes[x].append((y, d))
    nodes[y].append((x, d))

for _ in range(M):
    x, y = MIIS()
    visited = [False] * (N + 1)
    queue = deque([(x, 0)])
    while queue:
        u, dist = queue.popleft()
        if u == y:
            print(dist)
            break
        if visited[u]:
            continue
        visited[u] = True
        for v, d in nodes[u]:
            if not visited[v]:
                queue.append((v, dist + d))
