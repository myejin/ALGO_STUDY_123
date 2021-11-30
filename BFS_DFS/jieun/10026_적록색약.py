import sys
input = sys.stdin.readline
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def not_color_blind(y, x):
    check = area[y][x]
    q = deque([(y, x)])
    visited1[y][x] = 1
    while q:
        cy, cx = q.popleft()
        for k in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0<=ny<n and 0<=nx<n and area[ny][nx] not visited1[ny][nx]

n = int(input())
area = [list(input()) for _ in range(n)]

# 적록색약 아님
visited1 = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            cnt += 1

print(cnt, end=' ')

# 적록색약임
visited2 = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            cnt += 1
            while q:

print(cnt)

