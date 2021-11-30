import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
maps = [[0]*n for _ in range(m)]
dy = [-1, 1, 0, 0]
dx = [0,0,1,-1]
for i in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for ma in maps[ly:ry]:
        for j in range(lx, rx):
            ma[j] = 1

cnt_v = 0
cnt_list = []
q = deque()
for i in range(m):
    for j in range(n):
        if maps[i][j] == 0 :
            q.append((i,j))
            cnt = 0
            cnt_v += 1
            while q:
                y, x = q.popleft()
                if maps[y][x] == 1 :
                    continue
                maps[y][x] = 1
                cnt += 1
                for k in range(4):
                    ny, nx = y+dy[k], x+dx[k]
                    if m > ny >= 0 and n > nx >= 0 and maps[ny][nx] == 0 :
                        q.append((ny, nx))
            cnt_list.append(cnt)
cnt_list.sort()
print(cnt_v)
print(*cnt_list)