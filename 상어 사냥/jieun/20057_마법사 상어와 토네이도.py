import sys

def tornado(x, y, sand):
    global ans
    if 0 <= x < n and 0 <= y < n:
        a[x][y] += sand
    else:
        ans += sand

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
x, y = n // 2, n // 2

i, cnt, ans, move, turn = 0, 0, 0, 0, 1
while True:
    nx = x + dx[i]
    ny = y + dy[i]
    if a[nx][ny]:
        p1 = int(a[nx][ny] * 0.01)
        p2 = int(a[nx][ny] * 0.02)
        p7 = int(a[nx][ny] * 0.07)
        p5 = int(a[nx][ny] * 0.05)
        p10 = int(a[nx][ny] * 0.1)
        rem = a[nx][ny] - 2 * (p1 + p2 + p7 + p10) - p5

        p1x_u, p1y_u = x + dx[(i + 3) % 4], y + dy[(i + 3) % 4]
        p1x_d, p1y_d = x + dx[(i + 1) % 4], y + dy[(i + 1) % 4]
        p2x_u, p2y_u = nx + 2 * dx[(i + 3) % 4], ny + 2 * dy[(i + 3) % 4]
        p2x_d, p2y_d = nx + 2 * dx[(i + 1) % 4], ny + 2 * dy[(i + 1) % 4]
        p7x_u, p7y_u = nx + dx[(i + 3) % 4], ny + dy[(i + 3) % 4]
        p7x_d, p7y_d = nx + dx[(i + 1) % 4], ny + dy[(i + 1) % 4]

        tx, ty = nx + dx[i], ny + dy[i]
        p10x_u, p10y_u = tx + dx[(i + 3) % 4], ty + dy[(i + 3) % 4]
        p10x_d, p10y_d = tx + dx[(i + 1) % 4], ty + dy[(i + 1) % 4]
        p5x, p5y = tx + dx[i], ty + dy[i]

        tornado(tx, ty, rem)
        tornado(p1x_u, p1y_u, p1)
        tornado(p1x_d, p1y_d, p1)
        tornado(p2x_u, p2y_u, p2)
        tornado(p2x_d, p2y_d, p2)
        tornado(p7x_u, p7y_u, p7)
        tornado(p7x_d, p7y_d, p7)
        tornado(p10x_u, p10y_u, p10)
        tornado(p10x_d, p10y_d, p10)
        tornado(p5x, p5y, p5)

    if nx == 0 and ny == 0:
        break

    a[nx][ny] = 0
    x, y = nx, ny
    cnt += 1
    if cnt == turn:
        i = (i + 1) % 4
        cnt = 0
        move += 1
        if move % 2 == 0:
            turn += 1
            move = 0

print(ans)