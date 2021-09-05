'''
Title : 영역 구하기
Link : https://www.acmicpc.net/problem/2583
'''

import sys, collections

input = sys.stdin.readline

m, n, k = map(int, input().split())

spaces = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            spaces[j][i] = 1

area = 0
areas = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(m):
    for j in range(n):
        if spaces[i][j] == 0:
            queue = collections.deque([(i, j)])
            area += 1
            area_count = 1
            while queue:
                x, y = queue.popleft()
                spaces[x][y] = 2
                for k in range(4):
                    x2, y2 = x + dx[k], y + dy[k]
                    if x2 < 0 or x2 >= m:
                        continue
                    if y2 < 0 or y2 >= n:
                        continue
                    if spaces[x2][y2] == 0:
                        spaces[x2][y2] = 2
                        queue.append((x2, y2))
                        area_count += 1
            areas.append(area_count)

print(area)
print(*sorted(areas))