"""
Title : 늑대와 양
Link : https://www.acmicpc.net/problem/16956
"""

import sys
input = sys.stdin.readline


R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]

able = True
for i in range(R):
    if not able:
        break
    for j in range(C):
        if i < R - 1 and {grid[i][j], grid[i + 1][j]} == {'S', 'W'}:
            able = False
            break
        if j < C - 1 and {grid[i][j], grid[i][j + 1]} == {'S', 'W'}:
            able = False
            break

if able:
    print(1)
    for line in grid:
        line = line.replace('.', 'D')
        print(line)
else:
    print(0)
