import sys
from collections import deque
input = sys.stdin.readline

dy = [0, -1, 1, 0]
dx = [1, 0, 0, -1]


def bfs(y, x):
    global grid
    stack = deque([(y, x)])
    while stack:
        cy, cx = stack.popleft()
        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]
            if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] == '#':
                stack.append((ny, nx))
                grid[ny][nx] = '.'


T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                bfs(i, j)
                cnt += 1
    print(cnt)