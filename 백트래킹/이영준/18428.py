"""
Title : 감시 피하기
Link : https://www.acmicpc.net/problem/18428
"""

def dfs(obstacles: list, x: int, y: int) -> None:
    global n, hall, count, row, col, able
    if len(obstacles) == 3:
        if check_obstacles():
            able = True
        return
    if y == n:
        x += 1
        y = 0
    if x == n:
        return
    # 해당 행 / 열 확인
    if not row[x] and not col[y]:
        y += 1
    # 장애물 설치
    if hall[x][y] == 'X':
        hall[x][y] = 'O'
        obstacles.append((x, y))
        dfs(obstacles, x, y + 1)
        obstacles.pop()
        hall[x][y] = 'X'
    dfs(obstacles, x, y + 1)


def check_obstacles() -> bool:
    global n, hall, teachers
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    for x, y in teachers:
        for d in range(4):
            k = 1
            while True:
                nx, ny = x + dx[d] * k, y + dy[d] * k
                if 0 <= nx < n and 0 <= ny < n:
                    if hall[nx][ny] == 'S':
                        return False
                    elif hall[nx][ny] == 'X':
                        k += 1
                        continue
                    else:
                        break
                else:
                    break
    return True


n = int(input())
hall = [list(map(str ,input().split())) for _ in range(n)]

col = [False] * n
row = [False] * n
teachers = []
for i in range(n):
    for j in range(n):
        if hall[i][j] == 'T':
            teachers.append((i, j))
            row[i] = True
            col[j] = True

count = 0

able = False

dfs([], 0, 0)
if able:
    print('YES')
else:
    print('NO')