"""
Title : 청소년 상어
Link : https://www.acmicpc.net/problem/19236
"""

import copy
import sys
input = sys.stdin.readline


def dfs(shark_now: list, fish_position_num: list, fish_position_dir: list, fish_num_position: list) -> int:
    global  directions
    fish_eaten = 0
    # 상어 위치에서 해당 방향으로 3칸 앞으로 가보기
    shark_dir = fish_position_dir[shark_now[0]][shark_now[1]]
    x, y = shark_now
    for d in range(1, 4):
        nx, ny = x + directions[shark_dir][0] * d, y + directions[shark_dir][1] * d
        # 더이상 진행할 수 없으면 종료
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            break
        # 아니라면 해당자리로 상어 옮기고 dfs탐색
        fish_num = fish_position_num[nx][ny]
        # 해당 자리에 물고기가 없을 때
        if fish_num == 0:
            continue
        fish_position_num[x][y] = 0
        fish_position_num[nx][ny] = 20
        fish_num_position[fish_num] = []
        eaten = dfs([nx, ny], *fish_move(fish_position_num, fish_position_dir, fish_num_position))
        fish_position_num[x][y] = 20
        fish_position_num[nx][ny] = fish_num
        fish_num_position[fish_num] = [nx, ny]
        if fish_num + eaten > fish_eaten:
            fish_eaten = fish_num + eaten
    return fish_eaten


def fish_move(fish_position_num, fish_position_dir, fish_num_position):
    global directions
    next_fish_position_num = copy.deepcopy(fish_position_num)
    next_fish_position_dir = copy.deepcopy(fish_position_dir)
    next_fish_num_position = copy.deepcopy(fish_num_position)
    for i in range(1, 17):
        if next_fish_num_position[i] == []:
            continue
        x, y = next_fish_num_position[i]
        d = next_fish_position_dir[x][y]
        # 이동할 방향 선정
        while True:
            nx, ny = x + directions[d][0], y + directions[d][1]
            # 범위를 벗어날 때
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or next_fish_position_num[nx][ny] == 20:
                d += 1
                if d == 9:
                    d = 1
            else:
                break
        # 해당 방향으로 이동 & 물고기 있으면 교환
        nearby_fish = next_fish_position_num[nx][ny]
        next_fish_position_num[x][y] = nearby_fish
        next_fish_position_num[nx][ny] = i
        next_fish_position_dir[x][y], next_fish_position_dir[nx][ny] = next_fish_position_dir[nx][ny], d
        next_fish_num_position[i] = [nx, ny]
        next_fish_num_position[nearby_fish] = [x, y]
    return next_fish_position_num, next_fish_position_dir, next_fish_num_position


# 각 자리 물고기 번호
fish_position_num = [[0] * 4 for _ in range(4)]
# 각 자리 물고기 방향
fish_position_dir = [[0] * 4 for _ in range(4)]
# 각 물고기 위치
fish_num_position = [[]] * 17

for i in range(4):
    arr = tuple(map(int, input().split()))
    for j in range(4):
        fish_position_num[i][j] = arr[j * 2]
        fish_num_position[arr[j * 2]] = [i, j]
        fish_position_dir[i][j] = arr[j * 2 + 1]

# 첫 자리는 상어가 먹고 시작
fish_score = fish_position_num[0][0]
shark_now = [0, 0]
# 물고기 먹힌거를 빈 리스트로 위치 표현
fish_num_position[fish_position_num[0][0]] = []
# 상어는 20으로 표현
fish_position_num[0][0] = 20

directions = [
    (), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
]

print(dfs(shark_now, *fish_move(fish_position_num, fish_position_dir, fish_num_position)) + fish_score)



'''
# WA
import copy
import sys
input = sys.stdin.readline


def dfs(i: int, j: int, fish: list):
    global fish_by_num, max_fish, direction
    # 상어 위치 i, j
    # 더 먹는 물고기
    additional_fish = 0
    # 상어 방향
    dx, dy = direction[fish[i][j * 2 + 1]]
    for k in range(1, 5):
        # 범위를 벗어나면 종료
        ni, nj = i + dx * k, j + dy * k
        if ni < 0 or ni >= 4 or nj < 0 or nj >=4 :
            break
        # 해당 위치에 물고기가 있을 때
        if fish[ni][nj * 2] > 0:
            # 상어가 이동할 위치 물고기 번호
            fish_num = fish[ni][nj * 2]
            fish_pos = [ni, nj]
            # 상어를 해당 위치로 이동
            fish[i][j * 2] = 0
            fish[ni][nj * 2] = 20
            fish_by_num[fish_num] = []
            # 추가 탐색
            more_additional_fish = dfs(ni, nj, fish_move(copy.deepcopy(fish)))
            # 상어 이동 복귀
            fish[i][j * 2] = 20
            fish[ni][nj * 2] = fish_num
            fish_by_num[fish_num] = fish_pos
            # 최댓값 비교
            if additional_fish < more_additional_fish + fish_num:
                additional_fish = more_additional_fish + fish_num
    return additional_fish


def fish_move(fish: list) -> list:
    # 물고기 이동
    global fish_by_num, direction
    for i in range(1, 17):
        # 물고기가 살아 있을 때
        if fish_by_num[i]:
            # 해당 물고기 위치, 방향
            x, y = fish_by_num[i]
            d = fish[x][y * 2 + 1]
            while True:
                # 해당 방향으로 움직일 수 있는지 확인
                nx, ny = x + direction[d][0], y + direction[d][1]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    fish_num = fish[nx][ny * 2]
                    # 해당 위치에 다른 물고기가 있거나, 비어 있다면
                    if fish_num <= 16:
                        # 빈 자리면 그대로 이동
                        if fish_num == 0:
                            fish[nx][ny * 2], fish[nx][ny * 2 + 1] = fish[x][y * 2], fish[x][y * 2 + 1]
                            fish[x][y * 2] = 0
                            # 물고기 정보 바꾸기
                            fish_by_num[i] = [nx, ny]
                        # 물고기가 있으면, 위치 교체
                        else:
                            fish[nx][ny * 2], fish[x][y * 2] = fish[x][y * 2], fish[nx][ny * 2]
                            fish[nx][ny * 2 + 1], fish[x][y * 2 + 1] = fish[x][y * 2 + 1], fish[nx][ny * 2 + 1]
                            # 두 물고기 정보 교환
                            fish_by_num[i] = [nx, ny]
                            fish_by_num[fish_num] = [x, y]
                        break
                d -= 1
                if d == 0:
                    d = 8
    return fish



# 물고기 번호, 방향
fish = [list(map(int, input().split())) for _ in range(4)]
# 물고기 번호별 위치 저장
fish_by_num = [[] for _ in range(17)]
for i in range(4):
    for j in range(4):
        fish_by_num[fish[i][j * 2]] = [i, j]
# 이동하는 8방향
direction = {
    1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1),
    5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)
}

# 상어는 20, 빈칸은 0으로 판별
fish_eaten_num = fish[0][0]
fish[0][0] = 20
fish_by_num[fish_eaten_num] = []

shark = [0, 0]

print(dfs(*shark, fish) + fish_eaten_num)
'''
