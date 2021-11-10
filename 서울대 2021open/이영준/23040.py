"""
Title : 누텔라 트리 (Easy)
Link : https://www.acmicpc.net/problem/23040
"""

from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

edges_color = ' ' + input().strip()
blacks = []
# 빨간 점 기준으로 Union
reds_parent = list(range(N + 1))
# 빨간 점들의 집합 크기
reds_group_size = [0] * (N + 1)

for i in range(1, N + 1):
    # 검은색 점은 따로 보관
    if edges_color[i] == 'B':
        blacks.append(i)
    # 빨간 점이라면 Union
    elif reds_parent[i] == i:
        # 시작점을 기준으로 인접 빨간점 모두 탐색
        # & 부모로 i로 지정
        queue = deque([i])
        red_group = {i}
        while queue:
            x = queue.popleft()
            for y in graph[x]:
                if edges_color[y] == 'R' and y not in red_group:
                    red_group.add(y)
                    queue.append(y)
        group_size = len(red_group)
        for x in red_group:
            reds_group_size[x] = group_size
            reds_parent[x] = i

count = 0
for x in blacks:
    for y in graph[x]:
        count += reds_group_size[y]

print(count)


'''
Counter Example
8
1 2
2 3
3 4
1 5
5 6
6 7
5 8
BRRRBRRR
ans : 6
'''