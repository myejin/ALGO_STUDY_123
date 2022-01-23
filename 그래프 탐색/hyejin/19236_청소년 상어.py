import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def find_fish(arr, target):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == target:
                return (i, j)
    return None


def move_fish(arr, sx, sy):
    for i in range(1, 17):
        pos = find_fish(arr, i)
        if pos is None:
            continue

        x, y = pos
        d = arr[x][y][1]
        for _ in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4 and (sx, sy) != (nx, ny):
                arr[x][y][0], arr[nx][ny][0] = arr[nx][ny][0], arr[x][y][0]
                arr[x][y][1], arr[nx][ny][1] = arr[nx][ny][1], d
                break
            d = (d + 1) % 8


def dfs(arr, x, y, fish_cnt):
    global answer
    arr = copy.deepcopy(arr)

    fish, d = arr[x][y]
    arr[x][y][0] = -1  # 잡아먹혔다.
    answer = max(answer, fish_cnt + fish)

    move_fish(arr, x, y)

    p, q = x, y
    for _ in range(4):
        p += dx[d]
        q += dy[d]
        if 0 <= p < 4 and 0 <= q < 4 and arr[p][q][0] != -1:
            dfs(arr, p, q, fish_cnt + fish)


if __name__ == '__main__':
    init = [[None] * 4 for _ in range(4)]
    for i in range(4):
        tmp = list(map(int, input().split()))
        for j in range(4):
            init[i][j] = [tmp[j * 2], tmp[j * 2 + 1] - 1]

    answer = 0
    dfs(init, 0, 0, 0)
    print(answer)
