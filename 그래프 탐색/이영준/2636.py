"""
Title : 치즈 
Link : https://www.acmicpc.net/problem/2636
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


H, W = MIIS()
grid = [list(MIIS()) for _ in range(H)]

dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
search = [(0, 0)]
next_search = []
cheese_count = 0
last_cheese_count = 0
count = H * W
time = 0
while count:
    next_search = []
    cheese_count = 0
    while search:
        x, y = search.pop()
        if grid[x][y] == -1:
            continue
        if grid[x][y] == 1:
            cheese_count += 1
        count -= 1
        grid[x][y] = -1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != -1:
                if grid[nx][ny] == 0:
                    search.append((nx, ny))
                elif grid[nx][ny] == 1:
                    next_search.append((nx, ny))
    last_cheese_count = cheese_count
    search = next_search[::]
    time += 1

print(time - 1)
print(last_cheese_count)
