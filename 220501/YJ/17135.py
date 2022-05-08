"""
Title : 캐슬 디펜스
Link : https://www.acmicpc.net/problem/17135
"""

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def simulate(x: int, y: int, z: int, grid: list) -> int:
    global N, M
    count = 0
    new_grid = [line[::] for line in grid]
    for i in range(N, 0, -1):
        enemy = set()
        for w in (x, y, z):
            pos = search(i, w, new_grid)
            if pos:
                enemy.add(pos)
        for a, b in enemy:
            count += 1
            new_grid[a][b] = 0
    return count


def search(i: int, j: int, new_grid: list) -> tuple:
    global N, M, D
    for d in range(1, D + 1):
        for k in range(d):
            x, y = i - 1 - k, j + 1 - d + k
            if 0 <= x < N and 0 <= y < M:
                if new_grid[x][y]:
                    return(x, y)
        for k in range(d - 1):
            x, y = i - d + 1 - k, j + 1 + k
            if 0 <= x < N and 0 <= y < M:
                if new_grid[x][y]:
                    return(x, y)
    return ()


if __name__ == "__main__":
    N, M, D = MIIS()
    grid = [list(MIIS()) for _ in range(N)]    
    max_count = 0
    for x, y, z in list(combinations(range(M), 3)):
        count = simulate(x, y, z, grid)
        if max_count < count:
            max_count = count
    print(max_count)

'''
2 4 2
1 1 1 1
0 1 1 0
ans : 5

4 5 2
1 0 0 1 1
0 1 1 1 0
1 1 1 0 0
1 0 1 0 1
ans : 11
'''
