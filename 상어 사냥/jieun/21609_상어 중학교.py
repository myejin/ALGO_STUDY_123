from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def find_big_block():
    block_r = -1
    block_c = -1
    block_size = -1
    block_rainbow = -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 1:

                temp_r, temp_c, temp_size, temp_rainbow = count_block(i, j)

                if temp_size > block_size:
                    block_size = temp_size
                    block_rainbow = temp_rainbow
                    block_r = temp_r
                    block_c = temp_c
                elif temp_size == block_size:
                    if block_rainbow < temp_rainbow:
                        block_size = temp_size
                        block_rainbow = temp_rainbow
                        block_r = temp_r
                        block_c = temp_c
                    elif block_rainbow == temp_rainbow:
                        if block_r < temp_r:
                            block_r = temp_r
                            block_c = temp_c
                        elif block_r == temp_r:
                            if block_c < temp_c:
                                block_c = temp_c

    return block_r, block_c, block_size


def count_block(r, c):
    gizoon_r = r
    gizoon_c = c
    rainbow = 0
    q = deque([(r, c)])
    my_size = 1
    visited = [[0]*n for _ in range(n)]
    visited[r][c] = 1
    my_color = grid[r][c]
    while q:
        now_r, now_c = q.popleft()
        for k in range(4):
            nr = now_r + dy[k]
            nc = now_c + dx[k]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and (grid[nr][nc] == 0 or grid[nr][nc] == my_color):
                visited[nr][nc] = 1
                my_size += 1
                q.append((nr, nc))
                if not grid[nr][nc]:
                    rainbow += 1
                else:
                    if gizoon_r > nr:
                        gizoon_r = nr
                        gizoon_c = nc
                    elif gizoon_r == nr and gizoon_c > nc:
                        gizoon_c = nc
    if my_size >= 2 :
        return gizoon_r, gizoon_c, my_size, rainbow
    else :
        return -1, -1, -1, -1


def delete_block(r, c):
    q = deque([(r, c)])
    my_size = 1
    visited = [[0] * n for _ in range(n)]
    visited[r][c] = 1
    my_color = grid[r][c]
    grid[r][c] = -2
    while q:
        now_r, now_c = q.popleft()
        for k in range(4):
            nr = now_r + dy[k]
            nc = now_c + dx[k]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and (grid[nr][nc] == 0 or grid[nr][nc] == my_color):
                visited[nr][nc] = 1
                my_size += 1
                q.append((nr, nc))
                grid[nr][nc] = -2
    return my_size


def gravity():
    for i in range(n-2, -1, -1):
        for j in range(n):
            if grid[i][j] >= 0 and grid[i+1][j] == -2:
                ny = 0
                flag = 0
                for k in range(i+1, n):
                    ny = k
                    if grid[k][j] > -2:
                        flag = 1
                        break
                if flag:
                    grid[ny-1][j] = grid[i][j]
                else :
                    grid[ny][j] = grid[i][j]
                grid[i][j] = -2


def rotate():
    global grid
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-1-j][i] = grid[i][j]
    grid = temp


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
idx = 0
answer = 0
while True:
    y, x, size = find_big_block()
    if size < 2 :
        break
    score = delete_block(y, x)
    answer += score**2
    gravity()
    rotate()
    gravity()

print(answer)