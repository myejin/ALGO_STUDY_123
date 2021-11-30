import sys
from copy import deepcopy
input = sys.stdin.readline

N, M, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
time = 0
shark_priority = [[] for _ in range(M+1)]
# 1: 위, 2: 아래, 3: 왼쪽, 4 : 오른쪽
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
shark_dir = list(map(int, input().split()))
for i in range(1, M+1):
    shark_priority[i] = [list(map(int, input().split())) for _ in range(4)]

smell = [[[-1, 0] for _ in range(N)] for _ in range(N)]
isFalse = False
left_shark = M

while True:
    if left_shark == 1:
        break

    if time >= 1000:
        isFalse = True
        break

    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                smell[i][j] = [k, grid[i][j]]

    new_grid = deepcopy(grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                now_shark = grid[i][j]
                now_dir = shark_dir[now_shark-1]
                for d in shark_priority[now_shark][now_dir-1]:
                    ny = i + dy[d-1]
                    nx = j + dx[d-1]
                    if 0 <= ny < N and 0 <= nx < N and smell[ny][nx] == [-1, 0]:
                        if new_grid[ny][nx] == 0 :
                            new_grid[ny][nx] = now_shark
                            new_grid[i][j] = 0
                        else:
                            if new_grid[ny][nx] > now_shark:
                                new_grid[ny][nx] = now_shark
                            left_shark -= 1
                            new_grid[i][j] = 0
                        shark_dir[now_shark-1] = d
                        break
                else: # 냄새가 없는 칸이 하나도 없을 경우
                    for d in shark_priority[now_shark][now_dir-1]:
                        ny = i + dy[d - 1]
                        nx = j + dx[d - 1]
                        if 0 <= ny < N and 0 <= nx < N and smell[ny][nx][1] == now_shark:
                            new_grid[ny][nx] = now_shark
                            new_grid[i][j] = 0
                            shark_dir[now_shark - 1] = d
                            break

    grid = deepcopy(new_grid)

    # 냄새 줄여주기
    for i in range(N):
        for j in range(N):
            if smell[i][j][0] != -1:
                smell[i][j][0] -= 1
            if smell[i][j][0] == 0:
                smell[i][j] = [-1, 0]

    time += 1

if isFalse:
    print(-1)

else:
    print(time)
