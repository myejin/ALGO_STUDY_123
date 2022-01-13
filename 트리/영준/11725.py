"""
Title : 트리의 부모 찾기
Link : https://www.acmicpc.net/problem/11725
"""

import sys, collections
input = sys.stdin.readline


def find_parent(tree: list, n: int) -> None:
    parents = [0] * (n + 1)
    parents[1] = -1
    queue = collections.deque([1])
    while queue:
        p = queue.popleft()
        for q in tree[p]:
            if not parents[q]:
                parents[q] = p
                queue.append(q)
    print(*parents[2:], sep = '\n')
    return

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

find_parent(tree, n)
