import sys
from collections import deque
input = sys.stdin.readline


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))


while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny >= 0 and ny < n and nx >=0 and nx < m and tomato[ny][nx] == 0 :
            tomato[ny][nx] = tomato[y][x] + 1
            q.append((ny, nx))

flag = False
max_tomato = -2
for i in tomato:
    for j in i:
        if j == 0 :
            flag=True
        max_tomato = max(j, max_tomato)

if flag :
    print(-1)
elif max_tomato == -1:
    print(0)
else:
    print(max_tomato - 1)



