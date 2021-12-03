import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 경로를 dfs로 탐색
def dfs(x, y):
    global dp
    if x == M-1 and y == N-1:
        return 1
    # 델타 탐색에서 얻을 수 있는 경로의 수
    goal_cnt = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < M and 0 <= ny < N and MAP[nx][ny] < MAP[x][y]:
            # 이미 탐색된 지점인 경우 바로 경우의 수 저장
            if dp[nx][ny] >= 0:
                goal_cnt += dp[nx][ny]
                continue
            goal_cnt += dfs(nx, ny)
    # 델타 탐색에서 얻을 수 있는 경로 수의 합 저장
    dp[x][y] = goal_cnt
    return goal_cnt


M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]  # 해당 지점에서 목적지까지 갈 수 있는 경우의 수 저장
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

dfs(0, 0)

print(dp[0][0])