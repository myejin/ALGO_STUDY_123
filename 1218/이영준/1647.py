"""
Title :  도시 분할 계획
Link : https://www.acmicpc.net/problem/1647
"""

import sys, heapq
input = sys.stdin.readline


n, m = map(int, input().split())
roads = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    roads[a].append((b, c))
    roads[b].append((a, c))

# 힙
road_check = []
# 방문
visited = [False] * (n + 1)
# 추가된 도로
minmum_spanning_tree = []
# 탐색 준비
heapq.heappush(road_check, (0, 1))

while road_check:
    dist, now = heapq.heappop(road_check)
    if visited[now]:
        continue
    visited[now] = True
    minmum_spanning_tree.append(dist)
    for next, d in roads[now]:
        if not visited[next]:
            heapq.heappush(road_check, (d, next))

print(sum(minmum_spanning_tree) - max(minmum_spanning_tree))
