"""
Title : 세부
Link : https://www.acmicpc.net/problem/13905
"""

from collections import deque
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def solution() -> int:
    N, M = MIIS()
    S, E = MIIS()
    bridges = [[] for _ in range(N + 1)]
    for _ in range(M):
        h1, h2, k = MIIS()
        bridges[h1].append((h2, k))
        bridges[h2].append((h1, k))

    minimum, maximum = 1, 1_000_000
    ans = 0
    while minimum <= maximum:
        mid = (minimum + maximum) // 2
        if bin_search(bridges, mid, N, S, E):
            minimum = mid + 1
            ans = mid
        else:
            maximum = mid - 1
    return ans


def bin_search(bridges, limit, N, S, E):
    queue = deque([S])
    visited = [False] * (N + 1)
    while queue:
        x = queue.popleft()
        if x == E:
            return True
        if visited[x]:
            continue
        visited[x] = True
        for y, c in bridges[x]:
            if visited[y] or c < limit:
                continue
            queue.append(y)
    return False


print(solution())
