'''
Title : 마법사 상어와 비바라기
Link : https://www.acmicpc.net/problem/21610
'''

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def cloud_move_rain(magical_bucket:list, clouds_now: list, clouds: list, d: int, s: int):
    global n, dx, dy
    for x, y in clouds:
        x = (x + dx[d] * s) % n
        y = (y + dy[d] * s) % n
        # 구름 이동 적용
        clouds_now[x][y] = True
        # 비내리기
        magical_bucket[x][y] += 1


def water_copy_bug_and_make_cloud(magical_bucket: list, clouds_now: list, clouds: list) -> list:
    global n, dia_dx, dia_dy
    new_clouds = []    
    for i in range(n):
        for j in range(n):
            # 지금 위치가 이전 구름이 있었다면, 물복사 버그
            # 지금 구름이 있는지를 False로 만들고
            # 위쪽은 물 양이 있는지 & 새로 생긴 구름 있는지, 아래는 물 양만 확인
            if clouds_now[i][j]:
                water_bucket = 0
                # 위쪽 대각선
                for d in range(2):
                    nx, ny = i + dia_dx[d], j + dia_dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if magical_bucket[nx][ny] >= 1 or clouds_now[nx][ny]:
                            water_bucket += 1
                # 아래쪽 대각선
                for d in range(2, 4):
                    nx, ny = i + dia_dx[d], j + dia_dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if magical_bucket[nx][ny] >= 1:
                            water_bucket += 1
                magical_bucket[i][j] += water_bucket
            # 지금 위치에 이전 구름이 아니라면,
            # 물 양이 2이상이면 구름 생성, clouds_now의 해당 칸을 True로
            elif magical_bucket[i][j] >= 2:
                new_clouds.append([i, j])
                magical_bucket[i][j] -= 2
                clouds_now[i][j] = True
    return new_clouds


n, m = map(int, input().split())
magical_bucket = [list(map(int, input().split())) for _ in range(n)]

clouds = [ [n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]
dx, dy = (0, 0, -1, -1, -1, 0, 1, 1, 1), (0, -1, -1, 0, 1, 1, 1, 0, -1)
dia_dx, dia_dy = (-1, -1, 1, 1), (-1, 1, 1, -1)
for _ in range(m):
    clouds_now = [[False] * n for _ in range(n)]
    d, s = map(int, input().split())
    # 구름 이동 & 비내리기
    cloud_move_rain(magical_bucket, clouds_now, clouds, d, s)
    # 비 내리는 칸에서 물복사 버그 & 구름 생성
    clouds = water_copy_bug_and_make_cloud(magical_bucket, clouds_now, clouds)

# 380ms
print(sum([sum(line) for line in magical_bucket]))
# 376ms
print(sum(sum(magical_bucket, start=[])))
