"""
Title : 빵집
Link : https://www.acmicpc.net/problem/3109
"""

import sys
input = sys.stdin.readline


def search(row: int, col: int) -> int:
    global r, c, grid
    # 범위를 벗어남
    if row < 0 or row >= r:
        return 0
    # 마지막까지 도착
    if col == c:
        return 1
    # 건물있음
    if grid[row][col] == 'x':
        return 0
    # 지나간 길 표시
    grid[row][col] = 'x'
    # 탐색
    if search(row - 1 , col + 1):
        return 1
    if search(row, col + 1):
        return 1
    if search(row + 1, col + 1):
        return 1
    return 0


r, c = map(int, input().split())

grid = [list(input().strip()) for _ in range(r)]

pipe_count = 0
for i in range(r):
    if search(i, 0):
        pipe_count += 1
print(pipe_count)
