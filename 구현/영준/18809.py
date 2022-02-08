"""
Title : Gaaaaaaaaaarden
Link : https://www.acmicpc.net/problem/18809
"""

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def make_search_garden(garden, spreads, greens):
    global N, M
    search_garden = [garden_line[::] for garden_line in garden]
    for x, y in greens:
        search_garden[x][y] = 3
    for x, y in spreads:
        if search_garden[x][y] == 2:
            search_garden[x][y] = 4
    return search_garden


def search(search_garden, spreads):
    global N, M
    global dx, dy
    flowers = set()
    queue = deque([])
    for x, y in spreads:
        queue.append((x, y, search_garden[x][y]))
    while True:
        next_queue = deque([])
        while queue:
            x, y, c = queue.popleft()
            if search_garden[x][y] == 5:
                continue
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    if search_garden[nx][ny] == 1 or search_garden[nx][ny] == 2:
                        next_queue.append((nx, ny, c))
        if not next_queue:
            break
        for x, y, c in next_queue:
            if search_garden[x][y] == c:
                continue
            elif search_garden[x][y] == 1 or search_garden[x][y] == 2:
                search_garden[x][y] = c
                queue.append((x, y, c))
            else:
                search_garden[x][y] = 5
                flowers.add((x, y))
    return len(list(flowers))


N, M, G, R = MIIS()
garden = [list(MIIS()) for _ in range(N)]
possible = list()
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            possible.append((i, j))

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
max_flower = 0
for spreads in list(combinations(possible, G + R)):
    for greens in list(combinations(spreads, G)):
        search_garden = make_search_garden(garden, spreads, greens)
        flower = search(search_garden, spreads)
        if max_flower < flower:
            max_flower = flower

print(max_flower)
