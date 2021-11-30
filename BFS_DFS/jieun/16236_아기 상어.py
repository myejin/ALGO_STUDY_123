import sys
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    global ans
    global baby_shark
    start_y, start_x = y, x
    # 아기 상어 위치 0으로 초기화
    maps[start_y][start_x] = 0
    # 먹은 물고기 수
    eat = 0
    while True:
        # q에 아기상어 위치, 거리 저장
        q = deque([[start_y, start_x, 0]])
        # 물고기 위치 저장
        fish_pos = []
        # 가까운 몰고기 거리 저장 (일단 최대로 초기화)
        fish_dist = n*n+1
        # 새로운 아기 상어 위치마다 visited 배열 초기화
        visited = [[0]*n for _ in range(n)]
        visited[start_y][start_x] = 1
        while q:
            r, c, dist = q.popleft()
            for k in range(4):
                ny = r + dy[k]
                nx = c + dx[k]
                # 맵을 벗어나지 않고, 방문하지 않았으며, 아기상어 크기보다 크거나 같을 경우
                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and maps[ny][nx] <= baby_shark:
                    # 일단 방문
                    visited[ny][nx] = 1
                    # 만약 아기상어와 크기가 같거나, 물고기가 없음
                    # 그리고 그곳으로 도달하는 거리가 현 상태에서 먹을 수 있는 물고기의 거리보다 작을 경우
                    if (maps[ny][nx] == baby_shark or not maps[ny][nx]) and fish_dist > dist + 1:
                        q.append([ny, nx, dist+1])
                    # 만약 먹을 수 있는 물고기일 경우
                    if 0 < maps[ny][nx] < baby_shark:
                        # 현재 저장된 물고기 거리가 지금 거리보다 멀 경우
                        if fish_dist > dist+1:
                            fish_dist = dist+1
                            fish_pos = [[ny, nx]]
                        # 현재 저장된 물고기 거리와 지금 거리가 같을 경우
                        elif fish_dist == dist + 1:
                            fish_pos.append([ny, nx])
        # while 문 탈출 후 (먹을 수 있는 물고기 탐색 완료 후)
        # 먹을 수 있는 물고기가 있을 경우
        if len(fish_pos) > 0:
            # 거리가 가까운 물고기 많다면 가장 위, 왼쪽에 있는 물고기 먹기
            fish_pos.sort()
            # sort 후 가장 첫번째 물고기 먹음
            ny, nx = fish_pos[0]
            # 물고기까지의 거리 저장 (지난 시간 == 물고기와의 거리)
            ans += fish_dist
            # 먹은 물고기 추가
            eat += 1
            # 먹은 물고기 없애줌
            maps[ny][nx] = 0
            # 만약 아기상어 크기와 먹은 물고기 수가 같다면
            if eat == baby_shark:
                baby_shark += 1
                eat = 0
            # 아기 상어 위치 갱신
            start_y = ny
            start_x = nx
        # 없으면 엄마상어에게 도움 요청 (함수 탈출!)
        else:
            return


n = int(input())
# 1, 2, 3, 4, 5, 6 : 물고기 크기
# 9 아기 상어 위치
maps = [list(map(int, input().split())) for _ in range(n)]
baby_shark = 2
ans = 0

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            bfs(i, j)
            break


print(ans)
