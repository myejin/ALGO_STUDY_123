from collections import deque
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def move():
    new_arr = [[deque() for _ in range(n)] for _ in range(n)]
    for mi in range(n):
        for mj in range(n):
            if grid[mi][mj]:
                n_grid = len(grid[mi][mj])
                for _ in range(n_grid):
                    mt, st, dt = grid[mi][mj].pop()
                    ny = (mi + dy[dt] * st) % n
                    nx = (mj + dx[dt] * st) % n
                    new_arr[ny][nx].append([mt, st, dt])
    return new_arr


n, m, k = map(int, input().split())
grid = [[deque() for _ in range(n)] for _ in range(n)]
q = deque([])
for _ in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    grid[ri-1][ci-1].append([mi, si, di])


for _ in range(k):
    grid = move()
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) >= 2:
                fire_ball_n = len(grid[i][j])
                new_m = 0
                new_s = 0
                flag = 0
                for _ in range(fire_ball_n):
                    temp = grid[i][j].popleft()
                    new_m += temp[0]
                    new_s += temp[1]
                    if temp[2] % 2:
                        flag += 1
                new_m //= 5
                new_s //= fire_ball_n
                if not new_m:
                    continue
                if flag % fire_ball_n:
                    for t in [1, 3, 5, 7]:
                        grid[i][j].append([new_m, new_s, t])
                else:
                    for t in [0, 2, 4, 6]:
                        grid[i][j].append([new_m, new_s, t])
answer = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            for tm, _, _ in grid[i][j]:
                answer += tm

print(answer)
