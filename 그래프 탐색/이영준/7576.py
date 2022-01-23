"""
Title : 토마토
Link : https://www.acmicpc.net/problem/7576
"""

import sys, collections
input = sys.stdin.readline


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

unripe_tomato_count = 0
ripe_tomato = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            unripe_tomato_count += 1
        elif tomato[i][j] == 1:
            ripe_tomato.append((i, j, 0))

queue = collections.deque(ripe_tomato)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
min_day = 0
while queue:
    x, y, day = queue.popleft()
    if day > min_day:
        min_day = day
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if not tomato[nx][ny]:
                tomato[nx][ny] = 1
                unripe_tomato_count -= 1
                queue.append((nx, ny, day + 1))

if unripe_tomato_count:
    print(-1)
else:
    print(min_day)
