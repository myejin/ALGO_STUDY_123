import sys
from collections import deque
input = sys.stdin.readline

# 현재 지점부터 연결되어 있는 공기를 2로 변환
def air_check(x, y):
    global grid
    deq = deque()
    deq.append([x, y])
    grid[x][y] = 2
    while deq:
        x, y = deq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                deq.append([nx, ny])


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

all_cheese = []  # 치즈의 위치를 저장
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
result = 0

# 초기의 바깥 공기를 2로 변환
air_check(0, 0)

# 치즈의 위치를 모두 저장
for x in range(N):
    for y in range(M):
        if grid[x][y] == 1:
            all_cheese.append([x, y])

time = 0
while True:
    melted_cheese = []
    cheese_exist = False
    # 공기가 2개 이상 닿아 녹을 치즈를 저장
    for x, y in all_cheese:
        if grid[x][y] == 1:
            cheese_exist = True
            air = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if grid[nx][ny] == 2:
                    air += 1
            if air >= 2:
                melted_cheese.append([x, y])
    # 녹은 치즈부터 공기로 변환
    for x, y in melted_cheese:
        air_check(x, y)
    # 녹을 치즈가 없을 경우
    if not cheese_exist:
        print(time)
        break
    time += 1