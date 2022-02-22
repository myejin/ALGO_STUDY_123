"""
Title : 도시 건설
Link : https://www.acmicpc.net/problem/21924
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def solution() -> int:
    N, M = MIIS()
    parents = [i for i in range(N + 1)]
    roads = sorted([tuple(MIIS()) for _ in range(M)], key=lambda x: x[2])

    ans = 0
    for a, b, c in roads:
        a, b = find_parent(parents, a), find_parent(parents, b)
        if a == b:
            ans += c
        else:
            parents = union_parent(parents, a, b)

    for i in range(2, N + 1):
        if find_parent(parents, i) != 1:
            return -1
    return ans


def find_parent(parents, x):
    while x != parents[x]:
        x = parents[x]
    return x


def union_parent(parents, x, y):
    if x > y:
        x, y = y, x
    parents[y] = x
    return parents


print(solution())
