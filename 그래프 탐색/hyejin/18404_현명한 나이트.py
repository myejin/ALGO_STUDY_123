from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

N, M = map(int, input().split())  # 500 / 1000
X, Y = map(int, input().split())

board = [[0] * N for _ in range(N)]
board[X - 1][Y - 1] = 'K'

Es = {}
for _ in range(M):
    A, B = map(int, input().split())
    board[A - 1][B - 1] = 'E'
    Es[(A - 1, B - 1)] = 0

visit = [[0] * N for _ in range(N)]
visit[X - 1][Y - 1] = 1

q = deque([[X - 1, Y - 1]])

while q:
    i, j = q.popleft()

    if not M:
        break

    for d in range(8):
        x = i + dx[d]
        y = j + dy[d]
        if 0 <= x < N and 0 <= y < N and not visit[x][y]:
            visit[x][y] = visit[i][j] + 1
            q.append([x, y])

            if (x, y) in Es:
                Es[(x, y)] = visit[x][y]
                M -= 1

for v in Es.values():
    print(v - 1, end=' ')
print()
