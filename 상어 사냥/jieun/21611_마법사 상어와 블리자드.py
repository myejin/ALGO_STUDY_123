import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

# 좌 하 우 상
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

blizard = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, input().split())

# 구슬 없으면 0, 상어 0
grid = [list(map(int, input().split())) for _ in range(N)]

magic_shark = [(N+1)//2 - 1, (N+1)//2 - 1]

ans = 0
for _ in range(M):
    # 블리자드 마법 방향 d, 거리 s
    d, s = map(int, input().split())
    # 블리자드로 구슬 파괴
    y, x = magic_shark
    for i in range(s):
        dr, dc = blizard[d-1]
        ny, nx = y+dr, x+dc
        if 0 <= ny < N and 0 <= nx < N:
            grid[ny][nx] = 0
        y, x = ny, nx

    q = deque()
    turn = 0
    dire = 0
    cnt = 0
    move = 1
    y, x = magic_shark
    while True:
        if y == 0 and x == 0:
            break
        ny, nx = y + dy[dire], x + dx[dire]
        if grid[ny][nx]:
            q.append(grid[ny][nx])
        cnt += 1
        if cnt == move:
            dire = (dire + 1) % 4
            turn += 1
            cnt = 0
            if turn % 2 == 0:
                move += 1

        y, x = ny, nx

    # 큐 돌면서 구슬 폭발

    while True:
        if not q:
            break
        isFalse = True
        first_num = q[0]
        num = 1
        new_q = deque()
        for i in range(1, len(q)):
            if first_num != q[i]:
                if num >= 4:
                    ans += first_num * num
                    isFalse = False
                else:
                    for _ in range(num):
                        new_q.append(first_num)
                first_num = q[i]
                num = 1
            else:
                num += 1
        if num >= 4:
            ans += first_num * num
            isFalse = False
        else:
            for _ in range(num):
                new_q.append(first_num)
        q = deepcopy(new_q)
        if isFalse:
            break
    if q:
        new_q = deque()
        first_num = q[0]
        num = 1
        for i in range(1, len(q)):
            if first_num != q[i]:
                new_q.append(num)
                new_q.append(first_num)
                num = 1
                first_num = q[i]
            else:
                num += 1
        new_q.append(num)
        new_q.append(first_num)
        q = deepcopy(new_q)

    grid = [[0]*N for _ in range(N)]
    turn = 0
    dire = 0
    cnt = 0
    move = 1
    y, x = magic_shark
    for idx in range(len(q)):
        if not q:
            break
        if y == 0 and x == 0:
            break
        ny, nx = y + dy[dire], x + dx[dire]
        grid[ny][nx] = q[idx]
        cnt += 1
        if cnt == move:
            dire = (dire + 1) % 4
            turn += 1
            cnt = 0
            if turn % 2 == 0:
                move += 1

        y, x = ny, nx

print(ans)

