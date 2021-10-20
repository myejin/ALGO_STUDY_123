"""
Title : 여러분의 다리가 되어 드리겠습니다
Link : https://www.acmicpc.net/problem/17352
"""

import sys
input = sys.stdin.readline


def find_parent(x: int, parent: list) -> int:
    while x != parent[x]:
        x = parent[x]
    return x


n = int(input())

parents = list(range(n + 1))
for _ in range(n - 2):
    x, y = map(int, input().split())
    x_p, y_p = find_parent(x, parents), find_parent(y, parents)
    if x_p < y_p:
        parents[y_p] = x_p
    else:
        parents[x_p] = y_p

ans = set(find_parent(i, parents) for i in range(1, n + 1))

print(*ans)

'''
Counter Example
8
1 2
3 4
3 5
7 8
6 7
5 2
ans : 1 6
'''