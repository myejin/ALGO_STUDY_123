from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]


def dfs(y, x):
    global grid
    grid[y][x] = 1
    q = deque([(y, x)])

    while q :
        a, b = q.popleft()
        if a==gy and b==gx :
            print(grid[a][b]-1)
            return

        for i in range(8):
            ny, nx = a+dy[i], b+dx[i]
            if 0<=ny<l and 0<=nx<l and not grid[ny][nx]:
                q.append((ny, nx))
                grid[ny][nx] = grid[a][b] + 1


T = int(input())
for tc in range(T):
    l = int(input())
    grid = [[0]*l for _ in range(l)]
    #현재칸
    cy, cx = map(int, input().split())
    # 가려는 칸
    gy, gx = map(int, input().split())
    dfs(cy, cx)
