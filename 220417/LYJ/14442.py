"""
Title : 벽 부수고 이동하기 2
Link : https://www.acmicpc.net/problem/14442
"""

from collections import deque
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    my_map = [list(input().strip()) for _ in range(N)]
    visited = [[[1_000_000] * (K + 1) for _ in range(M)] for _ in range(N)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    queue = deque([(0, 0, 0, 1)])
    while queue:
        x, y, wall, move = queue.popleft()
        if move >= visited[x][y][wall]:
            continue
        visited[x][y][wall] = move
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            is_wall = int(my_map[nx][ny])
            if wall == K and is_wall:
                continue
            if move < visited[nx][ny][wall + is_wall]:
                queue.append((nx, ny, wall + is_wall, move + 1))
    min_move = min(visited[N - 1][M - 1])
    print(-1 if min_move == 1_000_000 else min_move)
