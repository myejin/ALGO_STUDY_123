import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temp = [[0]*m for _ in range(n)]
maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

result = 0


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if n > nx >= 0 and m > ny >=0 :
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def safe():
    safe_n = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe_n += 1

    return safe_n


def wall(count):
    global result
    if count == 3 :
        for i in range(n):
            for j in range(m):
                temp[i][j] = maps[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2 :
                    virus(i,j)

        result = max(safe(), result)
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0 :
                maps[i][j] = 1
                count += 1
                wall(count+1)
                maps[i][j] = 0
                count -= 1


wall(0)
print(result)