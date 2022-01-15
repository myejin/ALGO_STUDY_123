"""
Title : 전단지 돌리기
Link : https://www.acmicpc.net/problem/19542
"""

import sys
inpput = sys.stdin.readline
sys.setrecursionlimit(100_000)
MIIS = lambda: map(int, input().split())


def find_dist(current_node, previous_node):
    global N, S, D, graph, visited, result
    # visited[node]  = True
    count_dist = 0
    # for next_node in graph[node]:
    for next_node in graph[current_node]:
        if next_node == previous_node:
            continue
        dist = find_dist(next_node, current_node)
        if count_dist < dist:
            count_dist = dist
        # count_dist = max(count_dist, find_dist(next_node))
    if count_dist >= D:
        result += 1
    return count_dist + 1


N, S, D = MIIS()
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y =MIIS()
    graph[x].append(y)
    graph[y].append(x)

# visited = [False] * (N + 1)
result = 0
find_dist(S, -1)
print((result - 1) * 2 if result else 0)
