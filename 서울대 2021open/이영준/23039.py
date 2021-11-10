"""
Title : 실 전화기
Link : https://www.acmicpc.net/problem/23039
"""

import sys
input = sys.stdin.readline


def is_planar_graph(graph: list) -> bool:
    # 내부 교차점이 있는지 확인
    if 5 in graph[2] and (3 in graph[1] or 4 in graph[1]):
        return False
    if 4 in graph[2] and (1 in graph[3] or 5 in graph[3]):
        return False
    if 5 in graph[3] and 4 in graph[1]:
        return False
    return True


def one_point_except_planar(graph: list) -> bool:
    # 1 ~ 5번점을 하나씩 제외하며 평면 그래프가 되는지 확인
    # 직접 점을 제거하는 대신, 한 점이 없다면 == 점이 4개라면 내부 교차점은 최대 1개
    if (4 in graph[2] and 5 in graph[3]) and\
        (4 in graph[1] and 5 in graph[3]) and\
        (4 in graph[1] and 5 in graph[2]) and\
        (3 in graph[1] and 5 in graph[2]) and\
        (3 in graph[1] and 4 in graph[2]):
        return False
    return True


N = int(input())
graph = [[] for _ in range(6)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


if N == 10:
    print(-1)
# 이미 평면 그래프일 때
elif N == 1 or is_planar_graph(graph):
    print(0)
# 한마리 옮겨서 가능
# 해당 정점 제외 평면 그래프일 때
elif one_point_except_planar(graph):
    print(1)
# 두마리 올겨서 가능
# 나머지 모든 경우 / 3마리 옮겨서 가능 == 2마리 옮겨서 가능
else:
    print(2)
