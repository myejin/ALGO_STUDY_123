"""
Title : 상어 중학교
Link : https://www.acmicpc.net/problem/21609
"""

import collections
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_max_block_group(n: int, blocks: list) -> int:
    # 가장 큰 그룹의 크기
    maximum_group_size = 0
    # 가장 큰 그룹에 속한 무지개 블록
    maximum_group_size_rainbow = 0
    # 가장 큰 그룹의 기준 블록
    maximum_group_standard_block = []
    # 방문 확인
    visited = [[False] * n for _ in range(n)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            if blocks[i][j] > 0 and not visited[i][j]:
                # 지금 그룹의 블록 색
                color_now = blocks[i][j]
                # 지금 그룹의 블록 개수
                blocks_count = 0
                # 지금 그룹의 무지개 블록
                rainbow_blocks = set()
                # 지금 그룹의 기준 블록
                standard_block = [i, j]
                queue = collections.deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    # 두가지로 나누어 탐색
                    if blocks[x][y] == 0 and (x, y) not in rainbow_blocks:
                        rainbow_blocks.add((x, y))
                    elif blocks[x][y] == color_now and not visited[x][y]:
                        visited[x][y] = True
                        blocks_count += 1
                        # 기준 블록인지 확인 / 행, 열 번호 작은 순
                        if x < standard_block[0] or (x == standard_block[0] and y < standard_block[1]):
                            standard_block = [x, y]
                    else:
                        continue
                    # 추가적 주변 블록 탐색
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if blocks[nx][ny] == 0 and (nx, ny) not in rainbow_blocks:
                                queue.append((nx, ny))
                            elif blocks[nx][ny] == color_now and not visited[nx][ny]:
                                queue.append((nx, ny))
                # 탐색 종료 / 선택할 블록인지 확인
                rainbow_blocks = len(list(rainbow_blocks))
                if verify(maximum_group_size, blocks_count, maximum_group_size_rainbow,\
                        rainbow_blocks, maximum_group_standard_block, standard_block):
                    maximum_group_size = blocks_count
                    maximum_group_size_rainbow = rainbow_blocks
                    maximum_group_standard_block = standard_block
    # 블록 그룹에 2개 이상 있어야 함
    if maximum_group_size + maximum_group_size_rainbow < 2:
        return 0
    else:
        # 기준 블록 기준으로 빈 공간으로 바꾸기
        change_block(n, blocks, maximum_group_standard_block)
        # 제거한 블록 수 리턴
        return maximum_group_size + maximum_group_size_rainbow


def verify(count_before, count_after, rainbow_before, rainbow_after, standard_before, standard_after):
    # 새로 찾은 구역을 선택하는지 확인하는 함수
    if count_before + rainbow_before < count_after + rainbow_after:
        return True
    elif count_before + rainbow_before == count_after + rainbow_after:
        if rainbow_before < rainbow_after:
            return True
        elif rainbow_before == rainbow_after:
            # 문제 기준 행, 열 크다면 선택
            if standard_before[0] < standard_after[0] or (standard_before[0] == standard_after[0] and standard_before[1] < standard_after[1]):
                return True
    return False


def change_block(n: int, blocks: list, standard: list):
    # 기준블록에서 탐색하며 바꾸기
    visited = [[False] * n for _ in range(n)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    queue = collections.deque([standard])
    color = blocks[standard[0]][standard[1]]
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        blocks[x][y] = -2
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and (blocks[nx][ny] == 0 or blocks[nx][ny] == color):
                    queue.append((nx, ny))


def gravity(n: int, blcoks: list):
    for j in range(n):
        bottom = top = n - 1
        while top >= 0 and bottom >= 0:
            # bottom을 먼저 빈 공간으로 올려주기
            # top이 더 밑에 있다면 bottom 바로 위 칸으로
            # top이 더 위에 있다면 top을 올리면서 탐색
            # bottom이나 top중에서 -1을 만나면 둘 다 올리기
            if blocks[top][j] == -1:
                bottom = top = top - 1
            elif blocks[bottom][j] == -1:
                bottom = top = bottom - 1
            elif blocks[bottom][j] != -2:
                bottom -= 1
            elif blocks[bottom][j] == -2:
                if top >= bottom:
                    top = bottom - 1
                elif blcoks[top][j] == -2:
                    top -= 1
                else:
                    blocks[bottom][j], blocks[top][j] = blocks[top][j], blocks[bottom][j]
                    bottom -= 1
                    top -= 1


def rotate(n: int, blocks: list) -> list:
    new_blocks = list(zip(*blocks))[::-1]
    return [list(line) for line in new_blocks]


n, m = MIIS()
# -1 검은색, 0 무지개, -2 빈공간
blocks = [list(MIIS()) for _ in range(n)]

score = 0

while True:
    # 제거하여 점수 얻을 블록 선택
    block_point = find_max_block_group(n, blocks)
    if block_point == 0:
        break
    score += block_point ** 2
    # 중력 작용
    gravity(n, blocks)
    # 90도 반시계 회전
    blocks = rotate(n, blocks)
    # 중력 작용
    gravity(n, blocks)

print(score)
