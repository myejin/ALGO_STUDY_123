# S2 7562 나이트의 이동
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

from collections import deque

def bfs(l, sr, sc, er, ec):
    visited = [[0]*l for _ in range(l)]
    visited[sr][sc] = 1
    stack = deque()
    stack.append((sr, sc, 0))
    dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    dc = [-2, -1, 1, 2, 2, 1, -1, -2]

    while stack:
        # n을 이용해 방문횟수를 센다
        r, c, n = stack.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= l or nc >= l or visited[nr][nc]:
                continue
            # 도착점에 도착했다면 n+1을 return 해줌
            if nr == er and nc == ec:
                return n+1
            # 도착점에 도착하지 못했다면 visited 를 1로 바꿔주고 stack에 추가하는데 그 떄 n+1를 해줘서 방문횟수를 늘려준다.
            visited[nr][nc] = 1
            stack.append((nr, nc, n+1))


T = int(input())
for _ in range(T):
    l = int(input())
    # 시작점
    sr, sc = map(int, input().split())
    # 도착점
    er, ec = map(int, input().split())
    # 시작점과 도착점이 같으면 계산하지 않고 0 출력
    if sr == er and sc == ec:
        print(0)
    else:
        res = bfs(l, sr, sc, er, ec)
        print(res)