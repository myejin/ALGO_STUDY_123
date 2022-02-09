import sys, copy
from itertools import combinations
input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

# 배양액 설정
def set_culture_medium():
    global new_garden
    for x, y in new_green_comb:
        new_garden[x][y] = 3
    for x, y in new_red_comb:
        new_garden[x][y] = 5

# 초록색 배양액 확산
def spread_green():
    global new_green_comb, new_garden, spread_check
    new_green = set()
    for x, y in new_green_comb:
        if new_garden[x][y] == 6:
            continue
        new_garden[x][y] = 4
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if new_garden[nx][ny] == 1 or new_garden[nx][ny] == 2:
                    spread_check = 1
                    new_garden[nx][ny] = 3
                    new_green.add((nx, ny))
    new_green_comb = set(new_green)

# 빨간색 배양액 확산
def spread_red():
    global new_red_comb, new_garden, flower_cnt, spread_check
    new_red = set()
    for x, y in new_red_comb:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if new_garden[nx][ny] == 1 or new_garden[nx][ny] == 2:
                    if spread_check == 1:
                        spread_check = 2
                    new_garden[nx][ny] = 5
                    new_red.add((nx, ny))
                elif new_garden[nx][ny] == 3:
                    new_garden[nx][ny] = 6
                    flower_cnt += 1
    new_red_comb = set(new_red)


N, M, G, R = MIIS()
garden = [list(MIIS()) for _ in range(N)]

dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
max_flower_cnt = 0  # 꽃의 최대 개수

# 배양액을 뿌릴 수 있는 땅
possible_land = set()
for x in range(N):
    for y in range(M):
        if garden[x][y] == 2:
            possible_land.add((x, y))
all_green_comb = set(combinations(possible_land, G))  # 초록색 배양액을 뿌리는 조합

# 초록색 배양액 조합에 따라
for green_comb in all_green_comb:
    # 빨간색 배양액 조합
    all_red_comb = set(combinations(possible_land - set(green_comb), R))
    # 초록색, 빨간색 배양액 조합에 따라 결과 계산
    for red_comb in all_red_comb:
        new_green_comb = set(green_comb)
        new_red_comb = set(red_comb)
        new_garden = copy.deepcopy(garden)  # 구현을 진행할 새로운 가든
        set_culture_medium()
        flower_cnt = 0
        # 배양액 확산
        while True:
            spread_check = 0
            spread_green()
            spread_red()
            # 배양액이 하나라도 확산되지 않을 경우 중지
            if spread_check < 2:
                break
        max_flower_cnt = max(max_flower_cnt, flower_cnt)

print(max_flower_cnt)