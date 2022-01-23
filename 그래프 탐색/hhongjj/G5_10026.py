# G5 10026 적록색약
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
from collections import deque


def three_color():
    visited = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    alpha = color[0][0]
    n = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            n += 1
            alpha = color[i][j]
            stack = deque()
            stack.append((i, j))
            visited[i][j] = 1
            while stack:
                r, c = stack.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if nr < 0 or nc < 0 or nr >= N or nc >= N or visited[nr][nc]:
                        continue
                    # 같은 구역만 찾고 넘긴다.
                    if alpha != color[nr][nc]:
                        continue
                    stack.append((nr, nc))
                    visited[nr][nc] = 1
    return n


def two_color():
    visited = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    alpha = color[0][0]
    n = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            n += 1
            alpha = color[i][j]
            stack = deque()
            stack.append((i, j))
            visited[i][j] = n
            while stack:
                r, c = stack.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if nr < 0 or nc < 0 or nr >= N or nc >= N or visited[nr][nc]:
                        continue
                    # 찾고 있는 구역이 R이거나 G 일때 R과 G인 구역만 찾는다.
                    if alpha == 'R' or alpha == 'G':
                        if color[nr][nc] == 'B':
                            continue
                    else:
                        if color[nr][nc] == 'R' or color[nr][nc] == 'G':
                            continue
                    stack.append((nr, nc))
                    visited[nr][nc] = n

    return n


N = int(input())
color = []
for _ in range(N):
    color.append(list(input()))

# 빨강 != 초록
three_res = three_color()
print(three_res, end=' ')
# 빨강 == 초록
two_res = two_color()
print(two_res)
