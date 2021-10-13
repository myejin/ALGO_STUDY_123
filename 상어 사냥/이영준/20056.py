"""
Title : 마법사 상어와 파이어볼
Link : https://www.acmicpc.net/problem/20056
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def move_fireballs(magical_map: list) -> list:
    global n, dx, dy
    next_magical_map = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for m, s, d in magical_map[i][j]:
                ni, nj = (i + dx[d] * s) % n, (j + dy[d] * s) % n
                next_magical_map[ni][nj].append((m, s, d))
    return next_magical_map


def explode_fireballs(magical_map: list) -> list:
    global n
    next_magical_map = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(magical_map[i][j]) < 2:
                next_magical_map[i][j] = magical_map[i][j][::]
            else:
                # 해당 파이어볼 총 질량
                total_weights = 0
                total_speed = 0
                check_direction = []
                for m, s, d in magical_map[i][j]:
                    total_weights += m
                    total_speed += s
                    check_direction.append(d % 2)
                weight = total_weights // 5
                if weight == 0:
                    continue
                speed = total_speed // len(magical_map[i][j])
                # 방향 결정
                if all(check_direction) or not any(check_direction):
                    next_direction = [0, 2, 4, 6]
                else:
                    next_direction = [1, 3, 5, 7]
                # 다음 파이어볼 설정
                for d in next_direction:
                    next_magical_map[i][j].append((weight, speed, d))
    return next_magical_map


def count_fireballs(magical_map: list) -> int:
    global n
    fireballs = 0
    for i in range(n):
        for j in range(n):
            for m, *_ in magical_map[i][j]:
                fireballs += m
    return fireballs


n, m, k = MIIS()
magical_map = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = MIIS()
    magical_map[r - 1][c - 1].append((m, s, d))

dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
for _ in range(k):
    # 모든 파이어볼 이동
    magical_map = move_fireballs(magical_map)
    # 한 칸에 파이어볼 2개 이상이면 나누어지고 다시 탐색
    magical_map = explode_fireballs(magical_map)

print(count_fireballs(magical_map))
