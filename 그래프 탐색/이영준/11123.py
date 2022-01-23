"""
Title : 양 한마리... 양 두마리...
Link : https://www.acmicpc.net/problem/11123
"""

import sys, collections
input = sys.stdin.readline


for _ in range(int(input())):
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    flocks = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                flocks += 1
                queue = collections.deque([(i, j)])
                grid[i][j] = '.'
                while queue:
                    x, y = queue.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < h and 0 <= ny < w:
                            if grid[nx][ny] == '#':
                                grid[nx][ny] = '.'
                                queue.append((nx, ny))
    
    print(flocks)
