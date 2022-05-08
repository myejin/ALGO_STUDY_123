"""
Title : 학교 탐방하기
Link : https://www.acmicpc.net/problem/13418
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_parent(x, parents):
    while x != parents[x]:
        x = parents[x]
    return x


def union_parent(x, y, parents):
    if x > y:
        x, y = y, x
    parents[y] = x
    return parents


def kruskal(roads):
    global N
    ans = 0
    parents = list(range(N + 1))
    for a, b, c in roads:
        a, b = find_parent(a, parents), find_parent(b, parents)
        if a == b:
            continue
        parents = union_parent(a, b, parents)
        ans += 1 ^ c
    return ans


if __name__ == "__main__":
    N, M = MIIS()
    roads = [tuple(MIIS()) for _ in range(M + 1)]
    
    roads.sort(key=lambda x: x[2])
    max_val = kruskal(roads)
    roads.sort(key=lambda x: -x[2])
    min_val = kruskal(roads)
    print(max_val * max_val - min_val * min_val)
