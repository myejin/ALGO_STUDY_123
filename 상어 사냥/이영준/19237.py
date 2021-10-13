"""
Title : 어른 상어
Link : https://www.acmicpc.net/problem/19237
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def shark_next_stage():
    '''
    상어들이 순서대로 이동
    1. sharks의 상어를 순서대로 이동(번호순서 정렬되어 있음)
    2. 이전 상어가 있는자리는 냄새가 남아 있어 가지 못하게
    2-1. 이동이 모두 끝나고 새로 이동한 자리에 냄새 뿌리기
    3. 더 높은 번호 상어가 이동할 때, 이전 자리에 번호 낮은 상어 있으면 넘어가기
    4. 상어 이동 후 기존 냄새 감소 & 새로운 냄새 추가
    '''
    global shark_grid, sharks, scent_grid
    # 개별 상어들 이동
    next_sharks = []
    for shark_info in sharks:
        next_shark_info = shark_move(shark_info)
        if next_shark_info:
            next_sharks.append(next_shark_info)
    sharks = next_sharks
    # 기존 냄새 감소
    scent_decrease()
    # 새로운 냄새 추가
    new_scent()


def shark_move(shark_info: list):
    global n, shark_grid, scent_grid, shark_move_priority, dx, dy
    shark_num, shark_pos, shark_dir = shark_info
    x, y = shark_pos
    # 지금 방향 기준으로, 4방향 탐색
    for d in shark_move_priority[shark_num - 1][shark_dir]:
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            # 해당칸에 냄새가 있으면 넘어가기
            if scent_grid[nx][ny]:
                continue
            # 다른 상어(번호 낮은 상어)가 있으면 빈 리스트로 리턴
            if 0 < shark_grid[nx][ny] < shark_num:
                shark_grid[x][y] = 0
                return []
            # 빈 자리라면 상어 이동 후 정보 갱신
            shark_grid[x][y] = 0
            shark_grid[nx][ny] = shark_num
            return [shark_num, (nx, ny), d]
    # 4방향 모두 냄새가 있는 칸인 경우
    # 다시 한 번 탐색해서, 냄새가 자기것이면 그 칸으로 이동
    for d in shark_move_priority[shark_num - 1][shark_dir]:
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if scent_grid[nx][ny][0] == shark_num:
                shark_grid[x][y] = 0
                shark_grid[nx][ny] = shark_num
                return [shark_num, (nx, ny), d]


def scent_decrease():
    global n, scent_grid
    for i in range(n):
        for j in range(n):
            if scent_grid[i][j]:
                # 냄새가 1일때와 아닐때
                if scent_grid[i][j][1] == 1:
                    scent_grid[i][j] = []
                else:
                    scent_grid[i][j][1] -= 1


def new_scent():
    global n, k, scent_grid, sharks
    for shark_num, shark_pos, _ in sharks:
        scent_grid[shark_pos[0]][shark_pos[1]] = [shark_num, k]


n, m, k = MIIS()
shark_grid = [list(map(int, input().split())) for _ in range(n)]
shark_direction = tuple(MIIS())
shark_move_priority = [[()] + [tuple(MIIS()) for _ in range(4)] for _ in range(m)]
dx, dy = (0, -1, 1, 0, 0), (0, 0, 0, -1, 1)

# 남아있는 상어 순서대로, 상어 번호, 위치, 방향
sharks = [[i, (), shark_direction[i - 1]] for i in range(1, m + 1)]

scent_grid = [[[] for _ in range(n)] for _ in range(n)]

# 최초 탐색, 상어 정보 저장
for i in range(n):
    for j in range(n):
        if shark_grid[i][j] != 0:
            sharks[shark_grid[i][j] - 1][1] = (i, j)
            scent_grid[i][j] = [shark_grid[i][j], k]

time = 0
while True:
    # 1000초가 넘어가는 경우
    if time > 1000:
        time = -1
        break
    if len(sharks) == 1:
        break
    # 상어 이동
    shark_next_stage()
    # 시간 증가
    time += 1

print(time)
