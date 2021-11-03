"""
Title : 밤편지
Link : https://www.acmicpc.net/problem/23258
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def Floyd_Warshall(N: int, roads: list) -> list:
    # (i, j) 위치에서 최대 k 이하 이슬을 먹을 때 최소 거리
    dist = [[[0 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if roads[i][j]:
                dist[i][j][0] = roads[i][j]
            elif i != j:
                dist[i][j][0] = 10 ** 9
    # 거쳐 가는 점
    for k in range(1, N + 1):
        # 출발 점
        for i in range(1, N + 1):
            # 도착 점
            for j in range(1, N + 1):
                dist[i][j][k] = min(dist[i][j][k - 1], dist[i][k][k - 1] + dist[k][j][k - 1])
    return dist


N, Q = MIIS()
roads = [[0] * (N + 1)] + list([0] + list(MIIS()) for _ in range(N))
dist = Floyd_Warshall(N, roads)

for _ in range(Q):
    C, s, e = MIIS()
    if dist[s][e][C - 1] == 10 ** 9:
        print(-1)
    else:
        print(dist[s][e][C - 1])
