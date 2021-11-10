"""
Title : 박스 그림 문자
Link : https://www.acmicpc.net/problem/23038
"""

import sys
input = sys.stdin.readline


N, M = map(int ,input().split())
box_character = [list(input().strip()) for _ in range(N * 3)]

for i in range(N):
    for j in range(M):
        if not (i + j) % 2:
            continue
        # 중간을 채워줘야 하는지
        is_center = False
        # 중심 기준 4방향 확인
        if i > 0 and box_character[i * 3 - 1][j * 3 + 1] == '#':
            box_character[i * 3][j * 3 + 1] = '#'
            is_center = True
        if i < N - 1 and box_character[i * 3 + 3][j * 3 + 1] == '#':
            box_character[i * 3 + 2][j * 3 + 1] = '#'
            is_center = True
        if j > 0 and box_character[i * 3 + 1][j * 3 - 1] == '#':
            box_character[i * 3 + 1][j * 3] = '#'
            is_center = True
        if j < M - 1 and box_character[i * 3 + 1][j * 3 + 3] == '#':
            box_character[i * 3 + 1][j * 3 + 2] = '#'
            is_center = True
        if is_center:
            box_character[i * 3 + 1][j * 3 + 1] = '#'

for line in box_character:
    print(*line, sep='')


'''
2 3
.........
.........
.........
.........
.........
.........

3 2
......
......
......
......
......
......
......
......
......

'''